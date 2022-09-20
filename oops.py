#Student with object
from tabnanny import check
from unicodedata import name


class Student:
    def check_pass_fail(self):
        if self.marks>75:
            print("Outstanding")
        else:
            print("Try harder")
student = Student()
student.name="Kaavs"
student.marks=95
student.check_pass_fail()
# The init method
class Student1:
    name=""
    mark=0
    def check(self):
        if self.mark>80:
            print(self.name," is ","Good")
        else:
            print(self.name," is ","bad")
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
stu=Student1("kaav",50)
stu1=Student1("Mad",95)
stu.check()
stu1.check()
#Complex numbers
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def adding(self,var2,var3):
         real=self.real+var2.real+var3.real
         imag=self.imag+var2.imag+var3.imag
         return Complex(real,imag)
n1=Complex(2,1)
n2=Complex(3,2)
n3=Complex(1,1)
add=n1.adding(n2,n3)
print("add of complex num is ",add.real,"+",add.imag,"i")
