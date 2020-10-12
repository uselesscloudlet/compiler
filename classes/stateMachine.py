from classes.definitions import States, DELIMITERS


class StateMachine:
    def __init__(self):
        self.__currentState = States.IDLE
        self.__buffer = None


    @property
    def currentState(self):
        return self.__currentState
    

    @currentState.setter
    def currentState(self, state):
        self.__currentState = state


    def isDelimiter(self, symbol):
        return symbol in DELIMITERS


    def handleSymbol(self, symbol):
        if self.currentState == States.IDLE:
            if symbol.isdigit():
                self.__buffer = symbol
                self.currentState = States.INT
            elif symbol.isalpha():
                self.__buffer = symbol
                self.currentState = States.ID
            elif symbol == '.':
                self.__buffer = symbol
                self.currentState = States.FLOAT
            # ? Сделать с KEYWORD
            # elif self.isDelimiter(symbol):
            #     self.__buffer = symbol
            #     self.currentState = States.DELIM
            elif symbol.isspace():
                pass
            else:
                return [symbol + " error"]
        elif self.currentState == States.ID:
            if symbol.isalpha() or symbol.isdigit():
                self.__buffer += symbol
            else:
                result = list([self.__buffer + ' ' + 'ID'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
        elif self.currentState == States.INT:
            if symbol.isdigit():
                self.__buffer += symbol
            elif symbol == '.':
                self.__buffer += symbol
                self.currentState = States.FLOAT
            else:
                result = list([self.__buffer + ' ' + 'INTEGER'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
        elif self.currentState == States.FLOAT: # ! допилить числа с плавающей точкой
            if symbol.isdigit():
                self.__buffer += symbol
            else:
                result = list([self.__buffer + ' ' + 'FLOAT'])
                self.currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result