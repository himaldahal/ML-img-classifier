import concurrent.futures
import numpy as np
import PIL.Image
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("model.h5")

# Create a function to classify an image
def classify_image(image_data):
    # Convert the image data to a NumPy array
    image = np.array(PIL.Image.open(image_data))
    # Preprocess the image for the model
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    # Use the model to classify the image
    prediction = model.predict(image)
    # Get the class label with the highest probability
    class_index = np.argmax(prediction)
    class_label = class_labels[class_index]
    return class_label

# Create a thread pool with 4 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit a classification task for each image in the list
    for image_data in image_list:
        future = executor.submit(classify_image, image_data)

print("Finished classifying images")
