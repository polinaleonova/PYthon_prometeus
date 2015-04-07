__author__ = 'polina'

import os


# folder  = ['C:', 'backup.log', 'ideas.txt']
# filename = 'ideas.txt'
# a = sys.argv[1:]
# print folder, filename

cwd = os.getcwd()
print cwd
print os.path.exists('/media/polina/8802ebf9-bb70-49ed-923d-a92083b73b2d/learning/nefileforprometeus.txt')

# def file_search(folder, filename):
#     desc = '/'
#     path1 = desc.join(folder)
#     print path1
#     print os.path.exists(path1)
#     os.listdir(path1)
#     if os.path.exists('nefileforprometeus.txt'):
#         print path1
#         return path1
#     else:
#         print  False
#         return False


# ['polina@polina-comp:','media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning','nefileforprometeus.txt']


# file_search(['polina@polina-comp:','media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning','nefileforprometeus.txt'], 'nefileforprometeus.txt')
# polina@polina-comp:/home/polina/PycharmProjects/prometeus/1.py

# ['polina@polina-comp:','home', 'polina', 'PycharmProjects', 'prometeus', '1.py']