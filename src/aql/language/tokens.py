
from dataclasses import dataclass
from enum import Enum

class TokenType(str, Enum):
    AS = "AS"
    ALL = "ALL"
    ASC = "ASC"
    AND = "AND"
    BETWEEN = "BETWEEN"
    BY = "BY"
    CONTAINS = "CONTAINS"
    DECLARE = "DECLARE"
    DESC = "DESC"
    DESCRIBE = "DESCRIBE"
    ENDSWITH = "ENDSWITH"
    EOF = "EOF"
    EXCEPT = "EXCEPT"
    FROM = "FROM"
    GROUP = "GROUP"
    HAVING = "HAVING"
    IDENT = "IDENT"
    IN = "IN"
    INTERSECT = "INTERSECT"
    LIKE = "LIKE"
    LIMIT = "LIMIT"
    LITERAL = "LITERAL"       # a, b, c, 1, ., etc.
    MATCH = "MATCH"
    NOT = "NOT"
    NUMBER = "NUMBER"
    OR = "OR"
    ORDER = "ORDER"
    RECURSIVE = "RECURSIVE"
    SELECT = "SELECT"
    SHOW = "SHOW"
    STARTSWITH = "STARTSWITH"
    STRING = "STRING"
    WHERE = "WHERE"
    WITH = "WITH"
    UNION = "UNION"
    USING = "USING"
    LPAREN = "("
    RPAREN = ")"
    EQ = "="
    LT = "<"
    GT = ">"
    NEQ = "!="
    LTE = "<="
    GTE = ">="
    ADD_OP = "+"
    REGMATCH = "~="
    STAR = "*"
    LBRACK = "["
    RBRACK = "]"
    COMMA = ","
    PERCENT = "%"        # %
    QUESTION = "?"      # ?   (or UNDERSCORE if you go SQL style)
    DASH = "-"          # -
    CARET = "^"         # ^   (only if you support negation in charclass)
    ESCAPE = "\\"        # \   (if you support escaping)

@dataclass
class Token:
    type: str
    value: str