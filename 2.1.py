__author__ = 'polina'

import sys
import math


def f(a, b, c):
    res = float(1/(c*math.sqrt(2*math.pi)))*math.exp(-(((a-b)**2)/(2*(c**2))))
    print res

f(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
#commit test
