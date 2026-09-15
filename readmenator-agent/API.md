# API

## adapter.py

### main (method) `def main()`
- Defined: `adapter.py:185`
- Doc: Entry point for the adapter CLI.
- Depends on: `config.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `adapter.py:43`
- Depends on: `config.py`

### connect (method) `def connect(self)`
- Defined: `adapter.py:49`
- Doc: Establish a stdio connection to the LazyOwn MCP server.
- Depends on: `config.py`

### disconnect (method) `def disconnect(self)`
- Defined: `adapter.py:69`
- Doc: Close the connection to the LazyOwn MCP server.
- Depends on: `config.py`

### list_tools (method) `def list_tools(self)`
- Defined: `adapter.py:79`
- Doc: List all available tools from the LazyOwn MCP server.
- Depends on: `config.py`

### call_tool (method) `def call_tool(self, name, arguments)`
- Defined: `adapter.py:98`
- Doc: Call a tool by name with the given arguments.
- Depends on: `config.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `adapter.py:116`
- Depends on: `config.py`

### _create_app (method) `def _create_app(self)`
- Defined: `adapter.py:121`
- Doc: Create and configure the FastAPI application.
- Depends on: `config.py`

### run (method) `def run(self)`
- Defined: `adapter.py:168`
- Doc: Start the adapter HTTP server.
- Depends on: `config.py`

### _find_lazyown_dir (method) `def _find_lazyown_dir()`
- Defined: `adapter.py:191`
- Depends on: `config.py`

### lifespan (method) `def lifespan(app)`
- Defined: `adapter.py:125`
- Depends on: `config.py`

### health (method) `def health()`
- Defined: `adapter.py:138`
- Doc: Health check endpoint.
- Depends on: `config.py`

### list_tools (method) `def list_tools()`
- Defined: `adapter.py:143`
- Doc: List all available LazyOwn tools in OpenAI function format.
- Depends on: `config.py`

### call_tool (method) `def call_tool(request)`
- Defined: `adapter.py:148`
- Doc: Execute a LazyOwn tool by name with the provided arguments.
- Depends on: `config.py`

### get_config (method) `def get_config()`
- Defined: `adapter.py:158`
- Doc: Return the current adapter configuration.
- Depends on: `config.py`

## config.py

### skills_dir (method) `def skills_dir(self)`
- Defined: `config.py:22`
- Imported by: `adapter.py`

### mcp_script (method) `def mcp_script(self)`
- Defined: `config.py:26`
- Imported by: `adapter.py`

### modules_dir (method) `def modules_dir(self)`
- Defined: `config.py:30`
- Imported by: `adapter.py`

### sessions_dir (method) `def sessions_dir(self)`
- Defined: `config.py:34`
- Imported by: `adapter.py`

### payload_file (method) `def payload_file(self)`
- Defined: `config.py:38`
- Imported by: `adapter.py`
