class Even:
    def __init__(self,max):
        self.n=2
        self.max=max
    # def __iter__(self):
    #     return self
    def __next__(self):
        while(True):
            if self.n<=self.max:
                 res=self.n
                 self.n+=2
                 return res
            else :
                break
num=Even(50)
#num.__next__()
for i in range (0,50):
    print(next(num))
def even_gen(max):
        n=2
        #while(True):
        #     if n<=max:
        while(n<=max):
             yield n
             n+=2
#             
# #num.__next__()
max=50
# num=even_gen(max)
num=even_gen(max)
for i in even_gen(max):
     print(next(num))
#new

def fun_generator():
	yield "Hello world!!"
	yield "Geeksforgeeks"
obj = fun_generator()
print(type(obj))
for i in fun_generator():
     print(i)
# print(next(obj))
print(dir(list))


