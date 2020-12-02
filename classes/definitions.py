from enum import Enum
import pandas as pd


KEYWORDS = {
    'int': 0,
    'float': 1,
    'double': 2,
    'char': 3,
    'long': 4,
    'short': 5,
    'string': 6
}


DELIMITERS = ['(', ')', '[', ']', '{', '}',
              '.', ',', ':', ';']


OPERATORS = ['*', '%', '~', '!']


COMPRASIONSF = ['>', '<']


class States(Enum):
    IDLE = 0  # +
    ID = 1  # + var
    INT = 2  # + const
    FLOAT = 3  # + const
    CHAR = 4  # + const
    STRING = 5  # + const
    KEYWORD = 6  # + var type_name
    DELIM = 7  # +
    ASSIGNMENT = 8  # +
    COMPRASIONF = 9  # +
    COMPRASION = 10  # + comp_operator
    PLUS = 11  # +
    MINUS = 12  # +
    PPFIX = 13  # + ppfix_operator
    AND = 14  # + log_operator
    OR = 15  # + log_operator
    DIVIDE = 16  # + md_operator
    OPERATOR = 17  # + pm_operator md_operator
    SCOMMENT = 18  # +
    ERROR = 19  # +


class Terminals(Enum):
    SEMICOLON = 0
    OPEN_CURBR = 1
    CLOSE_CURBR = 2
    VAR = 3
    ASSIGNMENT = 4
    LOG_OPERATOR = 5
    COMP_OPERATOR = 6
    PM_OPERATOR = 7
    MD_OPERATOR = 8
    OPEN_PAR = 9
    TYPE_NAME = 10
    CLOSE_PAR = 11
    CONST = 12
    PPFIX_OPERATOR = 13
    UNARY_OPERATOR = 14
    END_SYMBOL = 15


class NonTerminals(Enum):
    STATS = 0
    STAT = 1
    ASSIGNMENT_EXP = 2
    EXPRESSION = 3
    LOG_EXP = 4
    ADDITIVE_EXP = 5
    MULT_EXP = 6
    CAST_EXP = 7
    UNARY_EXP = 8
