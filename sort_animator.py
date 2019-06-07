from sorting_algorithms import *
from PIL import Image, ImageDraw

def pickColor(index, size):
	color = None
	if index < size / 3:
		quantity = int(index / (size / 3) * 255)
		color = (255 - quantity, quantity, 0)
	elif index < 2 * size / 3:
		quantity = int((index - size / 3) / (size / 3) * 255)
		color = (0, 255 - quantity, quantity)
	else:
		quantity = int((index - 2 * size / 3) / (size / 3) * 255)
		color = (quantity, 0, 255 - quantity)
	return color

class SortAnimator:
	
	def __init__(self, array, SortingAlgorithm = BubbleSort):
		self.array = array
		self.arrayLen = len(array)
		self.states = None
		self.statesLen = 0
		self.SortingAlgorithm = SortingAlgorithm
	
	def Sort(self):
		self.states = self.SortingAlgorithm(self.array)
		self.states = [self.states[0]] + self.states + [self.states[-1]]
		self.statesLen = len(self.states)
		
	def ExportStatic(self, filename = None, show = True, save = False):
		height = 26 * len(self.states)
		width = 26 * len(self.array)
		
		img = Image.new("RGB", (width, height), (255, 255, 255))
		drawer = ImageDraw.Draw(img)
		
		for i in range(self.statesLen - 1):
			for j in range(self.arrayLen):
				start = (26 * j + 13, 26 * i + 13)
				end = (26 * self.states[i +
                                    1].index(self.states[i][j]) + 13, 26 * (i +
                                        1) + 13)
				color = pickColor(self.states[-1].index(self.states[i][j]), self.arrayLen)
				drawer.line([start, end], fill = color, width = 5)
		
		if save == True:
			img.save(filename)
		if show == True:
			img.show()
