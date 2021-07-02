import seaborn as sns
sns.set()

import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk

from myglobals import myglobals

import load_data


def main():
    master = tk.Tk()
    master.title("Medical Image Denoising")
    image2 = PIL.Image.open('saved_model/backpic.jpg')
    image1 = ImageTk.PhotoImage(image2)
    background_label = tk.Label(master, image=image1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    master.geometry("1480x700+0+0")

    label = Label(master, text="          WELCOME TO MEDICAL IMAGE DENOISING TOOL!          ")
    label.config(font=("Arial", 34, "bold"))
    label.grid(row=0, column=0)

    tk.Button(text='Load Data', command=lambda: load_data.load_data(), width=25, height=2).place(relx=0.45, rely=0.2)
    mg = myglobals()
    tk.Button(text='Generate Train', command=lambda: mg.generate(), width=25, height=2).place(relx=0.45, rely=0.3)

    tk.Button(text='Generate Test', command=lambda: mg.generate_test(), width=25, height=2).place(relx=0.45, rely=0.4)

    tk.Button(text='Autoencoder', command=lambda: mg.autoencoder_call(), width=25, height=2).place(relx=0.45, rely=0.5)

    tk.Button(text='Plot', command=lambda: mg.samples_plt(), width=25, height=2).place(relx=0.45, rely=0.6)

    tk.Button(text='Predict Result', command=lambda: mg.measure(), width=25, height=2).place(relx=0.45, rely=0.7)

    tk.Button(text='Visualize Result', command=lambda: mg.visualize_results(), width=25, height=2).place(relx=0.45, rely=0.8)

    master.mainloop()


if __name__ == '__main__':
    main()
