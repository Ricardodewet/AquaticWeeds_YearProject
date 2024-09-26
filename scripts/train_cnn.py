import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import json

# Load weather data from JSON (optional for further integration)
def load_weather_data(filepath='./data/weatherData.json'):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            weather_data = json.load(file)
        return weather_data
    else:
        print(f"No weather data found at {filepath}.")
        return None

# Function to integrate weather data and make predictions based on hyacinth detection
def predict_hyacinth_movement(weather_data, detected_patches):
    if weather_data and detected_patches:
        # Sample logic: Use wind speed/direction from weather data to predict movement
        wind_speed = weather_data.get("wind_speed", 0)
        wind_direction = weather_data.get("wind_direction", "N/A")
        
        # Implement simple heuristic to estimate movement
        movement_prediction = []
        for patch in detected_patches:
            # Example: Just for illustration, move patch based on wind
            new_position = {
                "x": patch["x"] + wind_speed * np.cos(np.radians(wind_direction)),
                "y": patch["y"] + wind_speed * np.sin(np.radians(wind_direction))
            }
            movement_prediction.append(new_position)

        return movement_prediction
    else:
        print("Insufficient data to predict movement.")
        return None

# Load and preprocess image data
data_dir = './data/'  # Directory where images are stored

# Create ImageDataGenerator with augmentations to preprocess the images
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,     # Randomly rotate images
    width_shift_range=0.2, # Randomly shift images horizontally
    height_shift_range=0.2,# Randomly shift images vertically
    shear_range=0.2,       # Shear transformations
    zoom_range=0.2,        # Random zoom
    horizontal_flip=True,  # Flip images horizontally
    fill_mode='nearest'    # Fill in missing pixels
)

# Split the data into training and validation sets
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training')

validation_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation')

# Build a Convolutional Neural Network (CNN) for hyacinth detection
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Optionally load weather data (to later integrate with CNN predictions if required)
weather_data = load_weather_data()

if weather_data:
    print("Weather data successfully loaded.")
    # Further integration of weather data can be done here

# Train the CNN model
history = model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

# Save the trained model to disk
model_save_path = './models/hyacinth_detection_model.h5'
model.save(model_save_path)

print(f"Model training complete and saved at {model_save_path}.")

# Optional: Evaluate model performance (if validation data available)
val_loss, val_accuracy = model.evaluate(validation_generator)
print(f"Validation loss: {val_loss}, Validation accuracy: {val_accuracy}")

# Example: Use the trained model to detect hyacinth patches (dummy example, replace with actual detection logic)
detected_patches = [{"x": 10, "y": 20}, {"x": 30, "y": 40}]  # Replace with actual detection results

# Predict hyacinth movement based on weather data
movement_predictions = predict_hyacinth_movement(weather_data, detected_patches)
if movement_predictions:
    print("Predicted hyacinth movements:")
    for i, movement in enumerate(movement_predictions):
        print(f"Patch {i + 1} will move to new position: {movement}")
