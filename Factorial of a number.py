#FIND FACTORIAL OF A NUMBER
x=int(input("Enter a Whole Number :"))
factorial=1
for i in range(1,x+1):
    factorial=factorial*i
print(f"{x} Factorial = {factorial}")
