import os 
import calculator
res=calculator.add(2,3)
res1=calculator.div(6,2)
print(res)
print(int(res1))
print(dir(calculator))
current_dir=os.getcwd()
print(current_dir)
print(os.listdir())
#os.mkdir("Exception_handling.py")
num=[1,-2,'s',4]
print(type(num))
print(dir(num))
c=3
from decimal import Decimal as d
print(c*d('3.3'))
x=d('1.1')
c=x+d('2.2')
print(type(x))
from fractions import Fraction as f
print(f(1.5)) 
print (f(1,3))
print(f("1.1"))
import math
print(dir(math))