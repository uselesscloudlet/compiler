from classes.definitions import Terminals, NonTerminals
import pandas as pd


def parseTable(file):
    df = pd.read_csv(file)
    result = {}
    for i, col in enumerate(df):
        if i == 0:
            continue
        result[Terminals(i - 1)] = {}
        for j, e in enumerate(df[col]):
            if j == 0:
                continue
            if pd.notna(e):
                if j - 1 < len(NonTerminals):
                    result[Terminals(i - 1)][NonTerminals(j - 1)] = e
                else:
                    result[Terminals(i - 1)][Terminals(j - len(NonTerminals) - 1)] = e
    return result