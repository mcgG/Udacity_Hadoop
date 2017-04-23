#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) != 19 or not line[0].isdigit():
        continue

    node_id, author_id, node_type, abs_parent_id = line[0], line[3], line[5], line[7]

    if node_type == 'question':
        flag = node_id
    else:
        flag = abs_parent_id
    print '{0}\t{1}'.format(flag, author_id)


