#!/usr/bin/python

import sys

last_node_id = None
students = []

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    node_id, author_id = data

    if last_node_id and last_node_id != node_id:
        print '{0}\t{1}'.format(last_node_id, students)
        students = []

    students.append(author_id)
    last_node_id = node_id

if last_node_id is not None:
    print '{0}\t{1}'.format(last_node_id, students)
