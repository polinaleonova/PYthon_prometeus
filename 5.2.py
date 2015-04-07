__author__ = 'polina'

def counter(a, b):
    list1 = str(b)
    l = set(list1)
    for i in l:
        res=0
        if i.find('5') == -1:
            res+=1
            print 'klkl'
    print res


counter(12345, 56766)

