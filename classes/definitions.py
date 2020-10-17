from enum import Enum


KEYWORDS = {
    'int': 0,
    'float': 1,
    'double': 2,
    'char': 3,
    'long': 4,
    'short': 5,
    'string': 6,
    'if': 7,
    'else': 8,
}


DELIMITERS = ['(', ')', '[', ']', '{', '}',
              '.', ',', ':', ';']


OPERATORS = ['*', '%', '~', '!']


COMPRASIONSF = ['>', '<']


class States(Enum):
    IDLE = 0 # +
    ID = 1 # + 
    INT = 2 # +
    FLOAT = 3 # +
    CHAR = 4 # +
    STRING = 5 # +
    KEYWORD = 6 # + 
    DELIM = 7 # + 
    ASSIGNMENT = 8 # + 
    COMPRASIONF = 9 # +
    COMPRASION = 10 # +
    PLUS = 11 # +
    MINUS = 12 # + 
    PPFIX = 13 # +
    AND = 14 # +
    OR = 15 # +
    DIVIDE = 16 # +
    OPERATOR = 17 # +
    SCOMMENT = 18 # +
    ERROR = 19 # +