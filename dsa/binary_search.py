def binary_search(numbers_list,number_to_find):
    left_index=0
    right_index=len(numbers_list)-1
    mid_index=0
    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=numbers_list[mid_index]

        if mid_number==number_to_find:
            return mid_index

        if mid_number<number_to_find:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return -1

if __name__=="__main__":
    list=[12,23,34,45,56,67,78,89,90]
    number_to_find=34
    result=binary_search(list,number_to_find)
    print(f"Number found at index {result} using binary search")