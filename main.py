import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title('Window')
root.geometry('400x300')


label = ttk.Label(root, text='Label 1')

label.pack(expand=True, fill='both')


# run
root.mainloop()
