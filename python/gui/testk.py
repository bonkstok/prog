#import tkinter as tk
from tkinter import * 

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		self.btnHi = Button(master, text='Hello', command=self.say_hi)
		self.btnHi.place(x=0,y=0)

	def say_hi(self):
		print("Hello")

      
   


def main():
	root = Tk()
	root.geometry('400x300')
	app = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()