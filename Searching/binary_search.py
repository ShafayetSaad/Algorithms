def binary_search(list, value):
    """This function takes a list as input and a value to find.Then it searches for that value using binary search"""
    left, right = 0, len(list)-1
    while left <= right:
        mid = (left+right)//2
        if list[mid] == value:
            return mid #Returning the index
        if list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1 #The value is not in the list

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = 9
    print("Expected output:", array.index(value))
    print("function's output:", binary_search(array, value))
