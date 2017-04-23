#!/usr/bin/python

import sys
import csv

try:
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) != 19 or not line[0].isdigit():
            continue
        node_id, body, node_type, abs_parent_id = line[0], line[4], line[5], line[7]
        
        if node_type == 'answer':
            flag = abs_parent_id
        elif node_type == 'question':
            flag = node_id
        else:
            continue
        
        print '{0}\t{1}\t{2}'.format(flag, node_type, len(body))

except:
    pass
