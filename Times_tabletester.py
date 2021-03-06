
from  tkinter import *
import random

class Timestable:
	def __init__(self):
		""" Import random - pick two random nums"""
		self.randnum = (random.randint(1,10))
		self.randnum1 = (random.randint(1,10))
		self.answer = self.randnum * self.randnum1
	
	def vaildate(self, inputanswer):
		"""Checks if the input is valid"""
		try:
			inputanswer = float(inputanswer)
			if int(inputanswer) == int(self.answer):
				return str(inputanswer) + " is correct."
			else:
				return str(inputanswer) + " is no correct."
		except ValueError:
			return str(inputanswer) + " is not a vaild input."

class Timestb_TesterGUI:
	def __init__(self, parent):

		""" Interface """
		self.questions = Timestable()

		self.question_label = Label(parent, text = f"{str(self.questions.randnum)} * {str(self.questions.randnum1)}")
		self.question_label.grid(row = 0, column = 0)

		self.entrypoint = Entry(parent, width = 5)
		self.entrypoint.grid(row = 0, column = 1)

		Bt1 = Button(parent, text = "Check Answer", command = self.check_answer)
		Bt1.grid(row = 1, column = 0, padx = 40)

		Bt2 = Button(parent, text = "Next", command = self.next)
		Bt2.grid(row = 1, column = 1, padx = 40)

		self.outputlabel = Label(parent, text = "", font = ("Comic Sans MS", "10", "bold"))
		self.outputlabel.grid(row = 2, columnspan = 2)

	def next(self):
		self.questions = Timestable()
		self.question_label.configure(text = f"{str(self.questions.randnum)} * {str(self.questions.randnum1)}")
		self.entrypoint.delete(0, END)

	def check_answer(self):
		self.outputlabel.configure(text = self.questions.vaildate(self.entrypoint.get()))
#main routine
if __name__ == "__main__": 
	root = Tk()
	timestb_tester = Timestb_TesterGUI(root)
	root.mainloop()