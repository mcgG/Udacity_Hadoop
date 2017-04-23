#!/usr/bin/python

import sys
import csv

try:
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        author_id, added_at = line[3], line[8]
        if author_id == 'author_id':
            continue
        print '{0}\t{1}'.format(author_id, added_at)
except:
    pass
