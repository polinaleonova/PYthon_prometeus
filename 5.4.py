__author__ = 'polina'

import os
import glob

#
folder  = ['media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning']
filename = 'nefileforprometeus.txt'
# a = sys.argv[1:]
# print folder, filename

# cwd = os.getcwd()
# print cwd
# print os.path.exists('/media/polina/8802ebf9-bb70-49ed-923d-a92083b73b2d/learning/nefileforprometeus.txt')

def file_search(folder, filename):
    print folder
    desc = '/'
    path1 = desc.join(folder)
    path2 = '/'+path1+ '/'
    print path2
    print os.path.exists(path2)
    names = glob.glob('c:\home\*.txt')

    os.listdir(path1)
    if os.path.exists('nefileforprometeus.txt'):
        print path1
    else:
        print  False



# ['polina@polina-comp:','media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning','nefileforprometeus.txt']


file_search(['media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning'], 'nefileforprometeus.txt')
# polina@polina-comp:/home/polina/PycharmProjects/prometeus/1.py

# ['polina@polina-comp:','media','polina','8802ebf9-bb70-49ed-923d-a92083b73b2d','learning','nefileforprometeus.txt'
