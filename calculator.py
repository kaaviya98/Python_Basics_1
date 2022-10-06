class Calculator:
    def __init__(self,a,b):
       self.a=a
       self.b=b
#     def __call__(self):
#        return self.add()
    def add(self):
      return self.a+self.b   
    def sub(self):
       return self.a-self.b
    
c=Calculator(2,3)

print('{0.c.add}'.format(c))