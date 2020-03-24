import tkinter as tk

window = tk.Tk()
window.title("Search-Clean-Inform")

greeting_frame = tk.Frame(master=window, height=25)
greeting_frame.grid(row=0, column=0)

greeting_label = tk.Label(master=greeting_frame, text="Welcome to Search-Clean-Inform!")
greeting_label.grid(row=0, column=0)


species_entry_frame = tk.Frame(master=window)
species_entry_frame.grid(row=1, column=0)

species_label = tk.Label(master=species_entry_frame, text = "Please enter the scientific name of your species of interest:")
species_label.grid(row=0, column=0)

species_entry = tk.Entry(master=species_entry_frame)
species_entry.insert(0, "Ex: Bison bison")
species_entry.grid(row=0, column=1)

go_button_frame = tk.Frame(master=window, relief=tk.RAISED)
go_button_frame.grid(row=2, column=0)

go_button = tk.Button(master=go_button_frame, text = "Go!")
go_button.grid(row=0, column=0)


species_name = species_entry.get()
print(species_name)

window.mainloop()
