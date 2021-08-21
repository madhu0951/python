def maxNoPlatform(a,d,n):
    a.sort()
    d.sort()
    pre=1
    need=1
    i=1
    j=0
    while(i<n and j<n):
        if (a[i]<=d[j]):
            pre+=1
            i+=1
        elif (a[i]>d[j]):
            pre-=1
            j+=1
        if pre>need:
            need=pre
    return need

arr=[900,940,950,1100,1500,1800]
dep=[910,1200,1120,1130,1900,2000]
n=len(arr)
print(maxNoPlatform(arr,dep,n))
