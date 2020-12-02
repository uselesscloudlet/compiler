from classes.stateMachine import StateMachine
from classes.parser import Parser
from classes.definitions import NonTerminals, Terminals
from tableParser import parseTable

def defineLexemsFromFile(filename = ''):
    file = open('tests/' + filename, 'r')
    sm = StateMachine()
    allLex = []
    for index, chunk in enumerate(iter(lambda: file.readline(), '')):
        for symbol in chunk:
            lexems = sm.handleSymbol(symbol)
            if lexems is None:
                continue
            for lexem in lexems:
                lexem.line = index + 1
            allLex += lexems
            
    lexems = sm.handleSymbol('\n')
    if lexems is not None:
        for lexem in lexems:
            lexem.line = index + 1
        allLex += lexems

    f = open('attachment/result.csv', 'w')
    f.write('line,type,value,attribute\n')
    f.write("\n".join(map(str, allLex)))
    f.close()
    parser = Parser(allLex)
    lex = parser.next_lexem()
    while lex != Terminals.END_SYMBOL:
        print(lex)
        lex = parser.next_lexem()

    tablef = open('attachment/control_table.csv')
    parseTable(tablef)
    tablef.close()
    #print("\n".join(map(str, allLex)))