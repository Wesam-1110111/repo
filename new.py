import tkinter as tk
from random import randint

def rand_n():
	return randint(10)


print(f'this is a random number from 0 - 10: {rand_n()}')


# setups
root = tk.Tk(value=rand_n())
root.title('Window')
root.geometry('400x300+700+50')

randvar = tk.IntVar()

tk.Label(root, text='some text', textvariable=randvar).pack()


# run
root.mainloop()
