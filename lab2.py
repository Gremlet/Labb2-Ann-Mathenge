import numpy as np
import math
import re

data_path = './data/datapoints.txt'
test_path = './data/testpoints.txt'

def read_datapoints(filepath):
    datapoints = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('('): 
                continue
            width, height, label = map(float, line.split(','))
            # convert the label value to an int because has to be 1 or 0 not 1.0 and 0.0.
            # and add width, height and label tuples to the datapoints list
            datapoints.append((width, height, int(label))) 
    return datapoints

def read_testpoints(filepath):
    testpoints = []
    list_number_pattern = re.compile(r'^\d+\.\s*') # start of line, digits, dots and whitespace
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('Test'):
                continue
            line = list_number_pattern.sub('', line) # substitute 1. 2. etc with empty string
            line = line.replace('(', '').replace(')', '')
            width, height = map(float, line.split(','))
            testpoints.append((width, height))
    return testpoints

