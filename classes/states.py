from enum import Enum


class States(Enum):
    IDLE = 0
    ID = 1
    INT = 2
    FLOAT = 3   
    KEYWORD = 4
    DELIM = 5
    ASSAGMENT = 6
    FIX = 7
    PLUS = 8
    MINUS = 9