a=[3,2,4,5,3,5]
a1=sorted(a)
l=[]
sum=0
for i in range(len(a1)):
    sum=sum+a1[i]
    l.append(sum)
print(l)
a.remove(4)
print(a)