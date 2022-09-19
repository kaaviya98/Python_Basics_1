from itertools import count
from queue import Empty


List=[1,-2,3,4,5]
list1=["Testpress",100,"python",-7.8,99.9999]
empty_list=[]
print(List[2])
print(list1[1:4])
print(list1[:2])
print(List[2:])
print(empty_list)
count=-1
while(count<0 and count >=(-len(List))):
    print(List[count])
    count=count-1
for i in list1:
    print(i)
print ("Testpress"in list1)



