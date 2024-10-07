from pymavlink import mavutil
import cv2  # OpenCV for image capture
import time
import numpy as np
import tensorflow as tf

class DroneInterface:
    def __init__(self, connection_string, model_path):
        """Initialize the connection to the drone and load the detection model."""
        # Connect to the MAVLink drone
        self.master = mavutil.mavlink_connection(connection_string)
        self.master.wait_heartbeat()
        print("Connected to the drone")

        # Load the trained detection model
        self.model = tf.keras.models.load_model(model_path)

        # Drone parameters
        self.altitude = 100  # Example altitude in meters; set as required
        self.image_width = 640  # Width of the camera frame
        self.image_height = 480  # Height of the camera frame
        self.fov_angle = 90  # Example horizontal FOV in degrees

    def capture_image(self, save_path="captured_images/"):
        """Capture an image from the drone's camera."""
        cap = cv2.VideoCapture(0)  # Replace with your camera ID
        ret, frame = cap.read()

        if ret:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_filename = f"{save_path}image_{timestamp}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image saved to {image_filename}")
            return frame  # Return the captured frame for processing
        else:
            print("Failed to capture image")
            return None

    def get_gps_coordinates(self):
        """Retrieve the GPS coordinates of the drone."""
        msg = self.master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        lat = msg.lat * 1e-7
        lon = msg.lon * 1e-7
        alt = msg.alt * 1e-3  # Convert to meters
        return lat, lon, alt

    def calculate_patch_coordinates(self, lat, lon, alt, detected_patch_coords):
        """Calculate GPS coordinates of detected patches based on drone position."""
        # Assuming detected_patch_coords is a list of tuples (x, y)
        gps_coords = []
        
        # Calculate scale based on altitude and FOV
        scale = alt / (2 * np.tan(np.radians(self.fov_angle / 2)))

        for (x, y) in detected_patch_coords:
            # Convert pixel coordinates to real-world coordinates
            # Assuming the center of the image is the drone's current position
            offset_lat = (y - self.image_height / 2) * (scale / 111320)  # meters to degrees latitude
            offset_lon = (x - self.image_width / 2) * (scale / (111320 * np.cos(np.radians(lat))))  # meters to degrees longitude
            
            gps_coords.append((lat + offset_lat, lon + offset_lon))
        
        return gps_coords

    def detect_hyacinth(self, frame):
        """Detect water hyacinth in the image frame using the trained model."""
        input_frame = cv2.resize(frame, (150, 150))  # Resize to model input size
        input_frame = input_frame / 255.0  # Normalize
        input_frame = np.expand_dims(input_frame, axis=0)  # Add batch dimension

        prediction = self.model.predict(input_frame)

        # If the model predicts a hyacinth patch
        if prediction > 0.5:
            return True  # Patch detected
        return False  # No patch detected

    def fly_to(self, latitude, longitude, altitude):
        """Send command to the drone to fly to a specific latitude, longitude, and altitude."""
        print(f"Flying to lat: {latitude}, lon: {longitude}, alt: {altitude}")

    def land(self):
        """Land the drone."""
        print("Landing the drone")

    def close_connection(self):
        """Safely close the connection to the drone."""
        print("Closing connection to the drone")
        self.master.close()


# Example usage of the DroneInterface class
if __name__ == "__main__":
    connection_str = "tcp:127.0.0.1:5760"  # Replace with actual drone connection string
    model_path = 'hyacinth_detection_model.h5'  # Path to your detection model

    # Initialize the drone interface
    drone = DroneInterface(connection_str, model_path)

    # Capture an image
    frame = drone.capture_image()

    if frame is not None:
        # Detect hyacinth in the captured image
        if drone.detect_hyacinth(frame):
            lat, lon, alt = drone.get_gps_coordinates()
            print(f"Hyacinth detected at drone's GPS Coordinates: Latitude {lat}, Longitude {lon}, Altitude {alt}m")
            
            # Assuming you have a method to get the coordinates of detected patches in the frame
            detected_patch_coords = [(100, 150), (200, 300)]  # Example pixel coordinates of detected patches
            gps_coords = drone.calculate_patch_coordinates(lat, lon, alt, detected_patch_coords)
            print("GPS Coordinates of detected patches:")
            for coord in gps_coords:
                print(f"Latitude: {coord[0]}, Longitude: {coord[1]}")
        
        else:
            print("No hyacinth detected.")

    # Land the drone
    drone.land()

    # Close the connection
    drone.close_connection()
