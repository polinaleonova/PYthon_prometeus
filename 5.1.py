# import json
w=[1,1.0,'1',-1,1]
# print dir(w)
def clean_list(w):
    list2 = list({x for x in w})
    print list2
    #
    # [di.update({x: None}) for x in w]
    # l = di.keys()
    # l.sort()
    # return l

clean_list(w)










# print json.dumps([1]) == json.dumps(clean_list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# print json.dumps([0, 'q', 'qq', 'qqq', 'qqqq']) == json.dumps(clean_list([0, 'q', 'qq', 'qqq', 'qqq', 'qqq', 'qqqq', 0, 'qqq']))
# print json.dumps(['asd', 'dsa', 1, '1', 1.0]) == json.dumps(clean_list(['asd', 'dsa', 1, '1', 1.0]))
# print clean_list(['asd', 'dsa', 1, '1', 1.0])
# print [1, '1', 'asd', 'dsa']