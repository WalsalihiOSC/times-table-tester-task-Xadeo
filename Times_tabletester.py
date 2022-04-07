
from  tkinter import *
import random

class Check:
	def __init__(self):
		""" Import random - pick two random nums"""
		self.randnum = (random.randint(1,20))
		self.randnum1 = (random.randint(1,20))
		self.answer = self.randnum * self.randnum1
	
	def vaildate(self, inputanswer):
		"""Checks if the input is valid"""
		if int(inputanswer) == int(self.answer):
			return str(inputanswer) + " is correct."
		else:
			return str(inputanswer) + " is no correct."

class Timestb_TesterGUI:
	def __init__(self, parent):

		self.check = Check()

		self.question_label = Label(parent, text = f"{str(self.check.randnum)} * {str(self.check.randnum1)}")
		self.question_label.grid(row = 0, column = 0)

		self.entrypoint = Entry(parent, width = 5)
		self.entrypoint.grid(row = 0, column = 1)

		Bt1 = Button(parent, text = "Check Answer", command = self.check_answer)
		Bt1.grid(row = 1, column = 0, sticky = SW, padx = 40)

		Bt2 = Button(parent, text = "Next", command = self.next)
		Bt2.grid(row = 1, column = 1, sticky = SE, padx = 40)

		self.outputlabel = Label(parent, text = "", font = ("Comic Sans MS", "10", "bold"))
		self.outputlabel.grid(row = 2, columnspan = 2)

	def next(self):
		check1 = Check()
		self.question_label.configure(text = f"{str(check1.randnum)} * {str(check1.randnum1)}")

	def check_answer(self):
		self.outputlabel.configure(text = self.check.vaildate(self.entrypoint.get()))
#main routine
if __name__ == "__main__": 
	root = Tk()
	timestb_tester = Timestb_TesterGUI(root)
	root.mainloop()