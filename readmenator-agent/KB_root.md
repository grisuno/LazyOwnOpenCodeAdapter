# Subsystem: root

## adapter.py
- Doc: ToolCallRequest: Request body for executing a tool by name.
- Layer: presentation
- Language: py
- Symbols:
  - `ToolCallRequest` (class, line 20) `class ToolCallRequest(BaseModel)`
  - `ToolDefinition` (class, line 27) `class ToolDefinition(BaseModel)`
  - `LazyOwnMcpClient` (class, line 35) `class LazyOwnMcpClient`
  - `LazyOwnOpenCodeAdapter` (class, line 107) `class LazyOwnOpenCodeAdapter`
  - `main` (method, line 185) `def main()`
  - `__init__` (method, line 43) `def __init__(self, config)`
  - `connect` (method, line 49) `def connect(self)`
  - `disconnect` (method, line 69) `def disconnect(self)`
  - `list_tools` (method, line 79) `def list_tools(self)`
  - `call_tool` (method, line 98) `def call_tool(self, name, arguments)`
  - `__init__` (method, line 116) `def __init__(self, config)`
  - `_create_app` (method, line 121) `def _create_app(self)`
  - `run` (method, line 168) `def run(self)`
  - `_find_lazyown_dir` (method, line 191) `def _find_lazyown_dir()`
  - `lifespan` (method, line 125) `def lifespan(app)`
  - `health` (method, line 138) `def health()`
  - `list_tools` (method, line 143) `def list_tools()`
  - `call_tool` (method, line 148) `def call_tool(request)`
  - `get_config` (method, line 158) `def get_config()`
- Depends on: `config.py`

## app.py
- Doc: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación...
- Layer: utility
- Language: py

## config.py
- Doc: Config: Configuration for the LazyOwn OpenCode adapter.
- Layer: infrastructure
- Language: py
- Symbols:
  - `Config` (class, line 6) `class Config`
  - `skills_dir` (method, line 22) `def skills_dir(self)`
  - `mcp_script` (method, line 26) `def mcp_script(self)`
  - `modules_dir` (method, line 30) `def modules_dir(self)`
  - `sessions_dir` (method, line 34) `def sessions_dir(self)`
  - `payload_file` (method, line 38) `def payload_file(self)`
- Imported by: `adapter.py`

## install.sh
- Layer: utility
- Language: sh
