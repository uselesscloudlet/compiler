from classes.definitions import Terminals, NonTerminals, States

term_map = {
    ';': Terminals.SEMICOLON,
    '{': Terminals.OPEN_CURBR,
    '}': Terminals.CLOSE_CURBR,
    'var': Terminals.VAR,
    '=': Terminals.ASSIGNMENT,
    'log_operator': Terminals.LOG_OPERATOR,
    'comp_operator': Terminals.COMP_OPERATOR,
    'pm_operator': Terminals.PM_OPERATOR,
    'md_operator': Terminals.MD_OPERATOR,
    '(': Terminals.OPEN_PAR,
    'type_name': Terminals.TYPE_NAME,
    ')': Terminals.CLOSE_PAR,
    'const': Terminals.CONST,
    'prefix_operator': Terminals.PPFIX_OPERATOR,
    'unary_operator': Terminals.UNARY_OPERATOR,
    '-|': Terminals.END_SYMBOL
}

nonterm_map = {
    'STATS': NonTerminals.STATS,
    'STAT': NonTerminals.STAT,
    'ASSIGNMENT_EXP': NonTerminals.ASSIGNMENT_EXP,
    'EXPRESSION': NonTerminals.EXPRESSION,
    'LOG_EXP': NonTerminals.LOG_EXP,
    'ADDITIVE_EXP': NonTerminals.ADDITIVE_EXP,
    'MULT_EXP': NonTerminals.MULT_EXP,
    'CAST_EXP': NonTerminals.CAST_EXP,
    'UNARY_EXP': NonTerminals.UNARY_EXP
}


def map_lexem_to_term(lexem):
    if (lexem.cl == ''):
        return Terminals.END_SYMBOL
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['&&', '||']):
        return Terminals.LOG_OPERATOR
    elif (lexem.cl == 'States.COMPRASION'):
        return Terminals.COMP_OPERATOR
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['+', '-']):
        return Terminals.PM_OPERATOR
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['*', '/', '%']):
        return Terminals.MD_OPERATOR
    elif (lexem.cl == 'States.PPFIX'):
        return Terminals.PPFIX_OPERATOR
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['~', '!']):
        return Terminals.UNARY_OPERATOR
    elif (lexem.cl == 'States.ID'):
        return Terminals.VAR
    elif (lexem.cl == 'States.KEYWORD' and
          lexem.value in ['int', 'float', 'char', 'string', 'double', 'short']):
        return Terminals.TYPE_NAME
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '('):
        return Terminals.OPEN_PAR
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == ')'):
        return Terminals.CLOSE_PAR
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '{'):
        return Terminals.OPEN_CURBR
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '}'):
        return Terminals.CLOSE_CURBR
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == ';'):
        return Terminals.SEMICOLON
    elif (lexem.cl == 'States.ASSIGNMENT'):
        return Terminals.ASSIGNMENT
    elif (lexem.cl in ['States.INT', 'States.FLOAT', 'States.CHAR', 'States.STRING']):
        return Terminals.CONST
    else:
        print('Alert!')
        print(lexem.cl)
        print(lexem.value)
