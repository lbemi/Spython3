# print('两数和')
# a = float(input('输入数字A:'))
# b = float(input('输入数字B:'))
# print('A + B = %0.3f'%(a+b))

# import cmath
# num = int(input('请输入一个整数：'))
# num_sqrt = cmath.sqrt(num)
# print('{0} 的平方根为：{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real , num_sqrt.imag))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}\t'.format(i,j,i*j),end='')
#     print()

# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
# # 测试字符串和数字
# print(is_number('foo'))   # False
# print(is_number('1'))     # True
# print(is_number('1.3'))   # True
# print(is_number('-1.37')) # True
# print(is_number('1e3'))   # True
#
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四')) # True
# # 版权号
# print(is_number('©'))  # False
# import calendar
# yy = int(input('输入年份:'))
# mm = int(input('输入月份：'))
# print(calendar.month(yy, mm))
# with open('foo.txt','wt') as  out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
# import datetime
# def getYes():
#     t = datetime.date.today()
#     o = datetime.timedelta(days=2)
#     y = t - o
#     print(t)
#     print(o)
#
#     return y
# print(getYes())


li = [1, 9, 8, 4]

for elem in li:
    print(elem*2)