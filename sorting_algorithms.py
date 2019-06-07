def BubbleSort(array):
	states = []

	for i in range(len(array)):
		for j in range(len(array) - 1 - i):
			if array[j] > array[j + 1]:
				states.append(list(array))
				array[j], array[j + 1] = array[j + 1], array[j]
	
	states.append(list(array))
	return states
	
def SelectionSort(array):
	states = []
	
	for i in range(len(array)):
		minpos = i
		min = array[i]
	
		for j in range(i, len(array)):
			if min < array[j]:
				min = array[j]
				minpos = j
				
		if i != minpos:
			states.append(list(array))
			array[i], array[minpos] = array[minpos], array[i]
	
	states.append(list(array))
	return states
		
def InsertionSort(array):
	states = []
	
	for i in range(len(array) - 1):
		if array[i + 1] < array[i]:
			j = i
	
			while j >= 0 and array[j + 1] < array[j]:
				states.append(list(array))
				array[j + 1], array[j] = array[j], array[j + 1]
				j -= 1
	
	states.append(list(array))
	return states

def MergeSort(array, start = None, end = None): #modified in order to do swaps instead of using extra memory, worst case complexity is O(N^2)
	if start == None and end == None:
		start = 0
		end = len(array) - 1

	states = []
	middle = (start + end) // 2
	
	if start >= end:
		return states
	
	states += MergeSort(array, start, middle)
	states += MergeSort(array, middle + 1, end)	
	
	i = start
	while i <= middle:
		aux = middle + 1
		if array[i] > array[aux]:
			while aux < end and array[i] > array[aux + 1]:
				aux += 1
				
			states.append(list(array))
			array[i], array[aux] = array[aux], array[i]
		else:
			i += 1
			
	if start == 0 and end == len(array) - 1:
		states.append(list(array))
	
	return states
	
def QuickSort(array, start = None, end = None):
	if start == None and end == None:
		start = 0
		end = len(array) - 1
	
	states = []
	pivot = array[end]
	index = start
	
	if start >= end:
		return states
	
	for i in range(start,end):
		if array[i] < pivot:
			if index != i:
				states.append(list(array))
				array[i], array[index] = array[index], array[i]
				
			index += 1
	
	states += QuickSort(array, start, (start + end) // 2)
	states += QuickSort(array, (start + end) // 2 + 1, end)
	
	if start == 0 and end == len(array) - 1:
		states.append(list(array))
	
	return states

def HeapSort(array):
	
	HeapSize = len(array) - 1
	states = []
	
	for i in range(len(array)):
		while i > 0 and array[i] > array[(i - 1) // 2]:
			states.append(list(array))
			array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
			i = (i - 1) // 2

	for i in range(len(array)):
		states.append(list(array))
		array[0], array[HeapSize] = array[HeapSize], array[0]
		HeapSize -= 1
		index = 0
		while 2 * index + 1 <= HeapSize:
			max = array[2 * index + 1]
			maxpos = 2 * index + 1
			
			if 2 * index + 2 <= HeapSize and array[2 * index + 2] > max:
				max = array[2 * index + 2]
				maxpos = 2 * index + 2
			
			if array[index] < max:
				states.append(list(array))
				array[index], array[maxpos] = array[maxpos], array[index]
				index = maxpos
			else:
				break
		
	states.append(list(array))	
	
	return states

def ShellSort(array): #implemented with gap(n) = N/(2^n), worst case complexity O(N^2), feel free to implement other faster methods.
	states = []
	shrinkingFactor = 2
	gap = len(array) // shrinkingFactor

	while gap > 0:
		for i in range(gap,len(array)):
			if array[i] < array[ i - gap]:
				j = i - gap
				while j >= 0 and array[j] > array[j + gap]:
					states.append(list(array))
					array[j], array[j + gap] = array[j + gap], array[j]
					j -= gap
	
		gap //= 2
	
	states.append(list(array))
	
	return states

def CombSort(array):
	states = []
	shrinkingFactor = 1.247 #(1 - e ^ - phi) ^ -1
	gap = len(array)
	sorted = False
	
	while not sorted or gap != 1:
		
		gap = int(gap / shrinkingFactor)
		if gap < 1:
			gap = 1
		
		sorted = True
		
		for i in range(0, len(array) - gap):
			if array[i] > array[i + gap]:
				states.append(list(array))
				array[i], array[i + gap] = array[i + gap], array[i]
				sorted = False
				
	states.append(list(array))
			
	return states
	
# I encourage anyone who wants to help to implement more comparison sorting algorithms.
# The only criteria to be met by the sorting function is that it takes as input
# an array and it outputs an array of all the states of the array.
# A new state is considered after each swap(i,j) where i!=j.