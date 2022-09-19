'''Basics of Python'''
#print("hello world!!")
city = "Goa"
print(city)

num= int(input("Enter value : "))
print(num)

#Discout 
fee= 4535
discount_percent =10
discounted_fee =(discount_percent/100)*4535
reduced_fee=fee-discounted_fee
print(reduced_fee)

#kilometer_to_miles
distance_km=54
distance_miles= distance_km*0.621371
print(distance_miles)

#positive_negative(if_else)
number =float(input("Enter value: "))
if number==0:
    {print("Number is Zero")}
elif number>0:
    print("Number is positive")
else :
    print ("Number is negative")   

#loop
language= ["Java","python","Swift","C","C++","Honda"]
for i in language:
    if i=="Swift" or i == "Honda" :
        continue
    else :
        print (i)
     
#Increment
count=0;
while count<5:
    print(count)
    count=count+1
#multiplication
num1=int(input("Enter the multiplication table number :"))
for count in range (1,11):
    product1=num1*count
    print(num1,"x",count,"=",product1)
# sum of natural numbers 1-100
sum=0
for count in range(1,101):
    pass #pass statement
    #sum=sum+count
#print("Sum is:",sum)
print("Hi")

#Function
def addition(num1,num2):
    res=num1+num2
    return res
    
res=addition(3,4)
print("Result :",res)
    
#Grader
marks=[55,64,75,80,65]
no_of_marks=len(marks)
sum=0 #global variable
def average(marks):
    for i in marks:
        global sum
        sum =sum + i
        print("Sum:",sum)
    avg=sum/no_of_marks
    print("Average:",avg)
    return avg
total=average(marks)
if total > 80:
    print("Grade A")
elif 80>total>=60:
    print ("Grade B")
elif 60>total>=50:
    print("Grade C")
else:
    print("Failed,Sorry!")

#Add and Multiply
def add(num1,num2):
    sum=num1+num2
    return sum
def prod(num1,num2):
    prod=num1*num2
    return prod
addition=add(2,3)
product=prod(5,4)
print("Addition:",addition)
print("product:",product)
#List
names=["Kaaviya","Madhu","Subi","Geni"]
print(names[2])
list=["Kaaviya","2",2.5,-3,-4.5,100000,0]
for i in list:
    print(i)
print(list[3])
def welcome(name,message):
    print("Hi",name)
    print(message)
welcome("Kaaviya","welcome")
    

