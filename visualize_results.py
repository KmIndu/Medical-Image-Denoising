import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import tkinter as tk



def visualize_results(r, z):
    img1 = r[0][:, :, 0]
    img2 = r[1][:, :, 0]
    img3 = r[2][:, :, 0]
    img4 = r[3][:, :, 0]
    img5 = r[4][:, :, 0]

    def_img1 = z[0][:, :, 0] * 255.
    def_img2 = z[1][:, :, 0] * 255.
    def_img3 = z[2][:, :, 0] * 255.
    def_img4 = z[3][:, :, 0] * 255.
    def_img5 = z[4][:, :, 0] * 255.

    fig = plt.figure(figsize=(20., 10.))
    grid = ImageGrid(fig, 111, nrows_ncols=(2, 5), axes_pad=0.1, )

    for ax, im in zip(grid, [img1, img2, img3, img4, img5, def_img1, def_img2, def_img3, def_img4, def_img5]):
        ax.imshow(im, cmap="gray")

    plt.show()
    print("Visualised Result Successfully")
    tk.Label(text="Visualised Result Successfully", width=40, height=2).place(relx=0.6, rely=0.8)
