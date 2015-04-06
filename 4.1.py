__author__ = 'polina'

import sys

a = sys.argv[1:]
if type(a) == list:
    print '!!'
s = ''
string = s.join(a).lower()
list1 = list(string)
list2 = list(string)
list2.reverse()
if list1 == list2:
    print 'YES'
else:
    print 'NO'

print list1, list2
print a

