# API

## adapter.py
Depends on: `config.py`
- `LazyOwnMcpClient.__init__` (method) `adapter.py:43` `def __init__(self, config)`
- `LazyOwnMcpClient.connect` (method) `adapter.py:49` `def connect(self)` -- Establish a stdio connection to the LazyOwn MCP server.
- `LazyOwnMcpClient.disconnect` (method) `adapter.py:69` `def disconnect(self)` -- Close the connection to the LazyOwn MCP server.
- `LazyOwnMcpClient.list_tools` (method) `adapter.py:79` `def list_tools(self)` -- List all available tools from the LazyOwn MCP server.
- `LazyOwnMcpClient.call_tool` (method) `adapter.py:98` `def call_tool(self, name, arguments)` -- Call a tool by name with the given arguments.
- `LazyOwnOpenCodeAdapter.__init__` (method) `adapter.py:116` `def __init__(self, config)`
- `LazyOwnOpenCodeAdapter.lifespan` (method) `adapter.py:125` `def lifespan(app)`
- `LazyOwnOpenCodeAdapter.health` (method) `adapter.py:138` `def health()` -- Health check endpoint.
- `LazyOwnOpenCodeAdapter.list_tools` (method) `adapter.py:143` `def list_tools()` -- List all available LazyOwn tools in OpenAI function format.
- `LazyOwnOpenCodeAdapter.call_tool` (method) `adapter.py:148` `def call_tool(request)` -- Execute a LazyOwn tool by name with the provided arguments.
- `LazyOwnOpenCodeAdapter.get_config` (method) `adapter.py:158` `def get_config()` -- Return the current adapter configuration.
- `LazyOwnOpenCodeAdapter.run` (method) `adapter.py:168` `def run(self)` -- Start the adapter HTTP server.
- `LazyOwnOpenCodeAdapter.main` (method) `adapter.py:185` `def main()` -- Entry point for the adapter CLI.

## config.py
Imported by: `adapter.py`
- `Config.skills_dir` (method) `config.py:22` `def skills_dir(self)`
- `Config.mcp_script` (method) `config.py:26` `def mcp_script(self)`
- `Config.modules_dir` (method) `config.py:30` `def modules_dir(self)`
- `Config.sessions_dir` (method) `config.py:34` `def sessions_dir(self)`
- `Config.payload_file` (method) `config.py:38` `def payload_file(self)`
