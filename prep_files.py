#!/usr/bin/env python

import os
import json

def get_rubros_info():
    return {file[:-4].split('_')[0]:os.path.join('data_rubros', file) for file in os.listdir('data_rubros') if file[-4:] == '.csv' }


def write():
    with open('rubros.json', 'w') as file:
        json.dump(get_rubros_info(), file)

if __name__ == '__main__':
    write()
