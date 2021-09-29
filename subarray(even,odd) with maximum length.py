""" find maximum subarray length which has same number of even and odd numbers"""

def max_length(l):
    li=[]
    length=[]
    for i in range(0,len(l)+1):
        for j in range(i,len(l)):
            ceven=0
            codd=0
            a=l[i:j+1]
            for k in range(len(a)):
                if a[k]%2==0:
                    ceven=ceven+1
                else:
                    codd=codd+1
            if ceven==codd:
                li.append(a)
                length.append(len(a))
    return max(length)

l=[1,2,3,4,5]
print(max_length(l))