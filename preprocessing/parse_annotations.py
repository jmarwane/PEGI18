#!/usr/bin/python3.6

import re
import json
import sys


# filename = 'annotations.txt'
# output   = 'currated.json'

filename = sys.argv[1]
output = sys.argv[2]

file = open(filename, "r")
data = []

current = {'sequences': []}

for line in file:
    if re.match(r'^\[INFO\]', line):   # Beginning match [INFO]
        current['end'] = re.search(r'^\[INFO\](.*) -', line).group(1)
        data.append(current)
        current = {'sequences': []}
        continue

    if not re.match(r'^\[F\]', line): # Beginning match [F]
        current['name'] = line
        continue

    beginning = re.search(r'^\[F\](.*) - Start', line).group(1)
    end       = re.search(r'\|\[F\](.*) - Stop', line).group(1)

    current['sequences'].append({'beginning': beginning, 'end': end})

file.close()

with open(output, 'w') as file:
    json.dump(data, file)
