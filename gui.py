import tkinter as tk

def getResults(entry):
    print(entry.get())

root = tk.Tk()

w = tk.Label(root, text="What stock are you looking for?")
w.pack()

symbol = tk.Entry(root)
symbol.pack()
symbol.focus_set()

b = tk.Button(root, text="Go", command=lambda: getResults(symbol))
b.pack(side="right")

root.mainloop()
