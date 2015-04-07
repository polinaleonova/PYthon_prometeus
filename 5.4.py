__author__ = 'polina'



def file_search(folder, filename):
    path = folder[0] + '/'
    if type(folder) == list:
        for i in folder[1:]:
            print i
            if file_search(i, filename)<>None:
                path = path + file_search(i, filename)
                print path
                return path
            else:
                if i == filename:
                    path = path +i
                    print path + filename
                    return path +filename
                else:
                    print False
                    return False
            # print path + filename
            # return path +filename
    else:
        path = path + filename
        print path



# file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me')
file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '4.txt')
# file_search(['/media',['polina','nefileforprometeus.txt']], 'nefileforprometeus.txt')

