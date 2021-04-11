import numpy as np 
import pandas as pd
from fuzzywuzzy import fuzz


def fuzzzy():
    return fuzz.WRatio(x,y)

def match_matrix(nombres, ingredientes):
    for i,x in enumerate(nombres):
        maximum = 0
        for y in enumerate(ingredientes):
            array[i][j] = fuzzy(x,y)
            if array[i][j] > maximum:
                maximum = y, 100 - array[i][j]
        maxima.append(maximum)
    return maxima, len(nombres)


def make_json(nombres, ingredientes):
    reconocidos, meta = match_matrix(nombres, ingredientes)
    return {
        'metadata':{
            'number of ingredients': meta
        },
        'ingredientes': reconocidos

    }