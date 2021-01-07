from tkinter import *
import math

cycle = 0
timer = None
sound = True

PINK = "#ee9595"
RED = "#ef4f4f"
GREEN = "#3FB351"
LIGHT_GREEN = "#00CC66"
YELLOW = "#ffcda3"
BLACK = "#000000"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 4


def app_in_front():
    """
    lift our app in the foreground on the toplevel
    """
    app.attributes("-topmost", 1)
    app.attributes("-topmost", 0)
    if sound is True:
        app.bell()


def reset_timer():
    """
    triggers after reset button click, it'll enable back start button
    """
    app.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    action_label.config(text="Timer", fg=GREEN)
    mark_label.config(text="")
    start_button.config(state="active")


def start_button_click():
    """
    triggers after start button click, it'll disable start button and start countdown
    """
    start_button.config(state="disabled")
    start_timer()


def start_timer():
    """
    detects which phase is now (work / break) and call countdown with specific time
    """
    global cycle
    cycle += 1

    # work_seconds = WORK_MIN * 60
    # short_break_seconds = SHORT_BREAK_MIN * 60
    # long_break_minutes = LONG_BREAK_MIN * 60

    work_seconds = WORK_MIN
    short_break_seconds = SHORT_BREAK_MIN
    long_break_minutes = LONG_BREAK_MIN

    if cycle % 8 == 8:
        count_down(long_break_minutes)
        action_label.config(text="Break", fg=RED)
    elif cycle % 2 == 0:
        count_down(short_break_seconds)
        action_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        action_label.config(text="Work", fg=GREEN)


def count_down(count):
    """
    start countdown with given arg count
    :param count: time in seconds
    """
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = app.after(1000, count_down, count - 1)
    else:
        app_in_front()
        start_timer()
        if cycle != 0 and cycle % 2 == 0:
            mark_label["text"] += "✔"


def change_sound_state():
    global sound
    if sound is True:
        sound_button.config(text="🔇", bg=PINK, fg=BLACK)
        sound = False
    else:
        sound_button.config(text="🔊", bg=YELLOW, fg=BLACK)
        sound = True


app = Tk()
app.title("Pomodoro")
app.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

action_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
action_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_button_click)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
mark_label.grid(row=3, column=1)

sound_button = Button(text="🔊",
                      bg=YELLOW,
                      fg=BLACK,
                      font=(FONT_NAME, 10, "bold"),
                      command=change_sound_state,
                      highlightthickness=0)
sound_button.grid(row=4, column=1)

app.mainloop()