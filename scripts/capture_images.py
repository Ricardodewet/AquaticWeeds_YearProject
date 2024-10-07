from dronekit import connect, VehicleMode, LocationGlobalRelative
from time import sleep
import math
import random  # Placeholder for image capture simulation
from PIL import Image  # If you want to save blank images as placeholders

# Connect to the drone
drone = connect('connection_string', wait_ready=True)

def calculate_grid_point(drone, row, col, grid_size=5, distance_between_points=10):
    """
    Calculate a new GPS location based on the grid position.
    :param drone: The connected drone object.
    :param row: The current row in the grid.
    :param col: The current column in the grid.
    :param grid_size: The size of the grid (default 5x5).
    :param distance_between_points: Distance between points in meters.
    :return: A LocationGlobalRelative object for the new target location.
    """
    # Get current location
    current_location = drone.location.global_relative_frame

    # Calculate lat/long shifts (simple approximation for short distances)
    lat_shift = (row - grid_size // 2) * (distance_between_points / 111320)  # 1 deg lat = 111.32 km
    lon_shift = (col - grid_size // 2) * (distance_between_points / (111320 * math.cos(math.radians(current_location.lat))))

    # Create new target location
    new_lat = current_location.lat + lat_shift
    new_lon = current_location.lon + lon_shift
    return LocationGlobalRelative(new_lat, new_lon, current_location.alt)

# Function to simulate image capture and saving
def capture_image_simulation(row, col):
    # Placeholder for image capture: create blank images with unique filenames
    img = Image.new('RGB', (100, 100), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    filename = f'grid_image_{row}_{col}.jpg'
    img.save(filename)
    print(f"Image saved as {filename}")
    return filename

# Function to capture images in a grid pattern
def capture_images_in_grid(drone, grid_size=5, distance_between_points=10):
    """
    Capture images in a grid pattern using the drone.
    :param drone: The connected drone object.
    :param grid_size: The size of the grid (default is 5x5).
    :param distance_between_points: The distance between grid points in meters.
    """
    for row in range(grid_size):
        for col in range(grid_size):
            # Move the drone to the next grid point
            target_location = calculate_grid_point(drone, row, col, grid_size, distance_between_points)
            print(f"Moving to grid point: Row {row}, Col {col} -> {target_location.lat}, {target_location.lon}")

            # Command the drone to fly to the next point
            drone.simple_goto(target_location)
            # Wait for the drone to reach the target
            sleep(10)  # Adjust this depending on the drone's speed and the distance between points

            # Capture image (simulated in this case)
            capture_image_simulation(row, col)

# Make sure the drone is in GUIDED mode
drone.mode = VehicleMode("GUIDED")
while not drone.mode.name == 'GUIDED':
    print("Waiting for drone to enter GUIDED mode...")
    sleep(1)

# Set altitude
target_altitude = 20  # Set the target altitude to 20 meters
drone.simple_takeoff(target_altitude)

# Wait until the drone reaches the target altitude
while True:
    print(f"Current Altitude: {drone.location.global_relative_frame.alt}")
    if drone.location.global_relative_frame.alt >= target_altitude * 0.95:
        print("Reached target altitude")
        break
    sleep(1)

# Start capturing images in the grid pattern
capture_images_in_grid(drone)

# Land the drone after completing the grid capture
print("Grid capture complete. Landing the drone.")
drone.mode = VehicleMode("LAND")
while not drone.mode.name == 'LAND':
    print("Waiting for drone to enter LAND mode...")
    sleep(1)

# Close connection
drone.close()
