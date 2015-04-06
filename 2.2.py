__author__ = 'polina'

import sys


x = int(sys.argv[1])  # count of la
y = int(sys.argv[2])  # repeat
z = int(sys.argv[3])  # 1 - !   0 - .

la = 'Everybody sing a song:' + ((('la-'*x)[:-1] + ' ')*y)[:-1] + ('.' if z == 0 else '!')
print la



