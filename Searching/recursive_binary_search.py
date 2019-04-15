def binary_search(array, left, right, value):
    if left > right:
        return -1 #The value is not in the list
    mid = (left+right) // 2
    if array[mid] == value:
        return mid
    if array[mid] < value:
        return binary_search(array, mid+1, right, value)
    else:
        return binary_search(array, left, mid-1, value)

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    item = 8
    left = 0
    right = len(array) - 1
    print("Expected output:", array.index(item))
    print("function's output:", binary_search(array, left, right, item))
