List=[1,-2,3,4,5]
#print(dir(List))
k=List.__add__([2,3])
List.extend([6,7,8])
print(List)
print(k)
print([2]*3)
list1=["Testpress",100,"python",-7.8,99.9999]
empty_list=[]
print(List[:])
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
list1.append("Employee-Kaaviya")
print(list1)
list1.insert(2,"Pallavaram")
print(list1)
list1.insert(len(list1)-1,"Trainee")
print(list1)
list1.remove("Employee-Kaaviya")
print(list1)

#copylist
list2=list1.copy()
print(list2)
string={1:2,2:3,3:3,4:2,5:2,6:2}
print(string)
list10=string.items()
print(list10)
con_dict = { 'Pink': 176, 'Brown': 94, 'Blue': 24 }
 
my_lis = [] #empty list
for e in con_dict:
   t = (e, con_dict[e])
   my_lis.append(t)
print("List of tuple:",my_lis)

##COMPREHENSION
gang1={'kaavs','mad','subi','vish'}
gang2=['vel','vimal','abi','akshu']
new_gang=[ele.upper()if len(ele)<5 else ele  for ele in gang1 ]
print(new_gang)
import os
import glob
n1=[os.path.realpath(f) for f in glob.glob('*.py')]
n2={f: os.stat(f).st_size for f in glob.glob('*.py') if os.stat(f).st_size>1000}
print(list(n2.keys()))
print(n2)



