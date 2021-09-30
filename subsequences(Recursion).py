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