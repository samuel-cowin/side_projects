from tensorflow import keras

def change_rate(arg, rate=2, direction=True):
    if direction:
        return arg*rate
    else:
        return arg/rate

class HandwritingNN(keras.Model):
    def __init__(self, units=128, filters=64, act_layer='relu', act_class='softmax', pad='same', **kwargs):
        super().__init__(**kwargs)
        self.main_layers = [
            keras.layers.Conv2D(filters, 7, activation="relu",
                        padding="same", input_shape=[28, 28, 1]),
            keras.layers.MaxPooling2D(2),
            keras.layers.Conv2D(change_rate(filters), 3, activation=act_layer, padding=pad),
            keras.layers.BatchNormalization(),
            keras.layers.Conv2D(change_rate(filters), 3, activation=act_layer, padding=pad),
            keras.layers.BatchNormalization(),
            keras.layers.MaxPooling2D(2),
            keras.layers.Conv2D(change_rate*(filters, 4), 3, activation=act_layer, padding=pad),
            keras.layers.BatchNormalization(),
            keras.layers.Conv2D(change_rate(filters, 4), 3, activation=act_layer, padding=pad),
            keras.layers.BatchNormalization(),
            keras.layers.MaxPooling2D(2),
            keras.layers.Flatten(),
            keras.layers.Dense(units, activation=act_layer),
            keras.layers.BatchNormalization(),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(change_rate(units, 2, False), activation=act_layer),
            keras.layers.BatchNormalization(),
            keras.layers.Dense(10, activation=act_class)
        ]

    def call(self, input_):
        Z = input_
        for layer in self.main_layers:
            Z = layer(Z)
        return Z
