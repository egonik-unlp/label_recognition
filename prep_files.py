#!/usr/bin/env python

import os
import pandas as pd 
import json

def get_rubros_info():
    return {file[:-4].split('_')[0]:os.path.join('data_rubros', file) for file in os.listdir('data_rubros') if file[-4:] == '.csv' }


def write():
    with open('rubros.json', 'w') as file:
        json.dump(get_rubros_info(), file)

def todos_rubros():
    os.chdir('data_rubros')
    pd.concat([pd.read_csv(file) for file in os.listdir() if file[-4:] == '.csv' and 'todos' not in file]).drop_duplicates().to_csv('todos.csv')
    
if __name__ == '__main__':
    write()
    todos_rubros()
