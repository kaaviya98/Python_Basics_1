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
  
con_li_dic = [{new_k : new_val[x] for new_k, new_val in new_dictiy.items()for x in range(2)} for x in range(2)]
print ("Convert list into dictionaries:",con_li_dic)