def binarySearch(array, value):
	lower = 0
	upper = len(array/2)
	while lower <= upper:
		mid = (lower + upper) / 2
		if array[mid] < value:
			lower += mid + 1
		elif array[mid] > value:
			upper = mid - 1
		else:
			return mid
	return -1

def binarySearch(array, value):
	lower = 0
	upper = len(array) - 1
	while lower <= upper:
		mid = (lower + upper) / 2
		if array[mid] < value:
			lower = mid + 1
		elif array[mid] > value:
			upper = mid - 1
		else:
			return mid
	return - 1

def binary_search(input_array, value):
    lower_index = 0
    upper_index = len(input_array) - 1
    while lower_index <= upper_index:
        mid = (lower_index + upper_index) / 2
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            upper_index = mid - 1
        else:
            lower_index = mid + 1
    return - 1

def binary_search(input_array, value):
    lower_index = 0
    upper_index = len(input_array) - 1
    while lower_index <= upper_index:
        mid = (lower_index + upper_index) / 2
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            upper_index = mid - 1
        else:
            lower_index = mid + 1
    return -1

def binary_search(input_array, value):
    lower_index = 0
    upper_index = len(input_array) - 1
    while lower_index <= upper_index:
        mid = (lower_index + upper_index) / 2
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            upper_index = mid - 1
        else:
            lower_index = mid + 1
    return -1

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    lower_index = 0
    upper_index = len(input_array) - 1
    while lower_index <= upper_index:
        mid = (lower_index + upper_index) / 2
        if input_array[mid] < value:
            lower_index = mid + 1
        elif input_array[mid] > value:
            upper_index = mid - 1
        else:
            return mid
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)