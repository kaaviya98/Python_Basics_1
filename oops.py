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

#Triangle perimeter
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return self.a+self.b+self.c
t1=Triangle(2,3,4)
per=t1.perimeter()
print("Perimeter of triangle is ",per)

#School
class School:
    def __init__(self,name,id,sc_name):
        self.name=name
        self.id=id
        self.sc_name=sc_name
    def msg(self):
        print("School is an architecture")
class Student3(School):
    def msg(self):
        print("Student is the one,who learns")
        super().msg()
class Teacher(School):
    def msg(self):
        print("Teacher is the one,who teaches")
        super().msg()

s1=Student3("Kaaviya",21,"Anna Univ")
s1.msg()
s2=Teacher("Madhu",35,"Anna univ")
s2.msg()