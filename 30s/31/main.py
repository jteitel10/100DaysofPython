from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
french_dict = {}

# ------------------------------ DATA FILE ----------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")
else:
    french_dict = data.to_dict(orient="records")


# ------------------------ RANDOM WORD SELECTION ----------------------------- #
def random_word():
    global current_word, time_to_flip
    window.after_cancel(time_to_flip)
    current_word = random.choice(french_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    time_to_flip = window.after(3000, func=flip_card)

# ----------------------------- FLIP CARD ------------------------------------ #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

# ---------------------------- KNOWS WORD ------------------------------------ #
def knows_word():
    french_dict.remove(current_word)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()
# ---------------------------- USER INTERFACE -------------------------------- #
window = Tk()
window.title("Flash Cards: French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# time flipping variable
time_to_flip = window.after(3000, func=flip_card)

# canvas the image
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263,image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# button images
unkown_img = PhotoImage(file="images/wrong.png")
known_img = PhotoImage(file="images/right.png")

# buttons
unkown_btn = Button(image=unkown_img, highlightthickness=0, command=random_word)
unkown_btn.grid(column=0, row=1)
known_btn = Button(image=known_img, highlightthickness=0, command=knows_word)
known_btn.grid(column=1, row=1)

# call card function to start with translations
random_word()

# end of window
window.mainloop()
