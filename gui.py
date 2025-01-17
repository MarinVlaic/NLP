import tkinter as tk
from model import ai
import random
from sentiment import sid


class CustomMessageBox:

    def __init__(self, parent, generated, image):
        self.base = tk.Toplevel(parent)
        self.base.title("Trumped")
        self.base.geometry("800x450")
        self.background = tk.Label(self.base, image=image, bd=0)
        self.background.pack(fill='both', expand=True)
        self.background.image = image

        self.label = tk.Label(self.background, text=generated, font=("TkTextFont"), wraplength=600, justify="center")
        self.ok = tk.Button(self.background, text="Trump approves", font=("TkTextFont", 15, "bold"), command=self.base.destroy)
        self.ok.pack(side="bottom")
        self.label.pack(side="bottom")




def click(top, topic, temperature, length, angry, happy):
    generated = ai.generate_one(prompt=topic, max_length=length, temperature=temperature)
    sentiment = sid.polarity_scores(generated)
    sentiment = 0 if sentiment['neg'] > sentiment['pos'] else 1
    if sentiment == 0:
        msg = CustomMessageBox(top, generated, angry)
    else:
        msg = CustomMessageBox(top, generated, happy)

top = tk.Tk()
top.title("Trumpifizer")

top.geometry('720x720')

trump = tk.PhotoImage(file="images/trump.png")
angry = tk.PhotoImage(file="images/angry.png")
happy = tk.PhotoImage(file="images/happy.png")

trump = trump.subsample(1, 1)
angry = angry.subsample(1, 1)
happy = happy.subsample(1, 1)

background = tk.Label(top, image=trump, bd=0)
background.pack(fill='both', expand=True)
background.image = trump

# resize empty rows, columns to put other elements in center
background.rowconfigure(0, weight=100)
background.rowconfigure(10, weight=100)
background.columnconfigure(0, weight=100)
background.columnconfigure(3, weight=100)

name_label = tk.Label(background, text="Topic", font=("TkTextFont", 17, "bold"))
name_label.grid(row=1, column=1, sticky='news')

entry = tk.Entry(background)  # the Entry will let the user entre text inside the text box
entry.grid(row=1, column=2)

slider_label = tk.Label(background, text="Temperature", font=("TkTextFont", 17, "bold"))
slider_label.grid(row=2, column=1)

slider = tk.Scale(background, from_=0.5, to=2, resolution=0.1, orient=tk.HORIZONTAL, font=("TkTextFont", 13, "italic"))
slider.grid(row=2, column=2)
slider.set(1)

length = tk.Scale(background, from_=1, to=100, orient=tk.HORIZONTAL, font=("TkTextFont", 13, "italic"))
length.grid(row=4, column=2)
length.set(30)

length_label = tk.Label(background, text="Tweet length", font=("TkTextFont", 17, "bold"))
length_label.grid(row=4, column=1)


butt = tk.Button(background, text="Trump it!", font=("TkTextFont", 14, "bold"), command=lambda: click(top, entry.get(), slider.get(), length.get(), angry, happy))
butt.grid(row=5, column=2)


top.mainloop()
