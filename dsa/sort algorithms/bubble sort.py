def bubble_sort(elements):
    size=len(elements)
    for j in range(size-1):
        for i in range(size-1):
            if elements[i]>elements[i+1]:
                temp=elements[i]
                elements[i]=elements[i+1]
                elements[i+1]=temp
elements=[5,9,2,1,67,34,88,34]
bubble_sort(elements)
print(elements)




def bubbleSort(arr):
    flag=False
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if flag:
            flag=False
        else:
            break
    return arr
print(bubbleSort([67,8,34,23,54,65,75,23,4,45]))

#Non recursive
#Stable
#In place
#O(n²)
