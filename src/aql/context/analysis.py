from dataclasses import dataclass, field
from .severity import Severity
from .metadata import Metadata
# from ..validate.rules.identifier.symbol_resolver import Binder

@dataclass
class AnalysisContext:

#    def __init__(self):
#
#        self.symbol_resolver = Binder()

    #
    # Input
    #
    text: str = ""

    artifacts: dict = field(default_factory=dict)

    current_node = None

    tables: dict = field(default_factory=dict)

    ctes: dict = field(default_factory=dict)

    macros: dict = field(default_factory=dict)

    #
    # Analysis
    #

    @property
    def has_errors(self):

        return any(
            d.severity in (
                Severity.ERROR,
                Severity.FATAL,
                Severity.INTERNAL
            )
            for d in self.artifacts["diagnostics"].diagnostics
        )

    @property
    def has_fatal(self):

        return any(
            d.severity in (
                Severity.FATAL,
                Severity.INTERNAL
            )
            for d in self.artifacts["diagnostics"].diagnostics
        )

    # Rule helpers

#    def resolve_symbol(self, name):
#
#        return self.symbol_resolver.resolve(
#            self,
#            name
#        )

    def is_reserved(self, value):

        return (
            value.upper()
            in self.metadata["reserved_keywords"]
        )
    #
    # Shared scratch space
    #

    metadata: Metadata = None

    statistics: dict = field(default_factory=dict)

    def __repr__(self):
        return (
            f"AnalysisContext( text: {self.text} artifacts: {self.artifacts})"
        )

    def to_dict(self):
        return {
            "type": "AnalysisContext",
            "text": self.text,
        }