__author__ = 'polina'
import os
# import ipdb
#
# ipdb.set_trace()


def create_search_list(root, folders, required_key, result={'response': False}):
    for i in folders:
        if type(i) == str:
            if i == required_key:
                result['response'] = os.path.join(root, i)
                return os.path.join(root, i)
        else:
            create_search_list(os.path.join(root, i[0]), i[1:], required_key, result)
    return result['response']


def file_search(folder, filename):
    return create_search_list(folder[0], folder[1:], filename)




# file_search(['/media',['polina','learning','nefileforprometeus.txt']], 'nefileforprometeus.txt')



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

def copy_file_search(folder, filename):
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
