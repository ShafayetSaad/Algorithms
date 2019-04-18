def selection_sort(list):
    """This function takes a list as input and sorts it by selection sort algorithm"""
    for i in range(len(list)-1):
        index_min = i
        for j in range(i+1, len(list)):
            if list[j] < list[index_min]:
                index_min = j
        if index_min != i:
            list[i], list[index_min] = list[index_min], list[i]
    return list

if __name__ == '__main__':
    li = [6, 1, 4, 9, 2]
    print("Before sort:", li)
    list = selection_sort(li)
    print('After sort:', list)
