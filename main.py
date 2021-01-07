from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ee9595"
RED = "#ef4f4f"
GREEN = "#3FB351"
YELLOW = "#ffcda3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

action_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
action_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=3)

mark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
mark_label.grid(row=3, column=1)


window.mainloop()