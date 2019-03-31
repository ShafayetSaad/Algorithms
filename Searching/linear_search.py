def linear_search(list, value):
	for i in range(len(list)):
		if list[i] == value:
			return i
	return -1

if __name__ == '__main__':
	array = [5, 1, 3, 9, 6, 0, 4, 8, 4, 7, 2]
	value = 0
	print(linear_search(array, value))
