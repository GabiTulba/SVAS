from sort_animator import SortAnimator
from sorting_algorithms import *
import random

array = [i for i in range(10)]
random.shuffle(array)
array2 = list(array)

Animator = SortAnimator(array, BubbleSort)
Animator.Sort()
Animator.ExportStatic("examples/BubbleSort.png", show = False, save = True)