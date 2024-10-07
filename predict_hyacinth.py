from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = load_model('hyacinth_detection_model.h5')

# Path to the image for prediction
image_path = 'path_to_image.jpg'  # Replace with the path to your image

# Preprocess the image
img = load_img(image_path, target_size=(150, 150))  # Resize image to match model input size
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
img_array /= 255.0  # Normalize pixel values

# Make a prediction
prediction = model.predict(img_array)

# Output the result
if prediction > 0.5:
    print("Hyacinth detected!")
else:
    print("No hyacinth detected.")
