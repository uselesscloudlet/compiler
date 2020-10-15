from enum import Enum


KEYWORDS = {
    'int': 0,
    'float': 1,
    'char': 2,
    'long': 3,
    'short': 4,
    'string': 5,
    'if': 6,
    'else': 7,
    'for': 8,
    'while': 9,
    'return': 10
}


DELIMITERS = ['(', ')', '[', ']', '{', '}',
              '.', ',', ':', ';']


OPERATORS = ['*', '%']


COMPRASIONSF = ['>', '<']


class States(Enum):
    IDLE = 0 # +
    ID = 1 # + 
    INT = 2 # +
    FLOAT = 3 # + без E
    STRING = 4
    KEYWORD = 5 # + 
    DELIM = 6 # + 
    ASSIGNMENT = 7 # + 
    COMPRASIONF = 8 # +
    COMPRASION = 9 # +
    PLUS = 10 # +
    MINUS = 11 # + 
    PPFIX = 12 # +
    AND = 13 # +
    OR = 14 # +
    DIVIDE = 15 # +
    OPERATOR = 16 # +
    SCOMMENT = 17 # +
    ERROR = 18 # +