#CHECK WHETHER A NUMBER IS PRIME
x=int(input("Enter a Whole Number :"))
count=0
for i in range(1,x+1):
    if(x%i==0):
        count+=1
    else:
        continue
if(count==2):
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")
    
    
    
