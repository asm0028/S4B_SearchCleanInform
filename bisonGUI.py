import tkinter as tk

window = tk.Tk()

greeting_frame = tk.Frame(master=window, height=25)
greeting_frame.pack(fill=tk.X)

greeting_label = tk.Label(master=greeting_frame, text="Welcome to Search-Clean-Inform!")
greeting_label.pack()


species_entry_frame = tk.Frame(master=window)
species_entry_frame.pack(fill=tk.X)

species_entry = tk.Entry(master=species_entry_frame)
species_entry.insert(0, "Ex: Bison bison")
species_entry.pack()

species_name = species_entry.get()
print(species_name)

window.mainloop()
