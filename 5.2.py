__author__ = 'polina'


def counter(a, b):
    str_a = str(a)
    list_b = str(list(set(str(b))))
    list_res = []
    for i in str_a :
        if list_b.find(i) != -1:
            list_res.append(i)
    return len(set(list_res))


#
# counter(98123560, 79266)


#
# proposed version


# def counter(a, b):
#     num = 0
#     a_str = str(a)
#     b_str = str(b)
#     found = ''
#     for char_b in b_str:
#         if a_str.find(char_b) != -1 and found.find(char_b) == -1:
#             num = num + 1
#             found = found + char_b
#     return num