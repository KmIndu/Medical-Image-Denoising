import os
import tkinter as tk
import cv2


def load_data():
    files = os.listdir("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images")
    files.remove("Info.txt")
    files.remove("Licence.txt")
    files.remove("README")

    os.mkdir("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/train")
    os.mkdir("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/test")

    for i in range(len(files)):
        x = cv2.imread("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/" + files[i])
        if i < round(0.6 * len(files)):
            cv2.imwrite("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/train/" + str(i) + ".png", x)
        else:
            cv2.imwrite("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/test/" + str(i) + ".png", x)
    print("Loaded Successfully")
    tk.Label(text="Loaded Successfully", width=40, height=2).place(relx=0.6, rely=0.2)
