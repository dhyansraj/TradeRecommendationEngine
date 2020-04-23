import tensorflow as tf
import dataset_manager as dm
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

pixels, labels, dates = dm.get_dataset()

train_pixels, test_pixels = pixels[:30000], pixels[30000:]
train_labels, test_labels = labels[:30000], labels[30000:]


# print(pixels.shape)

# print(labels.shape)

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="tanh"),
        tf.keras.layers.Dense(2),
    ]
)

predictions = model(train_pixels[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(train_labels[:1], predictions).numpy()

model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

model.fit(train_pixels, train_labels, epochs=5)

model.evaluate(test_pixels, test_labels, verbose=2)
