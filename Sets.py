from typing import final


names={'a','b','c','d','c'}
print(names)
name0=set()
name1=set([2,3,4,5,"kaavs"])
name2=set((2,-4,"kaavs"))
name3=set("pythonnn")
name4=set({('name','id','place'):('Kaaviya','21','Chennai')}.keys())
name5=frozenset(((1,2,3),(3,4,4),(4,3,2)))
try:
    name5[1] =(2,3,4) 
    print(name5)
finally:
    print("OOPS!!")
print(name1)
print(name2)
print(name3)
print(name4)
names.add("kaavs")
print(names)
names.update({"section":"C"})
print(names)
values={1,2,3,4,5}
values.add((6,7,8))#one argument
print(values)
values.discard(19)
values.update("String")#many arguments
print(values)


