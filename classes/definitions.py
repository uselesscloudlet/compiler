from enum import Enum


KEYWORDS = {
    'int': 0,
    'float': 1,
    'char': 2,
    'long': 3,
    'short': 4,
    'if': 5,
    'for': 6,
    'while': 7
}



DELIMITERS = ['(', ')', '[', ']', '{', '}',
              '.', ',', ':', ';', '\'', '\"']


OPERATORS = ['+', '-', '*', '/', '%',
             '&&', '||']


COMPRASIONSF = ['>', '<']


COMPRASIONS = ['>=', '<=', '==']


class States(Enum):
    IDLE = 0
    ID = 1
    INT = 2
    FLOAT = 3   
    KEYWORD = 4
    DELIM = 5
    ASSIGNMENT = 6
    COMPRASIONSF = 7
    COMPRASIONS = 8
    PPFIX = 9
    PLUS = 10
    MINUS = 11
    OPERATORS = 12