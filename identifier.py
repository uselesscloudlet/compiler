from classes.stateMachine import StateMachine


def defineLexemsFromFile(filename = ''):
    file = open('tests/' + filename, 'r')
    sm = StateMachine()
    for index, chunk in enumerate(iter(lambda: file.readline(), '')):
        print('СТРОКА ' + str(index + 1), chunk)
        for symbol in chunk:
            lexems = sm.handleSymbol(symbol)
            if lexems is None:
                continue
            print(lexems)
    lexems = sm.handleSymbol('\n')
    if lexems is None:
        return
    print(lexems)