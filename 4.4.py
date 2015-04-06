__author__ = 'polina'

import sys

a = sys.argv[1]
b = sys.argv[2]

res = 0
for i in range(int(a), int(b)+1):
    i = str(i)
    k = i.zfill(6)
    n = 0
    v = 0
    for l in k[:3]:
        n += int(l)
    for m in k[3:]:
        v += int(m)
    if n == v:
        res+=1
print res





