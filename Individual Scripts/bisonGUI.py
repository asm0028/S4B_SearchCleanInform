from tkinter import *

class BisonGUI:
    def __init__(self, master):
        self.master = master
        master.title("Search-Clean-Inform")

        self.species_name = ""

        self.label = Label(master, text="Welcome to Search-Clean-Inform")
        self.label.grid(columnspan=2)

        self.species_entry = Entry(master, text = "Example: Bison bison")
        self.species_entry.grid(row=1)
        self.species_entry.focus_set()

        self.go_button = Button(master, text = "Go!", command=self.go_button)
        self.go_button.grid(row=1, column=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, columnspan=2)

    def go_button(self):
        self.species_name = self.species_entry.get()
        #print(self.species_name)
        root.destroy()


root = Tk()
bison_gui = BisonGUI(root)
root.mainloop()


species_name = bison_gui.species_name

print(species_name)
