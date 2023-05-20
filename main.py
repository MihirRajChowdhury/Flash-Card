from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")






def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer = window.after(3000, func=flip_card)


def remove_card():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0)
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
language_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))

canvas.config(background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
check_mark = Button(image=check_image, highlightthickness=0, command=remove_card)
check_mark.grid(column=1, row=1)
next_card()

window.mainloop()

