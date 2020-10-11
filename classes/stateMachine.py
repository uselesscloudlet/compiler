from classes.states import States

class StateMachine:
    def __init__(self):
        self.__currentState = States.IDLE
        self.__buffer = None


    def handleSymbol(self, symbol):
        if self.__currentState == States.IDLE:
            if symbol.isdigit():
                self.__buffer = symbol
                self.__currentState = States.INT
            elif symbol.isalpha():
                self.__buffer = symbol
                self.__currentState = States.ID
            elif symbol.isspace():
                pass
            else:
                return [symbol + " error"]
        elif self.__currentState == States.INT:
            if symbol.isdigit():
                self.__buffer += symbol
            else:
                result = list([self.__buffer + ' ' + 'INTEGER'])
                self.__currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result
        elif self.__currentState == States.ID:
            if symbol.isalpha() or symbol.isdigit():
                self.__buffer += symbol
            else:
                result = list([self.__buffer + ' ' + 'ID'])
                self.__currentState = States.IDLE
                nextLex = self.handleSymbol(symbol)
                if nextLex is not None:
                    result += nextLex
                return result