def bubble_sort(array):
    """This function takes a list as input and sorts it by bubblegit  sort algorithm"""
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    list = [6, 1, 4, 9, 2]
    print("Before sort:", list)
    bubble_sort(list)
    print("After sort:", list)
