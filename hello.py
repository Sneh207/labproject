import cv2
import numpy as np

def calculate_bpm(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess the image (threshold, blur, etc.)
    _, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours which might correspond to beats
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the x-coordinates of the detected beat markers
    beat_positions = []
    for cnt in contours:
        # Calculate the centroid of each contour
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])  # X-coordinate of the centroid
            beat_positions.append(cx)

    # Sort the beat positions by x-coordinate (time axis)
    beat_positions.sort()

    # Calculate time intervals between beats (assuming uniform time scale on the x-axis)
    time_intervals = np.diff(beat_positions)

    if len(time_intervals) == 0:
        print("No beats detected")
        return None

    # Calculate average time interval
    avg_interval = np.mean(time_intervals)

    # Assuming the image represents one second of music/data, calculate BPM
    bpm = (60 / avg_interval) * len(time_intervals)

    return bpm

# Example usage
image_path = 'Screenshot 2024-10-22 195353.png'
bpm = calculate_bpm(image_path)

if bpm:
    print(f"Calculated BPM: {bpm}")
