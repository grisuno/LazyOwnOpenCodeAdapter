# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `Config`, `LazyOwnMcpClient`, `LazyOwnOpenCodeAdapter`, `ToolCallRequest`, `ToolDefinition`, `__init__`, `_create_app`, `_find_lazyown_dir`. Core file: `adapter.py` (19 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `adapter.py` | py | presentation | 19 | no |
| `config.py` | py | infrastructure | 6 | no |

## Key Symbols

- `ToolCallRequest` (class, `adapter.py:20`) `class ToolCallRequest(BaseModel)` - Request body for executing a tool by name.
- `ToolDefinition` (class, `adapter.py:27`) `class ToolDefinition(BaseModel)` - OpenAI-compatible function definition.
- `LazyOwnMcpClient` (class, `adapter.py:35`) `class LazyOwnMcpClient` - Client for the LazyOwn MCP server.
- `__init__` (method, `adapter.py:43`) `def __init__(self, config)`
- `connect` (method, `adapter.py:49`) `def connect(self)` - Establish a stdio connection to the LazyOwn MCP server.
- `disconnect` (method, `adapter.py:69`) `def disconnect(self)` - Close the connection to the LazyOwn MCP server.
- `list_tools` (method, `adapter.py:79`) `def list_tools(self)` - List all available tools from the LazyOwn MCP server.
- `call_tool` (method, `adapter.py:98`) `def call_tool(self, name, arguments)` - Call a tool by name with the given arguments.
- `LazyOwnOpenCodeAdapter` (class, `adapter.py:107`) `class LazyOwnOpenCodeAdapter` - Adapter that exposes LazyOwn MCP tools as OpenAI-compatible functions.
- `__init__` (method, `adapter.py:116`) `def __init__(self, config)`
- `_create_app` (method, `adapter.py:121`) `def _create_app(self)` - Create and configure the FastAPI application.
- `lifespan` (method, `adapter.py:125`) `def lifespan(app)`
- `health` (method, `adapter.py:138`) `def health()` - Health check endpoint.
- `list_tools` (method, `adapter.py:143`) `def list_tools()` - List all available LazyOwn tools in OpenAI function format.
- `call_tool` (method, `adapter.py:148`) `def call_tool(request)` - Execute a LazyOwn tool by name with the provided arguments.
- `get_config` (method, `adapter.py:158`) `def get_config()` - Return the current adapter configuration.
- `run` (method, `adapter.py:168`) `def run(self)` - Start the adapter HTTP server.
- `main` (method, `adapter.py:185`) `def main()` - Entry point for the adapter CLI.
- `_find_lazyown_dir` (method, `adapter.py:191`) `def _find_lazyown_dir()`
- `Config` (class, `config.py:6`) `class Config` - Configuration for the LazyOwn OpenCode adapter.
- `skills_dir` (method, `config.py:22`) `def skills_dir(self)`
- `mcp_script` (method, `config.py:26`) `def mcp_script(self)`
- `modules_dir` (method, `config.py:30`) `def modules_dir(self)`
- `sessions_dir` (method, `config.py:34`) `def sessions_dir(self)`
- `payload_file` (method, `config.py:38`) `def payload_file(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (root) and community 1 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `adapter.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `adapter.py`
- `config.py`
