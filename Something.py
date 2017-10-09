from tkinter import *

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title("Thermometerexchange")
		self.setup_gui()
			
	def setup_gui(self):
		self.entr()
		self.lbls()
		self.menu()
		self.k()
		
	def entr(self):	
		self.e_v = DoubleVar()
		self.e_b = IntVar()
		self.e = Entry(textvariable=self.e_v)
		self.e.grid(row=0, column=1)
		self.e2 = Entry(textvariable=self.e_b)
		self.e2.grid(row=2, column=1)
	
	def lbls(self):
		self.l = Label(text="in")
		self.l.grid(row=1, column=1)
	
	def menu(self):
		OPS = [
		"C",
		"F",
		"K"
		]
		
		self.ver = StringVar(self)
		self.ver.set(OPS[2])
		
		men = OptionMenu(self, self.ver, *OPS)
		men.grid(row=0, column=2)
		
		self.ver1 = StringVar(self)
		self.ver1.set(OPS[0])
		
		men1 = OptionMenu(self, self.ver1, *OPS)
		men1.grid(row=2, column=2)
	
	def k(self):
		self.after(20, self.k)
		try:
			if self.ver.get() == "K" and self.ver1.get() == "C":
					if int(self.e_v.get()) >= 0:
						self.e_b.set(float(self.e_v.get()) + -273.15)
		except TclError:
			pass
		try:
			if self.ver.get() == "K" and self.ver1.get() == "F":
					if int(self.e_v.get()) >= 0:
						self.e_b.set(float(self.e_v.get()) * 9/5 -459.67)
		except TclError:
			pass
		try:
			if self.ver.get() == "K" and self.ver1.get() == "K":
					if int(self.e_v.get()) >= 0:
						self.e_b.set(float(self.e_v.get()))
		except TclError:
			pass
		try:
			if self.ver.get() == "C" and self.ver1.get() == "F":
					if int(self.e_v.get()) >= -273.15:
						self.e_b.set(float(self.e_v.get()) * 9/5 + 32)
		except TclError:
			pass	
		try:
			if self.ver.get() == "C" and self.ver1.get() == "K":
					if int(self.e_v.get()) >= -273.15:
						self.e_b.set(float(self.e_v.get()) + 273.15)
		except TclError:
			pass
		try:
			if self.ver.get() == "C" and self.ver1.get() == "C":
					if int(self.e_v.get()) >= -273.15:
						self.e_b.set(float(self.e_v.get()))
		except TclError:
			pass
		try:
			if self.ver.get() == "F" and self.ver1.get() == "C":
					if int(self.e_v.get()) >= -459.67:
						self.e_b.set(float(self.e_v.get()) - 32 * 5/9)
		except TclError:
			pass
		try:
			if self.ver.get() == "F" and self.ver1.get() == "K":
					if int(self.e_v.get()) >= -459.67:
						self.e_b.set(float(self.e_v.get()) + 273.15 - 32 * 5/9)
		except TclError:
			pass			
		try:
			if self.ver.get() == "F" and self.ver1.get() == "F":
					if int(self.e_v.get()) >= -459.67:
						self.e_b.set(float(self.e_v.get()))
		except TclError:
			pass
		
root = App()
root.mainloop()