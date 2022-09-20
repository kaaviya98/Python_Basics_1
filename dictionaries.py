person={10:['Kaaviya'],("Age","mark"):("24",90)}
print(person["Age","mark"])
print(person.get("percent","90"))
person["percent"]="90percent"
print(person)
person.pop("percent")
print(person)
#iteration
for i in person:
    print(i)
    print(person[i])