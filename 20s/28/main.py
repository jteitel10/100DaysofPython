import tkinter
import math

# ----------------------------- CONSTANTS ----------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ------------------------------ TIMER RESET --------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer', fg=GREEN)
    check_mrk.config(text="")
    global reps
    reps = 0

# ----------------------------- TIMER MECHANISM ------------------------------ #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # break section
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text='Break', fg = RED)
    # break section
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text='Break', fg = PINK)
    # work section
    else:
        countdown(work_sec)
        timer_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM --------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = '0' + str(count_sec)
    if len(str(count_min)) == 1:
        count_min = '0' + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks=""
        for _ in range(work_sessions):
            marks += '✓'
        check_mrk.config(text=marks)

# --------------------------------- UI SETUP --------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = tkinter.Label(text='Timer',bg=YELLOW,fg=GREEN, font = (FONT_NAME, 36, 'normal'))
timer_label.grid(column=1,row=0)

canvas = tkinter.Canvas(window,width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)

timer_text = canvas.create_text(103, 140, text="00:00", fill='white', font=(FONT_NAME, 36, 'bold'))
canvas.grid(column=1,row=1)

start_btn = tkinter.Button(text='Start',bg=YELLOW,highlightthickness=0, command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = tkinter.Button(text='Reset',bg=YELLOW,highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2,row=2)

check_mrk = tkinter.Label(text='✓', bg=YELLOW, fg=GREEN)
check_mrk.grid(column=1,row=3)

window.mainloop()
