# Bubble sort - Best Case O(n), Worst case O(n^2), Average case O(n^2)
def bubbleSort(arr):
	swaps = 0
	l = len(arr)
	for i in range(l):
		for j in range(l-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swaps += 1
		if swaps == 0:
			return arr
	return arr

def bubbleSort(arr):
	swaps = 0
	l = len(arr)
	for i in range(l):
		for j in range(i, l-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swaps += 1
		if swaps == 0:
			return arr
	return arr

def bubble_sort(arr):
	swaps, length = 0, len(arr)
	i = 0
	while i < len(arr):
		for index in range(0, length-1-i):
			if arr[index] > arr[index+1]:
				temp = arr[index+1]
				arr[index+1] = arr[index]
				arr[index] = temp
				swaps += 1
		if swaps == 0:
			break
		i += 1
	return arr
print bubble_sort([1000,678,147,7899,21000,1])

def bubble_sort(arr):
	swaps = 0; length = len(arr)
	for i in range(length):
		for index in range(length-1-i):
			if arr[index] > arr[index+1]:
				temp = arr[index+1]
				arr[index+1] = arr[index]
				arr[index] = temp
				swaps += 1
		if swaps == 0:
			break
	return arr
print bubble_sort([1,100,67, 33, 567])

def bubble_sort(arr):
	swaps = 0; length = len(arr)
	for i in range(length):
		for index in range(length-1-i):
			if arr[index] > arr[index+1]:
				temp = arr[index+1]
				arr[index+1] = arr[index]
				arr[index] = temp
				swaps += 1
		if swaps == 0:
			break
	return arr

# Selection sort
# you should put the smallest element at the first index total O(n^2) be it best/worst/average case.
def selectionSort(a):
	l = len(a)
	for i in range(a-1):
		min = i
		for j in range(i+1, l):
			if a[j] < a[i]:
				min = j
		temp = a[i]
		a[i] = a[min]
		a[min] = temp
	return a
	
def selection_sort(arr):
	length = len(arr)
	for i in range(length):
		min_value_index = i
		for j in range(i+1, length):
			if arr[j] < arr[min_value_index]:
				min_value_index = j+1
		temp = arr[min_value_index]
		arr[min_value_index] = arr[i]
		arr[i] = temp
	return arr

print selection_sort([111400,54545678,147,7899,21000,187978])
print selection_sort(['a', 'd', 'c', 'b'])

def selection_sort(arr):
	length = len(arr)
	for i in range(length):
		min_value_index = i
		for j in range(i+1, length):
			if arr[j] < arr[min_value_index]:
				min_value_index = j+1
		temp = arr[min_value_index]
		arr[min_value_index] = arr[i]
		arr[i] = temp
	return arr
print selection_sort([1, 4, 3, 2])


# Insertion sort - THIS IS USING ADDITIONAL SPACE!
def insertionSort(a):
    sorted = [a[0]]
    for i in range(1, len(a)):
    	tempSorted = []
    	j = 0
    	while j < len(sorted) and a[i] > sorted[j]:
    	    tempSorted.append(sorted[j])
    	    j += 1
        tempSorted.append(a[i])
        for k in range(j, len(sorted)):
            tempSorted.append(sorted[k])
    	sorted = tempSorted
    return sorted

# Insertion sort in-place algo!! Finally did it man!! I implemented Insertion sort
def insertion_sort(a):
	for i in range(n):
		key = a[i]
		j = i - 1
		while j >= 0 and key < a[j]:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key
	return a

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
	
def insertionSort(a):
	for i in range(1, len(a)):
		key = a[i]
		j = i - 1
		while j >= 0 and key < a[j]:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key
	return a
	
# Merge sort
def mergeSort(a):
	if len(a) < 2:
		return a
	else:
		pivot = len(a) / 2
		sorted = []
		A = mergeSort(a[:pivot])
		B = mergeSort(a[pivot:])
		i = j = k = 0
		while i < len(A) + len(B):
			if j < len(a) and k >= len(B):
				sorted.append(A[j])
				j += 1
			elif j >= len(A) and k < len(B):
				sorted.append(B[k])
				k += 1
			else:
				if A[j] <= B[k]:
					sorted.append(A[j])
					j += 1
				else:
					sorted.append(B[k])
					k += 1
			i += 1
		return sorted

def mergeSort(a):
	if len(a) < 2:
		return a
	else:
		pivot = len(a) / 2
		sorted = []
		A = mergeSort(a[:pivot])
		B = mergeSort(a[pivot:])
		i = j = k = 0
		while i < len(A) + len(B):
			if j < len(A) and k >= len(B):
				sorted.append(A[j])
				j += 1
			elif j >= len(A) and k < len(B):
				sorted.append(B[k])
				k += 1
			else:
				if A[j] <= B[k]:
					sorted.append(A[j])
					j += 1
				else:
					sorted.append(B[k])
					k += 1
			i += 1
		return sorted

def merge_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		sorted = []
		pivot = int(len(arr)/2)
		A = merge_sort(arr[:pivot])
		B = merge_sort(arr[pivot:])
		i, j, k = 0, 0, 0
		while i < len(A)+len(B):
			if j >= len(A) and k < len(B):
				sorted.append(B[k])
				k += 1
				i += 1
			elif k >= len(B) and j < len(A):
				sorted.append(A[j])
				j += 1
				i += 1
			else:
				if A[j] < B[k]:
					sorted.append(A[j])
					j += 1
					i += 1
				else:
					sorted.append(B[k])
					k += 1
					i += 1
		return sorted

print merge_sort([1000,678,147,7899,21000,1])

# I fucking can't believe that my merge sort is working!!!!!!! I should never ever underestimate myself!

def merge_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		sorted = []
		pivot = len(arr)/2
		A = merge_sort(arr[:pivot])
		B = merge_sort(arr[pivot:])
		i, j, k = 0, 0, 0 
		while i < len(A)+len(B):
			if j >= len(A) and k < len(B):
				sorted.append(B[k])
				k += 1
			elif k >= len(B) and j < len(A):
				sorted.append(A[j])
				j += 1
			else:
				if A[j] < B[k]:
					sorted.append(A[j])
					j += 1
				else:
					sorted.append(B[k])
					k += 1
			i += 1
		return sorted
print merge_sort([1000,678,147,7899,21000,1])

def merge_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		sorted = []
		pivot = int(len(arr)/2)
		A = merge_sort(arr[:pivot])
		B = merge_sort(arr[pivot:])
		i, j, k =0, 0, 0
		while i < len(A)+len(B):
			if j >= len(A) and k < len(B):
				sorted.append(B[k])
				k += 1
			elif k >= len(B) and j < len(A):
				sorted.append(A[j])
				j += 1
			else:
				if A[j] < B[k]:
					sorted.append(A[j])
					j += 1
				else:
					sorted.append(B[k])
					k += 1
			i += 1
		return sorted

print merge_sort([1000,678,147,7899,21000,1])

#Quick Sort:
def partition(a, begin, end):
	if begin >= end:
		return a
	else:
		pivot = end
		i = begin
		while i < pivot:
			if a[i] > a[pivot]:
				a[i], a[pivot-1] = a[pivot-1], a[i]
				a[pivot-1], a[pivot] = a[pivot], a[pivot-1]
				pivot -= 1
			else:
				i += 1
		partition(a, begin, pivot-1)
		partition(a, pivot+1, end)
	return a
		
def quickSort(a):
	return partition(a, 0, len(a)-1)


# Counting Sort: O(n) time complexity for small order of n, actually for any value of n but a lot of space will be
# wasted if n is 10^5 or 10^6 or soo. limit it to n < 10^4 or something like that! Less than 1 lakh.
def countingSort(a):
	sorted = [0] * max(a)
	for i in a:
		sorted[i] += 1
	result = []
	for i in range(len(sorted)):
		for j in range(s[i]):
			result.append(i)
	return result
		

