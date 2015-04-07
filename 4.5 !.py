__author__ = 'polina'

import sys

a = sys.argv[1:]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
desc = ''
listkey = list(key)
listalp = list(alphabet)
listDval = []
s = desc.join(a)
s1 = []
for j in s:
    if j.islower() is True:
        j = 'a'
    else:
        j = 'b'
    s2 = s1.append(j)
listab = []
five = ''
for i in s1:
    five += i
    if len(five) == 5:
        listab.append(five)
        five = ''
for n in range(len(listkey)+1):
    if len(listkey) > 5:
        n = desc.join(listkey[:5])
        listDval.append(n)
        del listkey[0]
D = dict(zip(listDval, listalp))
res = ''
for i in listab:
    res += D[i]
print res
# file needed some revision - has not worked one test? with '[' and ']'






