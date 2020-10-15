from classes.definitions import States, DELIMITERS, KEYWORDS, COMPRASIONSF, OPERATORS
<<<<<<< HEAD
from classes.lexem import Lexem
=======
>>>>>>> 4e966c7375897b22f6ad2fa278b9f6fef2062616


class StateMachine:
    __slots__ = ['__currentState', '__buffer', '__idDict']

    def __init__(self):
        self.__currentState = States.IDLE
        self.__buffer = None
        self.__idDict = dict()


    @property
    def currentState(self):
        return self.__currentState
    

    @currentState.setter
    def currentState(self, state):
        self.__currentState = state


    def __isDelimiter(self, symbol):
        return symbol in DELIMITERS


    def __supFunc(self, symbol, t, attributes = None):
        result = list([Lexem(t, self.__buffer, attributes)])
        self.currentState = States.IDLE
        nextLex = self.handleSymbol(symbol)
        if nextLex is not None:
            result += nextLex
        return result


    def handleSymbol(self, symbol):
        if self.currentState == States.IDLE:
            if symbol.isdigit():
                self.__buffer = symbol
                self.currentState = States.INT
            elif symbol.isalpha():
                self.__buffer = symbol
                self.currentState = States.ID
<<<<<<< HEAD
            elif symbol == '.':
                self.__buffer = symbol
                self.currentState = States.FLOAT
            elif self.__isDelimiter(symbol):
=======
            elif self.isDelimiter(symbol):
>>>>>>> 4e966c7375897b22f6ad2fa278b9f6fef2062616
                self.__buffer = symbol
                self.currentState = States.DELIM
            elif symbol == '=':
                self.__buffer = symbol
                self.currentState = States.ASSIGNMENT
            elif symbol in COMPRASIONSF:
                self.__buffer = symbol
<<<<<<< HEAD
                self.currentState = States.COMPRASIONF
            elif symbol == '+':
                self.__buffer = symbol
                self.currentState = States.PLUS
            elif symbol == '-':
                self.__buffer = symbol
                self.currentState = States.MINUS
            elif symbol == '/':
                self.__buffer = symbol
                self.currentState = States.DIVIDE
            elif symbol == '&':
                self.__buffer = symbol
                self.currentState = States.AND
            elif symbol == '|':
                self.__buffer = symbol
                self.currentState = States.OR
            elif symbol in OPERATORS:
                self.__buffer = symbol
                self.currentState = States.OPERATOR
            elif symbol == '\"':
                self.__buffer = symbol
                self.currentState = States.STRING
=======
                self.__currentState = States.COMPRASIONSF
            elif symbol == '.':
                self.__buffer = symbol
                self.currentState = States.FLOAT
            elif symbol == '+':
                self.__buffer = symbol
                self.__currentState = States.PLUS
            elif symbol in OPERATORS:
                self.__buffer = symbol
                
            # elif symbol == '-':
            #     self.__buffer = symbol
            #     self.__currentState = States.MINUS
>>>>>>> 4e966c7375897b22f6ad2fa278b9f6fef2062616
            elif symbol.isspace():
                pass
            else:
                return [Lexem(States.ERROR, self.__buffer)]
        elif self.currentState == States.ID:
            if symbol.isalpha() or symbol.isdigit():
                self.__buffer += symbol
            else:
                if self.__buffer in KEYWORDS:
                    return self.__supFunc(symbol, States.KEYWORD, KEYWORDS[self.__buffer])
                else:
                    if self.__buffer not in self.__idDict:
                        self.__idDict[self.__buffer] = len(self.__idDict)
                    return self.__supFunc(symbol, States.ID, self.__idDict[self.__buffer])
        elif self.currentState == States.INT:
            if symbol.isdigit():
                self.__buffer += symbol
            elif symbol == '.':
                self.__buffer += symbol
                self.currentState = States.FLOAT
            else:
                return self.__supFunc(symbol, States.INT)
        elif self.currentState == States.FLOAT: # ! допилить числа с плавающей точкой
            if symbol.isdigit():
                self.__buffer += symbol
            else:
                return self.__supFunc(symbol, States.FLOAT)
        elif self.currentState == States.DELIM:
            return self.__supFunc(symbol, States.DELIM)
        elif self.currentState == States.ASSIGNMENT:
            if symbol == '=':
                self.__buffer += symbol
                self.currentState = States.COMPRASION
            else:
                return self.__supFunc(symbol, States.ASSIGNMENT)
        elif self.currentState == States.COMPRASIONF:
            if symbol == '=':
                self.__buffer += symbol
<<<<<<< HEAD
                self.currentState = States.IDLE
                return [Lexem(States.COMPRASION, self.__buffer)]
            else:
                return self.__supFunc(symbol, States.COMPRASION)
        elif self.currentState == States.COMPRASION:
            return self.__supFunc(symbol, States.COMPRASION)
        elif self.currentState == States.PLUS:
            if symbol == '+':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.PPFIX, self.__buffer)]
            elif symbol == '=':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.ASSIGNMENT, self.__buffer)]
            else:
                return self.__supFunc(symbol, States.OPERATOR)
        elif self.currentState == States.MINUS:
            if symbol == '-':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.PPFIX, self.__buffer)]
            elif symbol == '=':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.ASSIGNMENT, self.__buffer)]
            else:
                return self.__supFunc(symbol, States.OPERATOR)
        elif self.currentState == States.DIVIDE:
            if symbol == '/':
                self.__buffer += symbol
                self.currentState = States.SCOMMENT
            else:
                return self.__supFunc(symbol, States.OPERATOR)
        elif self.currentState == States.OPERATOR:
            return self.__supFunc(symbol, States.OPERATOR)
        elif self.currentState == States.AND:
            if symbol == '&':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.OPERATOR, self.__buffer)]
            else:
                return self.__supFunc(symbol, States.ERROR)
        elif self.currentState == States.OR:
            if symbol == '|':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.OPERATOR, self.__buffer)]
            else:
                return self.__supFunc(symbol, States.ERROR)
        elif self.currentState == States.STRING:
            if symbol == '\"':
                self.__buffer += symbol
                self.currentState = States.IDLE
                return [Lexem(States.STRING, self.__buffer)]
            elif symbol == '\n':
                self.currentState = States.IDLE
                return [Lexem(States.ERROR, self.__buffer)]
            else:
                self.__buffer += symbol
        elif self.currentState == States.SCOMMENT:
            if symbol == '\n':
                self.currentState = States.IDLE
                return [Lexem(States.SCOMMENT, self.__buffer)]
            else:
                self.__buffer += symbol
=======
                self.__currentState = States.IDLE
                return [self.__buffer + ' ' + 'COMPRASION']
            else:
                result = list([self.__buffer + ' ' + 'COMPRASION'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
        elif self.currentState == States.COMPRASIONS:
            result = list([self.__buffer + ' ' + 'COMPRASION'])
            self.currentState = States.IDLE
            nextLex = self.handleSymbol(symbol)
            if nextLex is not None:
                result += nextLex
            return result
        elif self.__currentState == States.PLUS:
            if symbol == '+':
                self.__buffer += symbol
                self.__currentState = States.IDLE
                return [self.__buffer + ' ' + 'PRE/POST-FIX OPERATOR']
            else:
                result = list([self.__buffer + ' ' + 'OPERATOR'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
        elif self.__currentState == States.MINUS:
            if symbol == '-':
                self.__buffer += symbol
                self.__currentState = States.IDLE
                return [self.__buffer + ' ' + 'PRE/POST-FIX OPERATOR']
            else:
                result = list([self.__buffer + ' ' + 'OPERATOR'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
>>>>>>> 4e966c7375897b22f6ad2fa278b9f6fef2062616
