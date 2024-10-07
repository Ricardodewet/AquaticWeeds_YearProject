import cv2
import tensorflow as tf
from dronekit import connect
from utils.gps_utils import calculate_gps_from_angle

# Load the trained model
model = tf.keras.models.load_model('hyacinth_detection_model.h5')

# Connect to the drone
drone = connect('127.0.0.1:14550', wait_ready=True)

# Open video stream from the drone (adjust the source as needed)
video_stream = cv2.VideoCapture(0)

if not video_stream.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Read a frame from the video stream
    ret, frame = video_stream.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Preprocess frame for model input
    input_frame = cv2.resize(frame, (150, 150))  # Ensure this matches your model's input size
    input_frame = input_frame / 255.0  # Normalize to [0, 1]
    input_frame = input_frame.reshape((1, 150, 150, 3))

    # Perform prediction
    prediction = model.predict(input_frame)

    # If hyacinth is detected (assuming binary output from model)
    if prediction[0][0] > 0.5:  # Adjust based on your model's output shape
        # Calculate GPS coordinates of detected patch
        gps_coords = calculate_gps_from_angle(drone, frame)
        
        # Mark patch on the frame (draw a rectangle)
        cv2.putText(frame, f'Hyacinth detected at {gps_coords}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display video stream with detection
    cv2.imshow('Drone Feed', frame)

    # Break loop on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_stream.release()
cv2.destroyAllWindows()
