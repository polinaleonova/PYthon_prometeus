__author__ = 'polina'

def find_most_frequent(text):
    t = text.replace(",", " ").replace(".", " ").replace(":", " ").replace(";", " ").replace("!", " ").replace("?", " ").replace("-", " ").lower()
    s = t.split(" ")
    s_res=[]
    for element in s:
        if element!= '':
            s_res.append(element)
    d = dict([(i, 0) for i in s_res])
    for j in s_res:
        d[j] += 1
    print d
    res = []
    for (x, y) in d.items():
        if y == max(d.values()):
            res.append(x)
    return res



find_most_frequent('to understand recursion you need first to understand recursion...')



# proposed version
# def find_most_frequent(text):
#     if text == '':
#         return []
#     text_list = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').lower().split()
#     counts = dict()
#     word = ''
#     for word in text_list:
#         if word in counts:
#             counts[word] = counts[word] + 1
#         else:
#             counts[word] = 1
#     max_word = [word]
#     for word in counts:
#         if counts[word] > counts[max_word[0]]:
#             max_word = [word]
#         elif counts[word] == counts[max_word[0]] and word != max_word[0]:
#             max_word.append(word)
#     return max_word