# LazyOwn OpenCode Adapter

OpenAI-compatible function calling adapter for the LazyOwn pentesting framework.

Bridges the LazyOwn MCP server with OpenCode, Kimi, and any OpenAI-compatible client by translating tool schemas and providing a REST interface for tool discovery and execution.

## Architecture

```
OpenCode / Kimi / OpenAI Client
        |
        | HTTP JSON (OpenAI function format)
        v
  LazyOwn OpenCode Adapter (this repo)
        |
        | stdio MCP protocol
        v
  LazyOwn MCP Server (lazyown_mcp.py)
        |
        | Python imports + subprocess
        v
  LazyOwn Framework
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

All configuration is parameterizable via CLI arguments or environment variables. No absolute paths are hardcoded.

### CLI Arguments

| Argument | Default | Environment Variable | Description |
|----------|---------|---------------------|-------------|
| `--lazyown-dir` | `LAZYOWN_DIR` or `/home/grisun0/LazyOwn` | `LAZYOWN_DIR` | Path to the LazyOwn framework directory. |
| `--host` | `127.0.0.1` | `ADAPTER_HOST` | Host to bind the adapter server. |
| `--port` | `9872` | `ADAPTER_PORT` | Port to bind the adapter server. |
| `--log-level` | `info` | `ADAPTER_LOG_LEVEL` | Logging level. |

### Example

```bash
python3 adapter.py --lazyown-dir /opt/LazyOwn --host 0.0.0.0 --port 8080
```

## Endpoints

### GET /health

Health check.

```bash
curl http://127.0.0.1:9872/health
```

### GET /tools

List all available LazyOwn tools in OpenAI function format.

```bash
curl http://127.0.0.1:9872/tools
```

### POST /call

Execute a tool by name with arguments.

```bash
curl -X POST http://127.0.0.1:9872/call \
  -H "Content-Type: application/json" \
  -d '{
    "name": "lazyown_set_config",
    "arguments": {
      "key": "rhost",
      "value": "10.10.11.78"
    }
  }'
```

### GET /config

Show current adapter configuration.

```bash
curl http://127.0.0.1:9872/config
```

## Using with OpenCode

Since OpenCode supports tool calling natively via HTTP, configure the adapter and then make requests to it using the standard tool calling workflow.

Example workflow:

1. Start the adapter:
   ```bash
   python3 adapter.py --lazyown-dir /path/to/LazyOwn
   ```

2. List available tools:
   ```bash
   curl -s http://127.0.0.1:9872/tools | python3 -m json.tool
   ```

3. Call a tool:
   ```bash
   curl -s -X POST http://127.0.0.1:9872/call \
     -H "Content-Type: application/json" \
     -d '{"name": "lazyown_get_config", "arguments": {}}'
   ```

## Files

| File | Description |
|------|-------------|
| `config.py` | Immutable configuration dataclass. All paths are derived from `lazyown_dir`. |
| `adapter.py` | FastAPI application + MCP client + OpenAI function translator. |
| `requirements.txt` | Python dependencies. |

## Requirements

- Python 3.10+
- LazyOwn framework installed at any path (configured via `--lazyown-dir`)
- `mcp` Python SDK (installed automatically via requirements.txt)

## License

Same as LazyOwn.


---
### Grisuno Offensive Security Ecosystem
This tool is part of a broader, synergistic RedTeam workflow:
- [LazyOwn](https://github.com/grisuno/LazyOwn): RedTeam/APT framework with AI-powered C&C, rootkits and malleable implants (Windows/Linux/Mac).
- [LazyOwnBT](https://github.com/grisuno/LazyOwnBT): Advanced complementary toolkit for BlueTeam professionals.
- [Lazymapd](https://github.com/grisuno/Lazymapd): Fast, customizable port scanner for firewall evasion.

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity

AI agents: Read `readmenator-agent/INDEX.md` for fast project context.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

