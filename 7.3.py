__author__ = 'polina'

import math

class SuperStr(str):

    def  is_repeatance(self, s):
        self.s = s
        try:
            if type(s) == str and len(s) > 0 and (len(self))%(len(self.s)) ==0 and len(self)!=0:
                k = (len(self))/(len(self.s))
                return self.s*k == self
        except TypeError:
            return False

    def is_palindrom(self):
        low_reg = self.lower()
        list_string = list(low_reg)
        list_rev_string = list_string[:]
        list_rev_string.reverse()
        return list_rev_string == list_string


s2 = SuperStr('678678678678')
print s2.is_repeatance('678')
# print s.is_repeatance('123123')
# print s.is_repeatance('123123123123')
# print s.is_repeatance('12312')
# print s.is_repeatance(123)
# print s.is_palindrom()
# print s
# print int(s)
# print s + 'qwe'
# p = SuperStr('123_321')
# print p.is_palindrom()
# print p



# proposed:
# class SuperStr(str):
#     def is_repeatance(self, substring):
#         try:
#             if len(substring) == 0 or len(self) == 0:
#                 return False
#             multiplier = len(self) / len(substring)
#             return self == substring * multiplier
#         except TypeError:
#             return False
#
#     def is_palindrom(self):
#         try:
#             return self.lower() == self[::-1].lower()
#         except TypeError:
#             return False