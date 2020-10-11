from classes.stateMachine import StateMachine


def defineLexemsFromFile(filename = ''):
    file = open(filename, 'r')
    sm = StateMachine()
    for chunk in iter(lambda: file.readline(), ''):
        for symbol in chunk:
            lexems = sm.handleSymbol(symbol)
            if lexems is None:
                continue
            print(lexems)