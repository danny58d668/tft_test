import cv2
import numpy as np


def is_bench_slot_empty(screenshot, bench_slot_coordinates):
    # Load the screenshot
    screenshot = cv2.imread(screenshot)

    bench_floor_color = np.array([145, 130, 166])
    color_threshold = 80
    # Extract the region of interest (ROI) based on bench slot coordinates
    x, y, w, h = bench_slot_coordinates
    roi = screenshot[y:y+h, x:x+w]

    # Calculate the average RGB values in the ROI
    average_color = np.mean(roi, axis=(0, 1))

    # Compare the average color with the specified bench floor color
    color_difference = np.linalg.norm(average_color - bench_floor_color)

    # Set a threshold for considering the slot as not empty
    threshold = color_threshold  # Adjust this threshold based on your needs

    if color_difference <= threshold:
        return True  # Bench slot is empty
    else:
        return False  # Bench slot is not empty

# Example usage
screenshot_path = '../img/ingame 10.png'
template_path = '../img/empty_bench.png'

coord = (501, 740, 600, 830)  #  F
# coord = (1172, 745, 1297, 828) #  T
#coord = (1295, 743, 1410, 830) #  T

result = is_bench_slot_empty(screenshot_path, coord)

if result:
    print("Bench slot is empty!")
else:
    print("Bench slot is not empty.")
