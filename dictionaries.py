# person={10:['Kaaviya'],("Age","mark"):("24",90)}
# # print(person[("Age","mark")])
# w=person.get(1,"90")
# # person["percent"]="90percent"
# print(w)
# # person.pop("percent")
# # print(person)
# #iteration
# # for key in person:
# #     print(key)
# #     print(person[key])
# #dictionary to dictionary
new_dictiy = { "p" : [4, 9], "d" : [5, 8], "l" : [19, 18] }
  
con_li_dic = [{new_k : new_val[x] for new_k, new_val in new_dictiy.items() if new_k>'d'} for x in range(0,2) ]

print ("Convert list into dictionaries:",con_li_dic)
##dictionary conversion
my_dict = dict(([1,'apple'], [2,'ball']))
print(my_dict)
dic1=dict(([1,2],[3,5],[3,4]))
print(dic1)