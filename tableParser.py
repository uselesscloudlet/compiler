from classes.definitions import Terminals, NonTerminals
from syntax_settings import term_map, nonterm_map
import pandas as pd

symb_map = term_map.copy()
symb_map.update(nonterm_map)


def parseTable(file):
    df = pd.read_csv(file)
    result = {}
    col_symb = None
    row_symb = None
    for i, col in enumerate(df):
        if i == 0:
            continue
        col_symb = symb_map[col]
        result[col_symb] = {}
        for j, e in enumerate(df[col]):
            if j == 0:
                row_symb = symb_map[df.iloc[i, 0]]
                continue
            if pd.notna(e):
                if j - 1 < len(NonTerminals):
                    result[col_symb][row_symb] = e
                else:
                    result[col_symb][row_symb] = e
    print(result)
    return result
