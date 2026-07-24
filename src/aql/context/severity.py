from enum import Enum

class Severity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"
    INTERNAL = "internal"