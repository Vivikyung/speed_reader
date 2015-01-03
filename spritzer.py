from DrawingTemplate import *

class WordGenerator:
	def __init__(self,filename):
		'''
		Takes file and creates a list with every word from that file
		'''
		with open(filename)as f:
			self.file = f.readlines()
		self.file = [x.replace("\n", "") for x in self.file]
		self.file = [x.split(" ") for x in self.file]
		self.wordList = []
		for x in self.file:
			self.wordList.extend(x)
		self.counter = -1
	
	def next_word(self):
		'''
		if n == 0:
			return self.file[n]
		else:
			return self.file[n] + next_word(self,)
		return self.file
		'''
		while self.counter < len(self.wordList):
			if self.is_empty():
				return "valueError"
			else:
				self.counter += 1
				return self.wordList[self.counter]

	def is_empty(self):
		return self.counter == len(self.wordList) - 1

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return "{0}".format(self.wordList)

	# def is_quotes(self):
	# 	# for x in wordList:
	# 	pass

	def centering(self):
		'''
		Highlights the focus letter in red
		'''
		focus = 0
		for x in wordList:	
			if len(x) > 13:
				focus = 5
			elif len(x) > 9:
				focus = 4
			elif len(x) > 5:
				focus = 3
			elif len(x) > 1:
				focus = 2
			else:
				focus = 1
			x[focus].color = "red"


def animate_text(gen,width,height,size,delay):
	panel = DrawingPanel(width,height)
	canvas = panel.canvas
	while not gen.is_empty():
		canvas.delete("all")
		if gen.next_word()[len(gen.next_word())-1] == "." or gen.next_word()[len(gen.next_word())-1] == "," or gen.next_word()[len(gen.next_word())-1] == ";":
			canvas.create_text(width/2, height/2, text = gen.next_word(), font = ("Courier", size))
			panel.sleep(delay*1.3)
		else:
			canvas.create_text(width/2, height/2, text = gen.next_word(), font = ("Courier", size))
			panel.sleep(delay)


def main():
	gen1 = WordGenerator("test.txt")
	animate_text(gen1, 600, 600, 16, 40)

main()

#90 milliseconds = max speed
#faster it is, harder to read, less comprehension
