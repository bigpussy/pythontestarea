# -*- coding: utf-8 -*-
print u"条件判断"
from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit', command = self.hello)
		self.quitButton.pack()
	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)
app = Application()

app.master.title('Hello world')
app.mainloop()

