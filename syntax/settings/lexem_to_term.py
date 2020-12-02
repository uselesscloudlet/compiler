def map_lexem_to_term(lexem):
    if (lexem.cl == ''):
        return "eof"
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value == '||'):
        return "||"
    elif (lexem.cl == 'States.OPERATOR' and
            lexem.value == '&&'):
        return "&&"
    elif (lexem.cl == 'States.COMPRASION'):
        return "comp_operator"
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['+', '-']):
        return "pm_operator"
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['*', '/', '%']):
        return "md_operator"
    elif (lexem.cl == 'States.PPFIX'):
        return "prefix_operator"
    elif (lexem.cl == 'States.OPERATOR' and
          lexem.value in ['~', '!']):
        return "unary_operator"
    elif (lexem.cl == 'States.ID'):
        return "var"
    elif (lexem.cl == 'States.KEYWORD' and
          lexem.value in ['int', 'float', 'char', 'string', 'double', 'short']):
        return "type_name"
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '('):
        return "("
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == ')'):
        return ")"
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '{'):
        return "{"
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == '}'):
        return "}"
    elif (lexem.cl == 'States.DELIM' and
          lexem.value == ';'):
        return ";"
    elif (lexem.cl == 'States.ASSIGNMENT'):
        return "="
    elif (lexem.cl in ['States.INT', 'States.FLOAT', 'States.CHAR', 'States.STRING']):
        return "const"
    elif (lexem.cl == "States.SCOMMENT"):
        return "COMMENT"
    else:
        print('Alert!')
        print(lexem.cl)
        print(lexem.value)
