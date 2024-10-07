import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
#TensorFlow is installed and working correctly, as indicated by the version number 2.17.0. The messages about oneDNN custom operations are just informational and not errors. They inform you that TensorFlow is using oneDNN optimizations, which might cause slight numerical differences due to floating-point round-off errors.

# Set directories for training and validation data
train_dir = 'data/train/'
validation_dir = 'data/validation/'

# Data augmentation and rescaling for training data
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, zoom_range=0.2)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir, target_size=(150, 150), batch_size=32, class_mode='binary')
validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size=(150, 150), batch_size=32, class_mode='binary')

# Building the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Binary classification (Hyacinth/Non-Hyacinth)
])

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Save model after each epoch if it improves
checkpoint = ModelCheckpoint('hyacinth_detection_model.h5', monitor='val_loss', save_best_only=True)

# Train model
history = model.fit(train_generator, epochs=10, validation_data=validation_generator, callbacks=[checkpoint])
