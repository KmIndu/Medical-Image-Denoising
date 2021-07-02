import cv2
import numpy as np


class DataGen:
    def __init__(self, path, batch_size, target_size):
        self.path = path
        self.batch_size = batch_size
        self.target_size = target_size

    def getImage(self, imPath):
        img = cv2.imread(imPath, 0)
        return img

    def rescale(self, img):
        x = img / 255.0
        return x

    def resize(self, img):
        x = cv2.resize(img, self.target_size, interpolation=cv2.INTER_CUBIC)
        x = np.reshape(x, (64, 64, 1))
        return x

    def addNoise(self, img, noise_factor, mu=0.0, sigma=1.0):
        img += noise_factor * np.random.normal(mu, sigma, size=img.shape)
        img = np.clip(img, 0.0, 1.0)
        return img

    def generate(self):
        import os

        files = os.listdir(self.path)
        while True:
            batch_paths = np.random.choice(a=files, size=self.batch_size)
            batch_input = []
            batch_output = []
            for input_path in batch_paths:
                img = self.getImage(self.path + input_path)
                img = self.rescale(img)
                img = img.astype(np.float)
                output = self.resize(img)
                img = self.addNoise(img, 0.1)
                img = self.resize(img)
                batch_input += [img]
                batch_output += [output]

            batch_x = np.array(batch_input)
            batch_y = np.array(batch_output)

            yield batch_x, batch_y