def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low, high):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1]
    #print(L)
    return i + 1

def quick_sort(L, low, high):
    if low >= high:
        return
    p = partition(L, low, high)
    quick_sort(L, low, p-1)
    quick_sort(L, p+1, high)
    #return L


if __name__ == '__main__':
    a = [9, 3, 5, 6, 1, 2, 4, 8, 7]
    print('Expected:', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    quick_sort(a, 0, len(a)-1)
    print('Got:', a)
