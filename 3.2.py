__author__ = 'polina'

import sys


def fib(a):
    list =[0, 1]
    if a==0:
        print list[0]
    else:
        for i in range(a-1):
            list.append(list[0]+list[1])
            list.pop(0)
        print list[1]

a = int(sys.argv[1])
if type(a) is not int:
    print 'Enter only integer'
else:
    fib(a)





