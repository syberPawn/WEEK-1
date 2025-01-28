#FIND LARGEST ITEM IN A LIST
list=[2,4,6,8]
largest=0
for i in list:
    if(i>largest):
        largest=i
    else:
        largest=largest
print(f"The largest item in the list is {largest}")
