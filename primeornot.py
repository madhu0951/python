a=int(input("enter the number: "))
count=0
for i in range(2,a+1):
    if a%i==0:
        count+=1
if count==1:
    print("given number is prime")
else:
    print("given number is not a prime")