import tkinter

# functions
def button_click():
    new_text = input.get()
    my_label.config(text=new_text)

# initialize tkinter window
window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="This is old text", font=("Arial", 24, "normal"))
my_label.config(text='This is new text')
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# buttons
button = tkinter.Button(text='button', command=button_click)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)
new_button = tkinter.Button(text='button', command=button_click)
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)

# entry component -- input field
input = tkinter.Entry(width=10)
input.get()
input.grid(column=3, row=2)



# put mainloop on bottom to end the GUI
window.mainloop()
