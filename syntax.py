from classes.definitions import Terminals, NonTerminals, States
from classes.parser import Parser
from tableParser import parseTable

lex_file = open('attachment/result.csv', 'r')
parser = Parser(lex_file)

lexem = parser.next_lexem()
while lexem.term != Terminals.END_SYMBOL:
    lexem = parser.next_lexem()
