__author__ = 'polina'

# import ipdb
#
# ipdb.set_trace()

def file_search(folder, filename):
    res = []
    for i in folder[1:]:
        if isinstance(i, str):
            k = folder[0] + '/' + i
            res.append(k)
        # print res
        else:
            if file_search(i, filename) <> None:
                k = folder[0]+ '/' + file_search(i, filename)
                res.append(k)
            else:
                k = folder[0]+ '/' +'ioioio'
                res.append(k)
    print res
    for n in res:
        if n.find(filename) != -1:
            # print n
            return n
        else:
            print 'iiio'
            return False






file_search(['/media',['polina','learning','nefileforprometeus.txt']], 'nefileforprometeus.txt')



# def file_search(folder, filename):
#     res = []
#     for i in folder[1:]:
#         if isinstance(i, str):
#             k = folder[0] + '/' + i
#             res.append(k)
#         # print res
#         else:
#             print 'fdf'
#     for n in res:
#         if n.find(filename) != -1:
#             print n
            # return n