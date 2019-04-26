def count_sort(L, max):
    count = [0] * (max + 1)
    #print(count)
    sorted_list = []
    for item in L:
        count[item] = count[item] + 1
    #print(count)
    for index, value in enumerate(count):
        if value > 0:
            sorted_list.extend([index] * value)
    return sorted_list


if __name__ == '__main__':
    a = [3, 4, 1, 6, 2, 4, 9, 7, 8, 4, 2, 1]
    print('Expected:', [1, 1, 2, 2, 3, 4, 4, 6, 7, 8, 9])
    print('Got:', count_sort(a, 10))
