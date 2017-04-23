#!/usr/bin/python

import sys

last_id = None
len_post = 0
len_ans = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 3:
        continue
    curr_id, node_type, body_len = data
    if last_id and last_id != curr_id:
        print '{0}\t{1}\t{2}'.format(last_id, len_post, len_ans)
        len_post = len_ans = 0

    if node_type == 'question':
        len_post += int(body_len)
    elif node_type == 'answer':
        len_ans += int(body_len)
    last_id = curr_id

if last_id is not None:
    if node_type == 'question':
        len_post += int(body_len)
    elif node_type == 'answer':
        len_ans += int(body_len)
    print '{0}\t{1}\t{2}'.format(last_id, len_post, len_ans)

