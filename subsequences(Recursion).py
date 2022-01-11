def printSubSequences(arr, index, subarr):
    if index == len(arr):
        if len(subarr) != 0:
            print(subarr)
    else:
        printSubSequences(arr, index + 1, subarr)
        printSubSequences(arr, index + 1, subarr + [arr[index]])

    return


a = [1, 2, 3]
printSubSequences(a, 0, [])




#Using itertools

from itertools import combinations
arr=[1,2,3,4]
for i in range(1,len(arr)+1):
    for j in combinations(arr,i):
        print(list(j))
