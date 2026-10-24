import tkinter as tk
import tkinter.font as tfont

window = tk.Tk()
window.title("My Application")

label = tk.Label(
    text="Hello this is from label",
    font=("Times New Roman", 20, "bold")
)

custom_font = tfont.Font(
    family="Times New Roman",
    size=15,
    slant="italic"
)

label1 = tk.Label(
    text="from the custom font",
    font=custom_font
)

label2 = tk.Label(text="Hello")

window.minsize(width=800, height=600)

label.pack()
label1.pack()
label2.pack()

label.config(font=("Courier New", 25, "underline"))

window.mainloop()