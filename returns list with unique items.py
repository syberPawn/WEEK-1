#return new list with unique items
list=[1,2,3,4,5,4,3,2,1]
unique_list=[]
for i in list:
    if(i not in unique_list):
        unique_list.append(i)
    else:
        print()
print(unique_list)
