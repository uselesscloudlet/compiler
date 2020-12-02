from syntax.settings.symbols import Terminals, NonTerminals
from syntax.settings.parser import Parser
from syntax.table_parser import parse_table
import pprint

lex_file = open('syntax/settings/lexems.csv', 'r')
parser = Parser(lex_file)

ct_file = open('syntax/settings/control_table.csv', 'r')
control_table = parse_table(ct_file)

reducers = []


def pop_n(stack, n):
    for i in range(n):
        stack.pop()


def reduce1(stack):
    if stack == [Terminals.NABLA, NonTerminals.STATS]:
        pop_n(stack, 2)
        print("Great!")
    else:
        raise "Too bad!"


def reduce2(stack):
    if stack[-2:] == [NonTerminals.STATS, NonTerminals.STAT]:
        pop_n(stack, 2)
        stack.append(NonTerminals.STATS)
    elif stack[-1:] == [NonTerminals.STAT]:
        pop_n(stack, 1)
        stack.append(NonTerminals.STATS)
    else:
        raise "Too bad!"


def reduce3(stack):
    if stack[-1:] == [NonTerminals.OR_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.EXP)
    else:
        raise "Too bad!"


def reduce4(stack):
    if stack[-1:] == [NonTerminals.AND_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.EXP)
    else:
        raise "Too bad!"


def reduce5(stack):
    if stack[-3:] == [Terminals.VAR, Terminals.ASSIGNMENT, NonTerminals.EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.ASSIGNMENT_EXP)
    elif stack[-3:] == [NonTerminals.LOG_EXP, Terminals.AND_OPERATOR, NonTerminals.EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.AND_EXP)
    elif stack[-3:] == [NonTerminals.LOG_EXP, Terminals.OR_OPERATOR, NonTerminals.EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.OR_EXP)
    else:
        raise "Too bad!"


def reduce6(stack):
    if stack[-1:] == [NonTerminals.LOG_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.AND_EXP)
    else:
        raise "Too bad!"


def reduce7(stack):
    if stack[-3:] == [NonTerminals.ADDITIVE_EXP, Terminals.COMP_OPERATOR, NonTerminals.ADDITIVE_EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.LOG_EXP)
    elif stack[-1:] == [NonTerminals.ADDITIVE_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.LOG_EXP)
    else:
        raise "Too bad!"


def reduce8(stack):
    if stack[-3:] == [NonTerminals.ADDITIVE_EXP, Terminals.PM_OPERATOR, NonTerminals.MULT_EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.ADDITIVE_EXP)
    elif stack[-1:] == [NonTerminals.MULT_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.ADDITIVE_EXP)
    else:
        raise "Too bad!"


def reduce9(stack):
    if stack[-4:] == [Terminals.OPEN_PAR, Terminals.TYPE_NAME, Terminals.CLOSE_PAR, NonTerminals.CAST_EXP]:
        pop_n(stack, 4)
        stack.append(NonTerminals.CAST_EXP)
    elif stack[-3:] == [NonTerminals.MULT_EXP, Terminals.MD_OPERATOR, NonTerminals.CAST_EXP]:
        pop_n(stack, 3)
        stack.append(NonTerminals.MULT_EXP)
    elif stack[-2:] == [Terminals.UNARY_OPERATOR, NonTerminals.CAST_EXP]:
        pop_n(stack, 2)
        stack.append(NonTerminals.UNARY_EXP)
    elif stack[-1:] == [NonTerminals.CAST_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.MULT_EXP)
    else:
        raise "Too bad!"


def reduce10(stack):
    if stack[-2:] == [Terminals.PPFIX_OPERATOR, NonTerminals.UNARY_EXP]:
        pop_n(stack, 2)
        stack.append(NonTerminals.UNARY_EXP)
    elif stack[-1:] == [NonTerminals.UNARY_EXP]:
        pop_n(stack, 1)
        stack.append(NonTerminals.CAST_EXP)
    else:
        raise "Too bad!"


def reduce11(stack):
    if stack[-2:] == [NonTerminals.ASSIGNMENT_EXP, Terminals.SEMICOLON]:
        pop_n(stack, 2)
        stack.append(NonTerminals.STAT)
    else:
        raise "Too bad!"


def reduce12(stack):
    if stack[-3:] == [Terminals.OPEN_CURBR, NonTerminals.STATS, Terminals.CLOSE_CURBR]:
        pop_n(stack, 3)
        stack.append(NonTerminals.STAT)
    else:
        raise "Too bad!"


def reduce13(stack):
    if stack[-1:] == [Terminals.VAR]:
        pop_n(stack, 1)
        stack.append(NonTerminals.UNARY_EXP)
    else:
        raise "Too bad!"


def reduce14(stack):
    if stack[-1:] == [Terminals.CONST]:
        pop_n(stack, 1)
        stack.append(NonTerminals.UNARY_EXP)
    else:
        raise "Too bad!"


buff = [Terminals.NABLA]

lexem = parser.next_lexem()

while len(buff) > 0:
    if (lexem.term not in control_table) or (buff[-1] not in control_table[lexem.term]):
        raise "Too bad!"
    action = control_table[lexem.term][buff[-1]]

    if action == 'shift':
        buff.append(lexem.term)
        lexem = parser.next_lexem()
    elif action == 'reduce':
        if buff[-1] == NonTerminals.STATS:
            reduce1(buff)
        elif buff[-1] == NonTerminals.STAT:
            reduce2(buff)
        elif buff[-1] == NonTerminals.OR_EXP:
            reduce3(buff)
        elif buff[-1] == NonTerminals.AND_EXP:
            reduce4(buff)
        elif buff[-1] == NonTerminals.EXP:
            reduce5(buff)
        elif buff[-1] == NonTerminals.LOG_EXP:
            reduce6(buff)
        elif buff[-1] == NonTerminals.ADDITIVE_EXP:
            reduce7(buff)
        elif buff[-1] == NonTerminals.MULT_EXP:
            reduce8(buff)
        elif buff[-1] == NonTerminals.CAST_EXP:
            reduce9(buff)
        elif buff[-1] == NonTerminals.UNARY_EXP:
            reduce10(buff)
        elif buff[-1] == Terminals.SEMICOLON:
            reduce11(buff)
        elif buff[-1] == Terminals.CLOSE_CURBR:
            reduce12(buff)
        elif buff[-1] == Terminals.VAR:
            reduce13(buff)
        elif buff[-1] == Terminals.CONST:
            reduce14(buff)
        else:
            print("WTF")

    else:
        print("Too bad!")
