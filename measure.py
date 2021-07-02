import tkinter as tk


def measure(autoencoder, test_gen):
    r, f = next(test_gen)
    z = autoencoder.predict(r)
    var = z.shape
    print(var)
    print("Predicted Result Successfully")
    tk.Label(text="Predicted Result Successfully", width=40, height=2).place(relx=0.6, rely=0.7)
    return r, z
