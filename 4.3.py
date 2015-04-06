__author__ = 'polina'

import sys

a = sys.argv[1:]
d = ''
k = d.join(a)
t = list(k)
res = 0
for i in t:
    if res<0:
        break
    if i == '(':
        res = res+1
    else:
        res=res-1
if res==0:
    print 'YES'
else:
    print "NO"




