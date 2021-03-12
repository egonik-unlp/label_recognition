#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from difflib import SequenceMatcher
from array import array
import os
import json
import numpy as np
from PIL import Image
import sys
import time


subscription_key = '49d43aca83e24104adb3808800ecae7e'
endpoint = 'https://goodvibes.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))




rubros = {
    file 1:pathfile1,
    file 1:pathfile1
}




params = {
    'image_file': file
    'rubro': rubro
}



def read_images(params, computervision_client):
    good_outcome = True
    string_ocr = ''
    try:
        local_image_printed_text_path = params['image_file']
        local_image_printed_text = open(local_image_printed_text_path, "rb")

        ocr_result_local = computervision_client.recognize_printed_text_in_stream(local_image_printed_text)
        for region in ocr_result_local.regions:
            for line in region.lines:
                #print("Bounding box: {}".format(line.bounding_box))
                s = ""
                for word in line.words:
                    s += word.text + " "
                print(s)
                return line.words 
    except Exception as e:
        print('problema con el reconocimiento de la imagen')


def matching(params, words):
    return_array = []
    for word in words:
        matchear[json]
        if matcheo:
            return_array.append(
                {
                    ingrediente: infotoreport
                }
            )
    if not return_array:
        r = 'No reconoci nada'
    else:
        r = return_array
    return r





