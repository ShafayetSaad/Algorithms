def merge(a, b):
    merged_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0
    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1
        else:
            merged_list.append(b[index_b])
            index_b += 1
    if index_a < len_a:
        merged_list.extend(a[index_a:])
    elif index_b < len_b:
        merged_list.extend(b[index_b:])
    return merged_list


def merge_sort(Li):
    if len(Li) <= 1:
        return Li
    mid = len(Li) // 2
    left = merge_sort(Li[:mid])
    right = merge_sort(Li[mid:])
    return merge(left, right)

if __name__ == '__main__':
    a = [1, 3, 5, 6, 7, 2, 4, 8, 9]
    print('Expected:', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print('Got:', merge_sort(a))
