import numpy as np 
import pandas as pd
from fuzzywuzzy import fuzz


def fuzzy(x,y):
    return fuzz.WRatio(x,y)

def match_matrix(nombres, ingredientes):
    maxima = []
    array = np.array(shape = (len(nombres),len(ingredientes)))
    for i,x in enumerate(nombres):
        maximum = {
            'value': 0
        }
        for j,y in enumerate(ingredientes):
            array[i][j] = fuzzy(x,y)
            if array[i][j] > maximum['value']:
                maximum = {
                    'value': array[i][j],
                    'ingredient': y
                }
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