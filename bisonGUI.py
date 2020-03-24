import tkinter

window = tkinter.Tk()

greeting = tkinter.Label(text="Welcome to Search-Clean-Inform!")
entry = tkinter.Entry()
entry.insert(0, "Ex: Bison bison")

greeting.pack()
entry.pack()

species_name = entry.get()
print(species_name)

window.mainloop()
