#!/usr/bin/python

import sys
import heapq

last_tag = None
total = 0
q = []

for data in sys.stdin:

    if last_tag and last_tag != tag:
        heapq.heappush(q, (-total, last_tag))
        total = 0    

    total += 1
    last_tag = tag

if last_tag is not None:
    heapq.heappush(q, (-total, last_tag))

ans = []
for _ in xrange(10):
    if q:
        node = heapq.heappop(q)
        ans.append((node[1], -node[0]))
for i in ans[::-1]:
    print '{0}\t{1}'.format(i[0], i[1])
