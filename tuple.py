values=(21,23,-45,56)
print(values)
print(values[3])
print(values[0:])
for i in values:
    if i>0  :
     print(i)
print (values[3:1])
c=len(values)-1
while(c>=0):
    print(values[c])
    c=c-1
quote = "Talk is cheap. Show me the code."
print("1.", quote[3])
print("2.", quote[-3])
print("3.", quote.replace("code", "program"))