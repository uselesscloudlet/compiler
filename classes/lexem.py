class Lexem:
    __slots__ = ['__line', '__cl', '__value', '__attributes']

    def __init__(self, cl, value, attributes = None):
        self.__line = None
        self.__cl = cl
        self.__value = value
        self.__attributes = attributes


    def __repr__(self):
        return "{},{},{},{}".format(self.__line, self.__cl, self.__value, self.__attributes)


    @property
    def line(self):
        return self.__line


    @line.setter
    def line(self, number):
        self.__line = number

    
    @property
    def cl(self):
        return self.__cl


    @property
    def value(self):
        return self.__value


    @property
    def attributes(self):
        return self.__attributes