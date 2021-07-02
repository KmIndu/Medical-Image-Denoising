import tkinter as tk
import seaborn as sns
sns.set()
import tensorflow as tf

class callback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('loss') < 0.23 and logs.get('val_loss') < 0.23:
            print("\nStopping training.....\n")
            self.model.stop_training = True


def autoencoder(train_gen, test_gen):
    myCallback=callback()
    autoencoder = tf.keras.models.Sequential([

        tf.keras.layers.Conv2D(64, (3, 3), input_shape=(64, 64, 1), activation="relu", padding="same", data_format="channels_last"),

        tf.keras.layers.MaxPool2D(padding="same"),

        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),

        tf.keras.layers.MaxPool2D(padding="same"),

        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),

        tf.keras.layers.UpSampling2D(),

        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),

        tf.keras.layers.UpSampling2D(),

        tf.keras.layers.Conv2D(1, (3, 3), activation="sigmoid", padding="same")

    ])
    autoencoder.summary()
    autoencoder.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
    hist = autoencoder.fit(train_gen, epochs=10, steps_per_epoch=16, validation_data=test_gen, validation_steps=10,
                           callbacks=[myCallback])
    print("Medical Images Denoised Successfully")
    tk.Label(text="Medical Images Denoised Successfully", width=40, height=2).place(relx=0.6,rely=0.5)
    return autoencoder, hist