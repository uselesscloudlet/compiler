from classes.definitions import DELIMITERS, KEYWORDS, Terminals, States


class Parser:
    __slots__ = ['__lexems', '__currentLexem']

    def __init__(self, lexems):
        self.__lexems = lexems
        self.__currentLexem = 0

    def next_lexem(self):
        if (self.__currentLexem >= len(self.__lexems)):
            return Terminals.END_SYMBOL

        lexem = self.__lexems[self.__currentLexem]
        if (lexem.cl == States.SCOMMENT):
            self.__currentLexem += 1
            return self.next_lexem()
        elif (lexem.cl in [States.AND, States.OR]):
            lexem.term = Terminals.LOG_OPERATOR
        elif (lexem.cl == States.COMPRASION):
            lexem.term = Terminals.COMP_OPERATOR
        elif (lexem.cl == States.OPERATOR and
              lexem.value in ['+', '-']):
            lexem.term = Terminals.PM_OPERATOR
        elif (lexem.cl == States.OPERATOR and
              lexem.value in ['*', '/']):
            lexem.term = Terminals.MD_OPERATOR
        elif (lexem.cl == States.PPFIX):
            lexem.term = Terminals.PPFIX_OPERATOR
        elif (lexem.cl == States.OPERATOR and
              lexem.value in ['&', '|']):
            lexem.term = Terminals.UNARY_OPERATOR
        elif (lexem.cl == States.ID):
            lexem.term = Terminals.VAR
        elif (lexem.cl == States.KEYWORD and
              lexem.value in ['int', 'float', 'char', 'string']):
            lexem.term = Terminals.TYPE_NAME
        elif (lexem.cl == States.DELIM and
              lexem.value == '('):
            lexem.term = Terminals.OPEN_PAR
        elif (lexem.cl == States.DELIM and
              lexem.value == ')'):
            lexem.term = Terminals.CLOSE_PAR
        elif (lexem.cl == States.DELIM and
              lexem.value == '{'):
            lexem.term = Terminals.OPEN_CURBR
        elif (lexem.cl == States.DELIM and
              lexem.value == '}'):
            lexem.term = Terminals.CLOSE_CURBR
        elif (lexem.cl == States.DELIM and
              lexem.value == ';'):
            lexem.term = Terminals.SEMICOLON
        elif (lexem.cl == States.DELIM and
              lexem.value == '='):
            lexem.term = Terminals.ASSIGNMENT
        elif (lexem.cl in [States.INT, States.FLOAT, States.CHAR, States.STRING]):
            lexem.term = Terminals.CONST

        self.__currentLexem += 1
        return lexem
    

