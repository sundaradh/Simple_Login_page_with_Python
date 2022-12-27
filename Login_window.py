#Simple Login Page with Python

from tkinter import *
from tkinter import messagebox

#create login class
class Login:
          key = 'awmrit' #this is th password
          def __init__(self, master):

                    #create the frame
                    self.frame = Frame(master)
                    self.frame.pack()

                    #create the label
                    self.label = Label(self.frame, text = 'Enter the password')
                    self.label.pack()

                    #create the entry
                    self.entry = Entry(self.frame, show = '*')
                    self.entry.pack()

                    #create the button
                    self.button = Button(self.frame, text = 'Login', command = self.check)
                    self.button.pack()

          def check(self):
                    if self.entry.get() == self.key:
                              self.new_window()
                    else:
                              messagebox.showerror('Error', 'Incorrect password')

          def new_window(self):
                    self.new = Toplevel(root)
                    self.app = App(self.new)

class App:
          def __init__(self, master):
                    self.master = master
                    self.frame = Frame(self.master)
                    self.frame.pack()

                    self.button = Button(self.frame, text = 'Quit', command = self.close_window)
                    self.button.pack()

          def close_window(self):
                    self.master.destroy()

root = Tk()
root.title('Login')
root.geometry('700x300')
app = Login(root)
root.mainloop()

