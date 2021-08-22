#p=[[1,1],[3,4],[-1,0]]
p=[[3,2],[-2,2]]
count=0
if len(p)==2:
    a=0
else:
    a=1
for i in range(a,len(p)):
    while(p[i]!=p[i-1]):
        if p[i-1][0]<p[i][0] and p[i-1][1]<p[i][1]:
            p[i-1][0]+=1
            p[i-1][1]+=1
            count+=1
        elif p[i-1][0]==p[i][0] and p[i-1][1]<p[i][1]:
            p[i-1][1]+=1
            count+=1
        elif p[i-1][0]<p[i][0] and p[i-1][1]==p[i][1]:
            p[i-1][0]+=1
            count+=1
        elif p[i-1][0]>p[i][0] and p[i-1][1]>p[i][1]:
            p[i-1][0]-=1
            p[i-1][1]-=1
            count+=1
        elif p[i-1][0]==p[i][0] and p[i-1][1]>p[i][1]:
            p[i-1][0]-=1
            count+=1
        elif p[i-1][0]>p[i][0] and p[i-1][1]==p[i][1]:
            p[i-1][1]-=1
            count+=1
print(count)





