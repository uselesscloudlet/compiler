from enum import Enum


DELIMITERS = ['(', ')', '[', ']', '{', '}',
              '.', ',', ':', ';', '\'', '\"']


class States(Enum):
    IDLE = 0
    ID = 1
    INT = 2
    FLOAT = 3   
    KEYWORD = 4
    DELIM = 5
    ASSIGNMENT = 6
    PPFIX = 7
    PLUS = 8
    MINUS = 9