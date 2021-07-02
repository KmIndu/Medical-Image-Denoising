import tkinter as tk
from DataGen import DataGen
import autoencoder
import samples_plt
import visualize_results
import measure

class myglobals:

    autoencoder = None
    hist = None
    test_gen = None
    train_gen = None
    r = None
    z = None


    def generate(self):
        train = DataGen("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/train/", 16, (64, 64))
        self.train_gen = train.generate()
        print("Training Set Generated Successfully")
        tk.Label(text="Training Set Generated Successfully", width=40, height=2).place(relx=0.6, rely=0.3)

    def generate_test(self):
        test = DataGen("C:/Users/butol/PycharmProjects/Medical Image Denoising/Images/test/", 10, (64, 64))
        self.test_gen = test.generate()
        print("Testing Set Generated Successfully")
        tk.Label(text="Testing Set Generated Successfully", width=40, height=2).place(relx=0.6, rely=0.4)

    def autoencoder_call(self):
        self.autoencoder, self.hist = autoencoder.autoencoder(self.train_gen, self.test_gen)

    def samples_plt(self):
        samples_plt.samples_plt(self.hist)

    def measure(self):
        self.r, self.z = measure.measure(self.autoencoder,self.test_gen)

    def visualize_results(self):
        visualize_results.visualize_results(self.r, self.z)