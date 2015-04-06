__author__ = 'polina'

import sys
import math


a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

print a, b, c
if a <= 0 or b <= 0 or c <= 0:
    print 'not triangle'

else:
    w = math.acos((a**2+b**2-c**2)/(2*a*b))
    if w >= math.pi or w ==0 :
        print 'not triangle'
    else:
        print 'triangle'
