k=4
t=5
jobs=[10,7,8,12,6,8]
e=sum(jobs)//4
l=[]
j=0
sum=0
i=0
while(j!=k):
    sum=sum+jobs[i]
    if sum<10:
        i+=1
    else:
        l.append(sum)
        j+=1
        i+=1
        sum=0
print(max(l)*t)
