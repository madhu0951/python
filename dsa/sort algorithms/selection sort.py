def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

print(selection_sort([12,3,5,6,4,64,23,13]))

## Non recursive
## Unstable
## In place
## O(n²)
