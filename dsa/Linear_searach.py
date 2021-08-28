def linear_search(numbers_list,number_to_find):
    for index,element in enumerate(numbers_list):
        if element==number_to_find:
            return index
    return -1


if __name__=="__main__":
    list=[23,56,43,6,4,12,45,34]
    num_to_find=45

    index=linear_search(list,num_to_find)
    print(f"Number found at index {index} using linear search")