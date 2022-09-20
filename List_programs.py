List=[1,-2,3,4,5]
#print(dir(List))
k=List.__add__("5")
print(k)
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



