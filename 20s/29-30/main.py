from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ltr_list=[choice(letters) for _ in range(1, randint(10,14))]
    symb_list=[choice(symbols) for _ in range(1, randint(2,4))]
    num_list=[choice(numbers) for _ in range(1,randint(2,4))]

    pwd_list = ltr_list + symb_list + num_list
    shuffle(pwd_list)

    final_pwd = "".join(pwd_list)
    pwd_input.insert(0, final_pwd)
    pyperclip.copy(final_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    website = website_input.get().title()
    usr_name = usr_input.get()
    pswd = pwd_input.get()
    new_data = {
        website: {
            "username" : usr_name,
            "password":pswd,
            }
        }

    if len(website) == 0 or len(pswd) == 0 or len(usr_name) == 0:
        messagebox.showinfo(title='Error', message='Please make sure all fields are filled')
    else:
        try:
            with open ('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            # reset GUI fields
            website_input.delete(0,END)
            usr_input.delete(0,END)
            usr_input.insert(0,'user@email.com')
            pwd_input.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pwd():
    website = website_input.get()
    try:
        with open ('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
            if website in data:
                usr_info = data[website]['username']
                pwd_info = data[website]['password']
                messagebox.showinfo(title=website, message=f"Username: {usr_info}\nPassword: {pwd_info}")
            else:
                messagebox.showinfo(title="Error", message=f"No account info for {website.title()}.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# add the photo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)

# search Button
search_btn = Button(text="Search", width=14, command=find_pwd)
search_btn.grid(column=2, row=1, columnspan=2)

# email/username label and entry
usr_label = Label(text="Email/Username:")
usr_label.grid(column=0, row=2)
usr_input = Entry(width=35)
usr_input.grid(column=1, row=2, columnspan=2)
usr_input.insert(0,'user@email.com')

# password label and entry and generate button
pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)
pwd_input = Entry(width=21, show="*")
pwd_input.grid(column=1, row=3)
gen_pwd = Button(text='Generate Password', command=generate_password)
gen_pwd.grid(column=2, row=3, columnspan=1)

# add button
add_btn = Button(text='Add', width=36, command=save_pwd)
add_btn.grid(column=1, row=4, columnspan=2)

# end of window
window.mainloop()
