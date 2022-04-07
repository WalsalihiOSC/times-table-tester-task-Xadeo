
from  tkinter import *
import random

class Check:
	def __init__(self):
		self.randnum = (random.randint(1,20))
		self.randnum1 = (random.randint(1,20))
		self.answer = self.randnum * self.randnum1
	
	def check(self, inputanswer):
		"""Checks if the input is valid"""
		if int(inputanswer) == self.answer:
			return inputanswer + "is correct."
		else:
			return inputanswer + "is no correct"

class Timestb_TesterGUI:
	def __init__(self, parent):
		font = ("Comic Sans MS", "10", "bold")

		question_label = Label(parent, text = "", font = font)
		question_label.grid(row = 0, column = 0)

		self.entrypoint = Entry(parent, width = 5)
		self.entrypoint.grid(row = 0, column = 1)

		Bt1 = Button(parent, text = "Check Answer")
		Bt1.grid(row = 1, column = 0)

		Bt2 = Button(parent, text = "Next")
		Bt2.grid(row = 1, column = 1, padx = 10)
		

#main routine
if __name__ == "__main__": 
	root = Tk()
	timestb_tester = Timestb_TesterGUI(root)
	root.mainloop()