from tkinter import *
from tkinter import messagebox
from playsound import playsound

# Constants
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1  # if timer in minutes use this
SECONDS = WORK_MIN * 60  # if timer in seconds use this, but first remove work_min from here
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
AUDIO = 'audio.mp3'
reps = 0
lifeblood = None


# Functions
def start_timer():
    global reps
    reps += 1
    with open("data.txt", mode="a") as data:
        data.write(str(reps) + "\n")
    if reps < 5:
        countdown(SECONDS)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def countdown(time_seconds):
    minute_text = int(time_seconds / 60)
    second_text = int(time_seconds % 60)
    a = minute_text
    b = second_text

    if minute_text < 10:
        a = "0" + str(int(time_seconds / 60))
    if second_text < 10:
        b = "0" + str(int(time_seconds % 60))
    canvas.itemconfig(timer, text=f"{a}:{b}")

    # most important part - recursion; lifeblood of function
    if time_seconds > 0:
        global lifeblood
        lifeblood = window.after(1000, countdown, time_seconds - 1)
    else:
        mark = ""
        for _ in range(reps):
            mark += "✔"
        check_marks.config(text=mark)
        playsound(AUDIO)
        answer = messagebox.askyesno("Question", "Do you want to start the next Pomodoro?")
        if answer:
            start_timer()
        else:
            return


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Instances
window = Tk()
window.title("POMODORO")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20, bg=YELLOW)

label = Label(text=" Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(column=0, row=0, padx=(20, 1))

tomato = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0, row=1, columnspan=2, padx=(80, 1), pady=(10, 30))

start_button = Button(text="Start", highlightthickness=0, command=start_timer, width=10, height=1,
                      font=(FONT_NAME, 15, "bold"))
# in command i can also use lambda function if i want to run a function with some arguments
# by doing-  command= lambda: my_function(arg1, arg2, arg3)
start_button.grid(column=0, row=2, padx=(60, 1))

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(column=0, row=3)

window.mainloop()
