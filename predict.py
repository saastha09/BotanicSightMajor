import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import sys

def load_and_preprocess_image(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(224, 224))  # Adjust target size as needed
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image_class(image_path, model_path):
    # Load the model
    model = tf.keras.models.load_model(model_path)

    # Load and preprocess the image
    img_array = load_and_preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    return class_index

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python predict.py <image_path> <model_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    model_path = sys.argv[2]

    predicted_class = predict_image_class(image_path, model_path)
    print("Predicted class index:", predicted_class)
