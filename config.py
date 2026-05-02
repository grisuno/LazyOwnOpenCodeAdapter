from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Config:
    """
    Configuration for the LazyOwn OpenCode adapter.

    All paths are resolved relative to the LazyOwn installation directory.
    No absolute paths are hardcoded, making the adapter portable across
    different machines and installations.
    """

    lazyown_dir: Path
    host: str = "127.0.0.1"
    port: int = 9872
    log_level: str = "info"
    mcp_timeout: int = 120

    @property
    def skills_dir(self) -> Path:
        return self.lazyown_dir / "skills"

    @property
    def mcp_script(self) -> Path:
        return self.skills_dir / "lazyown_mcp.py"

    @property
    def modules_dir(self) -> Path:
        return self.lazyown_dir / "modules"

    @property
    def sessions_dir(self) -> Path:
        return self.lazyown_dir / "sessions"

    @property
    def payload_file(self) -> Path:
        return self.lazyown_dir / "payload.json"
