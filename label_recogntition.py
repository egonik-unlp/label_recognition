# -*- coding: utf-8 -*-
"""label_recogntition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WtyIe12UacDvqvqJX6zQj6Cx5IoIHXfq
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

!pip install --upgrade azure-cognitiveservices-vision-computervision
!pip install fuzzywuzzy python-levenshtein
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from google.colab import files

from fuzzywuzzy import fuzz
import difflib
from difflib import SequenceMatcher
from array import array
import os
import json
import numpy as np
from PIL import Image
import sys
import time
import pandas as pd

subscription_key = '49d43aca83e24104adb3808800ecae7e'
endpoint = 'https://goodvibes.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def fuzzy(word, dataframe):
  ratios = []
  dic = {}
  for ing_words in dataframe.ingrediente.to_list():
    ratio = fuzz.WRatio(word, ing_words)
    ratios.append(ratio)
    dic[ratio] = ing_words
  ratios.sort(reverse = True)
  if ratios[0] > 90:
    print(f'El puntaje más alto para {word} fue {ratios[0]}')
  #print(f'{word} -> {ratios}')
  return dic[ratios[0]]

def read_images(params, computervision_client):
    good_outcome = True
    string_ocr = ''
    try:
        all_words = []
        local_image_printed_text_path = params['image_file']
        local_image_printed_text = open(local_image_printed_text_path, "rb")
        ocr_result_local = computervision_client.recognize_printed_text_in_stream(local_image_printed_text)
        for region in ocr_result_local.regions:
            for line in region.lines:
                #print("Bounding box: {}".format(line.bounding_box))
                s = ""
                for word in line.words:
                    s += word.text + " "
                #print(s)
                all_words += [word.text for word in line.words]
                words_joined = ' '.join(all_words).split(',')
                words_split = [palabra.strip() for palabra in words_joined]
        return words_split
    except Exception as e:
        print(e)
    

   


def matching(params ,words):
    return_array = []
    if params['rubro'] != 'todos':
        df = pd.read_csv(rubros[params[rubro]])
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/egonik-unlp/label_recognition/main/data_rubros/todos.csv')
    print(words[-1])
    for word in words:
        try:
          match = fuzzy(word,df)
          
          print(f'{word} matcheo ingrediente {match}')
          #match = difflib.get_close_matches(word, ' '.join(df['ingrediente'].to_list()))[0]
          #sm = SequenceMatcher(None, word,' '.join(df['ingrediente'].to_list()) )
          #a, b, s = sm.get_close_mar 
          #return_array.append(
          #        {
          #            'matcheo' : df[df['ingrediente'] == match]['info'],
          #            'palabra_ocr' : word
          #        }
          #    )
          return_array = ['hulabaloo']
        except IndexError as e:
              print(f'no matches found for {word}')
    if not return_array:
        r = False 
    else:
        r = return_array
    return r

uploaded = files.upload()

name = list(uploaded.keys())[0]

params = {
    'rubro': 'todos',
    'image_file': name 
}

df = pd.read_csv('https://raw.githubusercontent.com/egonik-unlp/label_recognition/main/data_rubros/todos.csv')


a = read_images(params, computervision_client)
z = matching(params,a )

a

from math import log
print(10 - 3.55*log(100 - 9,5))