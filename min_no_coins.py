
def minNoCoin(val):
    count=0
    sum=val
    d=[1000,500,100,50,20,10,5,2,1]
    de=[x for x in d if x<=val]

    while(sum!=0):
        if max(de)<=sum:
            sum=sum-max(de)
            count=count+1
        else:
            de.remove(max(de))
    return count

value=93
a=minNoCoin(value)
print(a)