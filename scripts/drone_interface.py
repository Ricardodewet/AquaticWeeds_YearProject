# Import necessary libraries
from pymavlink import mavutil
import cv2  # OpenCV for image capture
import time

class DroneInterface:
    def __init__(self, connection_string): #The connection string should be replaced with your actual drone's connection info. For simulation, tcp:127.0.0.1:5760 works for MAVProxy.
        """Initialize the connection to the drone."""
        # Connect to the MAVLink drone
        self.master = mavutil.mavlink_connection(connection_string)
        # Wait for the heartbeat message to know the connection is successful
        self.master.wait_heartbeat()

        print("Connected to the drone")

    def capture_image(self, save_path="captured_images/"):
        """Capture an image from the drone's camera."""
        # This part would depend on the drone's camera setup, simulated here by OpenCV webcam
        cap = cv2.VideoCapture(0)  # Replace 0 with appropriate camera ID if needed
        ret, frame = cap.read()

        if ret:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_filename = f"{save_path}image_{timestamp}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image saved to {image_filename}")
        else:
            print("Failed to capture image")

        cap.release()

    def get_gps_coordinates(self):
        """Retrieve the GPS coordinates of the drone."""
        # Wait for a GPS message
        msg = self.master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        lat = msg.lat * 1e-7
        lon = msg.lon * 1e-7
        alt = msg.alt * 1e-3  # Convert to meters

        return lat, lon, alt

    def fly_to(self, latitude, longitude, altitude):
        """Send command to the drone to fly to a specific latitude, longitude, and altitude."""
        print(f"Flying to lat: {latitude}, lon: {longitude}, alt: {altitude}")
        # Add commands to send flight instructions to the drone using MAVLink messages

    def land(self):
        """Land the drone."""
        print("Landing the drone")
        # Add MAVLink command to land the drone

    def close_connection(self):
        """Safely close the connection to the drone."""
        print("Closing connection to the drone")
        self.master.close()

# Example usage of the DroneInterface class
if __name__ == "__main__":
    # Define the connection string (this will depend on your drone setup)
    connection_str = "tcp:127.0.0.1:5760"  # Replace with actual drone connection string

    # Initialize the drone interface
    drone = DroneInterface(connection_str)

    # Capture an image
    drone.capture_image()

    # Get the GPS coordinates
    lat, lon, alt = drone.get_gps_coordinates()
    print(f"GPS Coordinates: Latitude {lat}, Longitude {lon}, Altitude {alt}m")

    # Example: Fly the drone to a different location
    drone.fly_to(latitude=lat + 0.001, longitude=lon + 0.001, altitude=alt + 10)

    # Land the drone
    drone.land()

    # Close the connection
    drone.close_connection()
