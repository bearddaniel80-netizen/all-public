from dataclasses import dataclass
from typing import Optional, Any

@dataclass(frozen=True)
class ConfigContext:
    source: str
    format: str
    ddl: Optional[str]
    limit: int
    offset: int
    debug: bool
    profile: Optional[str]

    # extensibility escape hatch
    extras: dict[str, Any]