# import re
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# import random
# print(random.choice(['apple', 'pear', 'banana']))
#
# print(random.sample(range(100), 10))
#
# from urllib.request import urlopen
# for line in  urlopen('http://www.baidu.com'):
#     line = line.decode('utf-8')
#     if '新闻' in line or 'EDT' in line:
#         print(line)
# from datetime import date
# print(date.today())
#
# import zlib
# s = b'qqqq1321313132'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# from timeit import  Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests