from dataclasses import dataclass, field
from .severity import Severity

@dataclass
class Diagnostic:

    code: str
    severity: Severity

    message: str

    line: int = 1
    column: int = 1

    recoverable: bool = True

    hint: str | None = None

@dataclass
class DiagnosticCollection:
    diagnostics: list[Diagnostic] = field(default_factory=list)

    def error(self, code, message, hint):
        self.diagnostics.append(Diagnostic(code, Severity.ERROR, message, hint=hint))
    
    def warning(self, code, message, hint):
        self.diagnostics.append(Diagnostic(code, Severity.WARNING, message, hint=hint))
    
    def fatal(self, code, message):
        self.diagnostics.append(Diagnostic(code, Severity.FATAL, message))