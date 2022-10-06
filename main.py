# import os
# from re import A 
# import calculator
# res=calculator.add(2,3)
# res1=calculator.div(6,2)
# print(res)
# print(int(res1))
# print(dir(calculator))
# current_dir=os.getcwd()
# print(current_dir)
# print(os.listdir())
# os.remove("/mnt/d/text")
# #os.mkdir("Exception_handling.py")
# num=[1,-2,'s',4]
# print(type(num))
# print(dir(num))
# c=3
# from decimal import Decimal as d
# print(c*d('3.3'))
# x=d('1.1')
# c=x+d('2.2')
# print(type(x))
# from fractions import Fraction as f
# print(f(1.5)) 
# print (f(1,3))
# print(f("1.1"))
# import math
# print(dir(math))
# # #f = open("calclator.py")   
# with  open("/mnt/d/text/text1.txt",'w',encoding='utf-8') as f:
#     #   f.write("\nI am a Doc\n")
#     #   f.write("i luv my sis\n")
#     f.writelines("bye")
#     #   c=(f.readline())
#     #   c=(f.readline())
#     #   c=(f.readline())
#     # print(c)
# #       co1=f.tell()
# #       print(co1)
# # #f.close()
a=(1,2,3)
print(a)
print(id(a))
b=(4,5,6)
print(a+b)
print(a)
a=[1,2,3]
b=a
a.append([5,6])
print(a)
print(b)
print(id(a))
print(id(b))
print(13//2)
print(13.8//2)
from fractions import Fraction as F
x=F(1,2)
x*2
print(x)
def is_it_true(anything): 
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")
is_it_true([False])
a_list = ['a']
a_list = a_list + [2, 'a']
a_list.extend((2,3,4))
print(a_list)
print(list([2,3,4]))
print(a_list.remove(2))
print(a_list.clear())
