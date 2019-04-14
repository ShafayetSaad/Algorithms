def linear_search(list, value):
	"""This function takes a list as input and a value to find.Then linearly it searches for that value"""
	for i in range(len(list)):
		if list[i] == value:
			return i #Returning the index
	return -1 #The value is not in the list

if __name__ == '__main__':
	array = [5, 1, 3, 9, 6, 0, 4, 8, 4, 7, 2]
	value = 6
	print("Expected output:", array.index(value))
	print("function's output:", linear_search(array, value))
