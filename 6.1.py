__author__ = 'polina'

def count_holes(n):
    if type(n) == int or (type(n) == str and n.isdigit()) or type(n) == long:
        n_str = str(n)
        res = 0
        dic ={'-':0, '1': 0, '2':0, '3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1,'0':1}
        if type(n) == str:
            withoutzerro = n_str.lstrip('0')
        else:
            withoutzerro = n_str
        for i in withoutzerro:
            if dic[i]!='0':
                res+=dic[i]
        print res
        return res
    else:
        return 'ERROR'



count_holes(1)