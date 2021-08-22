def printsorted(arr):
    l=[]
    arr.sort(key=lambda x:x[2])
    arr=arr[::-1]
    sum=0
    p=[0 for x in range(len(arr))]
    for i in range(len(arr)):
        if p[arr[i][1]-1]==0:
            p[arr[i][1]-1]=arr[i][0]
            sum=sum+arr[i][2]
        else:
            for j in range(p[arr[i][1]]-1,-1,-1):
                if p[j]==0:
                    p[j]=a[i][0]
                    sum=sum+arr[i][2]
                    break
    try:
        while True:
            p.remove(0)
    except ValueError:
        pass
    return p


a=[["a",4,20],["b",1,10],["c",1,40],["d",1,30]]
lis=printsorted(a)
print(" ".join(lis))