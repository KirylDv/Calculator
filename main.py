from tkinter import *
from tkinter.ttk import *
from functools import partial

def init_root():
	global root
	root = Tk()
	root.title("Калькулятор")
	root.geometry("300x145")
	root.resizable(False, False)

class Calc():
	def __init__(self):
		super(Calc, self).__init__()
		self.main_label = Label(root, text="0")
		self.buff_label = Label(root, text="0")
		self.result = 0.0
		self.bts = [str(i) for i in range(10)] + ["+", "-", "*", "/", ".", "=", "C"]
		self.comm = ""
		self.operators = { "+": lambda a, b: a + b,
						   "-": lambda a, b: a - b,
						   "*": lambda a, b: a * b,
						   "/": lambda a, b: a / b}
		self.buttons = [Button(root, text=i, command=partial(self.click_calculate, self=self, btn=i)) for i in self.bts]

	def click_calculate(event, self, btn):
		if btn == "C":
			self.main_label.config(text="0")
			self.buff_label.config(text="0")
			self.comm = ""
			self.result = 0.0
		if btn.isnumeric() or (btn == "." and "." not in self.main_label["text"]):
			if(self.main_label["text"] == "0"):
				self.main_label.config(text=btn)
			else:
				self.main_label.config(text=self.main_label["text"]+btn)
		if btn in "+-*/=":
			if btn == "=" and self.comm == "":
				pass
			else:
				temp = float(self.main_label["text"])
				self.main_label.config(text="")
				if self.comm != "":
					self.result = self.operators[self.comm](self.result, temp)
				else:
					self.result = temp
				self.comm = btn if btn != "=" else ""
				self.buff_label.config(text=str(round(self.result, 9)))
				self.main_label.config(text="0")

	def init_calc(self):
		self.main_label.grid(row=0, column=0, columnspan=4)
		self.buff_label.grid(row=1, column=1, columnspan=3)
		self.buttons[0].grid(row=5, column=0)
		self.buttons[1].grid(row=4, column=0)
		self.buttons[2].grid(row=4, column=1)
		self.buttons[3].grid(row=4, column=2)
		self.buttons[4].grid(row=3, column=0)
		self.buttons[5].grid(row=3, column=1)
		self.buttons[6].grid(row=3, column=2)
		self.buttons[7].grid(row=2, column=0)
		self.buttons[8].grid(row=2, column=1)
		self.buttons[9].grid(row=2, column=2)
		self.buttons[10].grid(row=2, column=3)
		self.buttons[11].grid(row=3, column=3)
		self.buttons[12].grid(row=4, column=3)
		self.buttons[15].grid(row=5, column=2)
		self.buttons[14].grid(row=5, column=1)
		self.buttons[13].grid(row=5, column=3)
		self.buttons[16].grid(row=1, column=0)


def main():
	init_root()
	calc = Calc()
	calc.init_calc()
	root.mainloop()

if __name__ == "__main__":
	main()