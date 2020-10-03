"""harvard access case"""
import os
import sys
sys.path.append('..')

import pandas as pd
import matplotlib.pyplot as plt
import lzma
import json
import urllib.request
import shutil

#from config import settings
#import utils

#%matplotlib inline


#compressed_file = utils.get_and_extract_from_bulk(jurisdiction="Illinois", data_format="json")


#a list to hold the cases we're sampling
cases = []

#decompress the file line by line

with lzma.open("ill_text/data/data.jsonl.xz") as infile:
    for line in infile:
        #decode the file into a convenient format
        record = json.loads(str(line, 'utf-8'))
        #if the decision date on the case matches one we're interested in, add to our list
        cases.append(record)

        #print(record['casebody']['data']['opinions'][0]['author'])
#print(cases[0]['text'])


#print("Number of Cases: {}".format(len(cases)))

for case in cases:
    author = case['casebody']['data']['opinions'][0]['author']
    if 'Barnes' in author or "Jett" in author:
        print(case['casebody']['data']['opinions'][0]['text'])
