
!pip install --upgrade azure-cognitiveservices-vision-computervision
!pip install fuzzywuzzy python-levenshtein
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


from matching import make_json
from fuzzywuzzy import fuzz
# import difflib
# from difflib import SequenceMatcher
from array import array
import os
import json
import numpy as np
# from PIL import Image
import sys
import time
import pandas as pd

subscription_key = '49d43aca83e24104adb3808800ecae7e'
endpoint = 'https://goodvibes.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


class Azure:
    subscription_key = '49d43aca83e24104adb3808800ecae7e'
    endpoint = 'https://goodvibes.cognitiveservices.azure.com/'

    def __init__(self):
        self.computervision_client =  ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    def read_images(self, params):
        good_outcome = True
        string_ocr = ''
        try:
            all_words = []
            local_image_printed_text_path = params['image_file']
            local_image_printed_text = open(local_image_printed_text_path, "rb")
            ocr_result_local = self.computervision_client.recognize_printed_text_in_stream(local_image_printed_text)
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
        