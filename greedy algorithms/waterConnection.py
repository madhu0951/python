a=[7,5,4,2,9,3]
b=[4,9,6,8,7,1]
d=[98,72,10,22,17,66]
c=[]
for i in range(len(a)):
    if a[i] not in b:
        c.append(i)
print(len(c))
for k in range(len(c)):
    l=[a[c[k]],b[c[k]]]
    index=c[k]
    m=0
    while(m==0):
        for j in range(len(a)):
            if b[index]==a[j]:
                index=j
                l.append(b[index])
            else:
                for i in range(len(a)):
                    if b[index] not in a:
                        m=1
    print(l[0],l[-1],d[index])


