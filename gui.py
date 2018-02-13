import tkinter as tk

def getResults(entry):
    print(entry.get())

def onEnter(entry):
    getResults(entry)

root = tk.Tk()
search = tk.Frame(root)
search.pack(side="top")

w = tk.Label(search, text="What stock are you looking for?")
w.pack(side="top")

symbol = tk.Entry(search)
symbol.pack(side="left")
symbol.focus_set()
symbol.bind("<Return>", lambda event: onEnter(symbol))

b = tk.Button(search, text="Go", command=lambda: getResults(symbol))
b.pack(side="right")

root.mainloop()
