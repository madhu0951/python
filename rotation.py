a=input("enter first string: ")
b=input("enter second string: ")
c=["".join(a[j+1:]+a[:j+1]) for j in range(len(a)-1)]
if b in c:
    print("Yes")
else:
    print("no")