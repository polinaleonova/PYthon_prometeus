__author__ = 'polina'

import sys
import math
print dir(math)

a = float(sys.argv[1])
b = float(sys.argv[2])
if a < 0 or b < 0 and b != 0:
    print "Enter only positive numbers.The second number must be don't equile 0"

else:
    x = float((math.sqrt(a*b)/((math.e**a)*b))+a*math.e**(2*a/b))
    print x

 print 2*3%2.0