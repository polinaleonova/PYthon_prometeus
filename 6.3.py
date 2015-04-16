__author__ = 'polina'

def saddle_point(matrix_list):
    d = {}
    a = []
    print a
    b = []
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[0])):
            d[matrix_list[i][j]] = (i, j)
            a.append(j)

    b = d.items()
    # for n in d.values():
    #     if


    print a






saddle_point([[1,2,3],[0,4,6]])