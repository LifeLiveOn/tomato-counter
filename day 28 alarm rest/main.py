from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 5
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTime():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_lbl.config(text="Time reminder")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's the 1st/3rd/5th/7th rep
    if reps % 8 == 0:
        Timer_lbl.config(text="LONG BREAK", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        Timer_lbl.config(text="short break", fg=GREEN)
        count_down(short_break_sec)
    else:
        Timer_lbl.config(text="Work Bitch", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds <= 9 and "0" not in str(seconds):
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_secssion = math.floor(reps / 2)
        for _ in range(work_secssion):
            mark += "✓"
        check_mrk.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("take your rest app")
window.config(padx=100, pady=50, bg="#f7f5dd")

# this is for the label
Timer_lbl = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
Timer_lbl.grid(column=2, row=0)

# canvas of the tomato
canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

# timer
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

# function to show the green tick
check_mrk = Label(text="✓", bg=YELLOW, fg=GREEN, font=("Courier", 30))
check_mrk.grid(column=2, row=3)

# button_start
start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
start_btn.grid(column=0, row=2)

# button_end                   
start_end = Button(text="End", command=resetTime, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
start_end.grid(column=3, row=2)
window.mainloop()
