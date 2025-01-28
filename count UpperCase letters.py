#COUNT NUMBER OF UPPER AND LOWER CASE LETTERS
x=input("Enter a String : ")
u_count=0
l_count=0
for i in x:
    if('A'<=i and i<='Z'):
        u_count+=1
    else:
        l_count+=1
print(f"{u_count} UpperCase Letters and {l_count} LowerCase Letters in {x}")
        
