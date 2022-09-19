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