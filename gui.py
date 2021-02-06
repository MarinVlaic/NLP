import tkinter as tk
from model import ai
import random


class CustomMessageBox(tk.Toplevel):

    def __init__(self, parent, generated, image):
        super().__init__()
        self.base = tk.Toplevel(parent)
        self.base.title("Trumped")
        self.base.geometry("800x450")
        self.background = tk.Label(self.base, image=image, bd=0)
        self.background.pack(fill='both', expand=True)
        self.background.image = image

        self.label = tk.Label(self.background, text=generated)
        self.ok = tk.Button(self.background, text="Trump approves", command=self.base.destroy)
        self.label.pack()
        self.ok.pack()


def click(top, topic, temperature, length, angry, happy):
    generated = ai.generate_one(prompt=topic, max_length=length, temperature=temperature)
    sentiment = (lambda x: x)(random.randint(0, 1))
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

name_label = tk.Label(background, text="Topic")
name_label.grid(row=1, column=1, sticky='news')

entry = tk.Entry(background)  # the Entry will let the user entre text inside the text box
entry.grid(row=1, column=2)

slider_label = tk.Label(background, text="Temperature")
slider_label.grid(row=2, column=1)

slider = tk.Scale(background, from_=0.5, to=2, resolution=0.1, orient=tk.HORIZONTAL)
slider.grid(row=2, column=2)

length = tk.Scale(background, from_=1, to=100, orient=tk.HORIZONTAL)
length.grid(row=4, column=2)

length_label = tk.Label(background, text="Tweet length")
length_label.grid(row=4, column=1)


butt = tk.Button(background, text="Trump it!", command=lambda: click(top, entry.get(), slider.get(), length.get(), angry, happy))
butt.grid(row=5, column=2)

top.mainloop()
