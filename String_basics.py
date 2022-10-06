from encodings import utf_8


text="Hi "
text1="there!!"
print(text+" "+text1)
#multiple lines
text3='''Hi,
how's it going?'''
print(text3)
print("Kaaviya\'s textbook is the one that says,\"Pride and Prejudice\"")
print(text[1])
print(text1[-1])
print(text1[0:4])
print(text1[5])
#new_text=text*3
#print(new_text)
#for i in text3:
#    print(i)
print("going" in text3)
print("ingo" in text3)
#Stringmethods(few)
text="I like Python"
res=text.lower()
print(res)
res=text.upper()
print(res)
res=text.find("like")
print(res)
res=text.replace("Python","Java")
print(res)
val=[1,2,3,4,3]
r=str(val)
person={10:['Kaaviya'],("Age","mark"):("24",90)}
names={'a','b','c','d','c'}
r=str(person.values())
v=str(names)
print(v)
print(v[0])
s="hello"" ""world"
print(s)
s1 = '深入 Python'
print(len(s1))
stri='s','t','r','i','n','g'
print(str(stri))
##splitmethod
query = 'user=pilgri=m&database=master&password=PapayaWhip'
a_list = query.split('&') 
print(a_list)#['user=pilgri=m', 'database=master', 'password=PapayaWhip']
a_list_of_lists = [v.split('=', 1) for v in a_list ] 
print(a_list_of_lists)
a_dict = dict(a_list_of_lists) 
print(a_dict)
by = b'b';s='str'
print(s.encode('utf_8'))
print(by)
print(s+by.decode('ascii'))
bb='\xff'
print(bb)
bbb=bytearray(by)
print(bbb)
a_string = '深入 Python'
by = a_string.encode('big5') 
ret=by.decode('big5')
print(ret)