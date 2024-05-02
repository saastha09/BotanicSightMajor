import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Define the parameters
input_shape = (150, 150, 3)  # Input image dimensions
num_classes = len(os.listdir('content'))  # Number of classes

# Data generator for training
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # Normalize pixel values to [0, 1]
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Create a Keras Sequential model+
model = Sequential()

# Add convolutional layers
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))  # <--- This was missing a closing parenthesis


model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the feature maps to a 1D array
model.add(Flatten())

# Fully connected layers
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))  # Add dropout for regularization

model.add(Dense(num_classes))  # Output layer with one neuron per class
model.add(Activation('softmax'))  # Softmax activation for classification

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Create data generators
batch_size = 32
train_generator = train_datagen.flow_from_directory(
    'content',  # Path to your data folder
    target_size=(input_shape[0], input_shape[1]),
    batch_size=batch_size,
    class_mode='categorical'
)

# Train the model
epochs = 10  # Number of training epochs
model.fit(train_generator, epochs=epochs)

# Save the trained model
model.save('image_classifier_model.h5')

# To make predictions on new images, you can use the model.predict() function.

# Example of loading an image and making predictions
img = load_img('326.jpeg', target_size=(input_shape[0], input_shape[1]))
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Reshape to (1, input_shape[0], input_shape[1], 3)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

# Make predictions
predictions = model.predict(img_array)
class_index = np.argmax(predictions)
class_name = os.listdir('content')[class_index]

print(f'The image is classified as: {class_name}')
