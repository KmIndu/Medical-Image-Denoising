import matplotlib.pyplot as plt
import tkinter as tk



def samples_plt(hist):
    plt.ylabel("Loss")
    plt.xlabel("epochs")

    plt.plot(hist.history["loss"], label="Training Loss")
    plt.plot(hist.history["val_loss"], label="Validation Loss")
    plt.legend()
    plt.show()
    print("Plotted Successfully")
    tk.Label(text="Plotted Successfully", width=40, height=2).place(relx=0.6, rely=0.6)