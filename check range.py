#CHECK WHETHER A NUMBER IS IN A GIVEN RANGE
start=int(input("Enter Starting Number :"))
end=int(input("Enter Ending number :"))
x=int(input("Enter your number:"))
if(start <= x and x <=end):
    print(f"{x} is in Range")
else:
    print(f"{x} is out of Range")
