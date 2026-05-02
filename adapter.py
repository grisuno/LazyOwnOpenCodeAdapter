import asyncio
import json
import logging
import os
import sys
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from config import Config


logger = logging.getLogger("lazyown_opencode_adapter")


class ToolCallRequest(BaseModel):
    """Request body for executing a tool by name."""

    name: str = Field(..., description="Name of the tool to call.")
    arguments: dict = Field(default_factory=dict, description="Arguments to pass to the tool.")


class ToolDefinition(BaseModel):
    """OpenAI-compatible function definition."""

    name: str
    description: str
    parameters: dict


class LazyOwnMcpClient:
    """
    Client for the LazyOwn MCP server.

    Manages a persistent stdio connection to the LazyOwn MCP server,
    providing methods to list and call tools via the Model Context Protocol.
    """

    def __init__(self, config: Config):
        self.config = config
        self.session: ClientSession | None = None
        self._stdio_context = None
        self._streams = None

    async def connect(self):
        """Establish a stdio connection to the LazyOwn MCP server."""
        env = os.environ.copy()
        env["LAZYOWN_DIR"] = str(self.config.lazyown_dir)

        params = StdioServerParameters(
            command=sys.executable,
            args=[str(self.config.mcp_script)],
            env=env,
        )

        self._stdio_context = stdio_client(params)
        self._streams = await self._stdio_context.__aenter__()
        read_stream, write_stream = self._streams

        self.session = ClientSession(read_stream, write_stream)
        await self.session.__aenter__()
        await self.session.initialize()
        logger.info("Connected to LazyOwn MCP server.")

    async def disconnect(self):
        """Close the connection to the LazyOwn MCP server."""
        if self.session:
            await self.session.__aexit__(None, None, None)
            self.session = None
        if self._stdio_context:
            await self._stdio_context.__aexit__(None, None, None)
            self._stdio_context = None
        logger.info("Disconnected from LazyOwn MCP server.")

    async def list_tools(self) -> list[ToolDefinition]:
        """List all available tools from the LazyOwn MCP server."""
        if not self.session:
            raise RuntimeError("MCP client is not connected.")

        response = await self.session.list_tools()
        tools = []

        for tool in response.tools:
            tools.append(
                ToolDefinition(
                    name=tool.name,
                    description=tool.description or "",
                    parameters=tool.inputSchema,
                )
            )

        return tools

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> list[dict]:
        """Call a tool by name with the given arguments."""
        if not self.session:
            raise RuntimeError("MCP client is not connected.")

        result = await self.session.call_tool(name, arguments)
        return [item.model_dump() for item in result.content]


class LazyOwnOpenCodeAdapter:
    """
    Adapter that exposes LazyOwn MCP tools as OpenAI-compatible functions.

    This adapter bridges the LazyOwn MCP server with OpenCode and other
    OpenAI-compatible clients by translating tool schemas and providing
    a REST interface for tool discovery and execution.
    """

    def __init__(self, config: Config):
        self.config = config
        self.client = LazyOwnMcpClient(config)
        self.app = self._create_app()

    def _create_app(self) -> FastAPI:
        """Create and configure the FastAPI application."""

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            await self.client.connect()
            yield
            await self.client.disconnect()

        app = FastAPI(
            title="LazyOwn OpenCode Adapter",
            description="OpenAI-compatible function calling adapter for the LazyOwn pentesting framework.",
            version="1.0.0",
            lifespan=lifespan,
        )

        @app.get("/health")
        async def health() -> dict:
            """Health check endpoint."""
            return {"status": "healthy"}

        @app.get("/tools", response_model=list[ToolDefinition])
        async def list_tools() -> list[ToolDefinition]:
            """List all available LazyOwn tools in OpenAI function format."""
            return await self.client.list_tools()

        @app.post("/call")
        async def call_tool(request: ToolCallRequest) -> dict:
            """Execute a LazyOwn tool by name with the provided arguments."""
            try:
                result = await self.client.call_tool(request.name, request.arguments)
                return {"tool": request.name, "result": result}
            except Exception as exc:
                logger.exception("Tool call failed: %s", request.name)
                raise HTTPException(status_code=500, detail=str(exc)) from exc

        @app.get("/config")
        async def get_config() -> dict:
            """Return the current adapter configuration."""
            return {
                "lazyown_dir": str(self.config.lazyown_dir),
                "host": self.config.host,
                "port": self.config.port,
            }

        return app

    def run(self):
        """Start the adapter HTTP server."""
        import uvicorn

        logging.basicConfig(
            level=getattr(logging, self.config.log_level.upper(), logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

        uvicorn.run(
            self.app,
            host=self.config.host,
            port=self.config.port,
            log_level=self.config.log_level,
        )


def main():
    """Entry point for the adapter CLI."""
    import argparse
    from pathlib import Path as _Path

    parser = argparse.ArgumentParser(description="LazyOwn OpenCode Adapter")
    def _find_lazyown_dir() -> _Path:
        env = os.environ.get("LAZYOWN_DIR")
        if env:
            return _Path(env)
        adapter_dir = _Path(__file__).parent.resolve()
        for candidate in [
            adapter_dir.parent.parent.parent,
            adapter_dir.parent.parent,
            adapter_dir.parent,
            _Path.cwd(),
        ]:
            if (candidate / "skills" / "lazyown_mcp.py").exists():
                return candidate
        return _Path.cwd()

    parser.add_argument(
        "--lazyown-dir",
        type=_Path,
        default=_find_lazyown_dir(),
        help="Path to the LazyOwn framework directory.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.environ.get("ADAPTER_HOST", "127.0.0.1"),
        help="Host to bind the adapter server.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("ADAPTER_PORT", "9872")),
        help="Port to bind the adapter server.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default=os.environ.get("ADAPTER_LOG_LEVEL", "info"),
        help="Logging level.",
    )

    args = parser.parse_args()

    config = Config(
        lazyown_dir=args.lazyown_dir.resolve(),
        host=args.host,
        port=args.port,
        log_level=args.log_level,
    )

    adapter = LazyOwnOpenCodeAdapter(config)
    adapter.run()


if __name__ == "__main__":
    main()
