import tkinter

FONT = ('Arial', 14, 'normal')

# functions
def mile_to_km():
    miles = float(to_convert.get())
    km = round((miles*1.609),2)
    conversion_box.config(text=f"{km}")
# initialize window
window=tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)
# widget-grid (1,0)
to_convert = tkinter.Entry(width=10)
to_convert.grid(column=1, row=0)
# widget-grid (2,0)
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)
# widget-grid (0,1)
is_equal_to_label = tkinter.Label(text='is equal to', font=FONT)
is_equal_to_label.grid(column=0, row=1)
# widget-grid (1,1)
conversion_box = tkinter.Label()
conversion_box.grid(column=1,row=1)
# widget-grid (2,1)
km_label = tkinter.Label(text='KM')
km_label.grid(column=2, row=1)
# widget-grid(1,2)
calculate_btn = tkinter.Button(text='Calculate', command=mile_to_km)
calculate_btn.grid(column=1, row=2)

# end mainloop
window.mainloop()
