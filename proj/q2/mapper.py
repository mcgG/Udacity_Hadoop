#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) != 19 or not line[0].isdigit():
        continue
    
    node_type = line[5]
    tag_names = line[2]

    if node_type == 'question':
        for tag in tag_names.split(' '):
            print tag
