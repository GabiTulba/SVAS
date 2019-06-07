from sort_animator import SortAnimator
from sorting_algorithms import *
import random

algorithms = [BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort, HeapSort, ShellSort, CombSort]
arraySize = [15, 30, 20, 20, 50, 20, 20, 20]
filenames = ["BubbleSort.png", "SelectionSort.png", "InsertionSort.png", "MergeSort.png", "QuickSort.png", "HeapSort.png", "ShellSort.png", "CombSort.png"]

for SortingAlgorithm, size, filename in zip(algorithms, arraySize, filenames):

	array = [i for i in range(size)]
	random.shuffle(array)

	Animator = SortAnimator(array, SortingAlgorithm)
	Animator.Sort()
	Animator.ExportStatic("examples/"+filename, show = False, save = True)
