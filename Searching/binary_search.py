def binary_search(list, value):
	left, right = 0, len(list)-1
	while left <= right:
		mid = (left+right)//2
		if list[mid] == value:
			return mid
		if list[mid] < value:
			left = mid + 1
		else:
			right = mid - 1
	return -1

if __name__ == '__main__':
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	value = 5
	print(binary_search(array, value))
