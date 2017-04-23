#!/usr/bin/python

import sys

active_hours = [0] * 24
last_author_id = None

try:
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        author_id, added_at = data
    
        if last_author_id and last_author_id != author_id:
            print '{0}\t{1}'.format(author_id, active_hours.index(max(active_hours)))
            active_hours = [0] * 24
        active_hour = int(added_at.split(' ')[1][:2])
        active_hours[active_hour] += 1
        last_author_id = author_id
    
    if last_author_id:
        print '{0}\t{1}'.format(author_id, active_hours.index(max(active_hours)))
except:
    pass
