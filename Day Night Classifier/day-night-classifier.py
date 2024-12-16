import cv2
import os
import numpy as np

# Function to determine if the frame is day or night based on brightness
def is_day_or_night(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    average_brightness = np.mean(gray_frame)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    average_saturation = np.mean(hsv_frame[:, :, 1])
    if average_brightness > 30:
        return "Day"
    else:
        return "Night"

# Uncomment these for debugging purposes
# debug_folder = "debug"
# os.makedirs(debug_folder, exist_ok=True)
# day_folder = os.path.join(debug_folder, "day")
# night_folder = os.path.join(debug_folder, "night")
# os.makedirs(day_folder, exist_ok=True)
# os.makedirs(night_folder, exist_ok=True)

# Read the input video
video_path = "Input.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Define the codec and create a VideoWriter object
output_path = "Output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

frame_number = 0

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_number += 1

    # Determine if it's day or night
    label = is_day_or_night(frame)
    color = (0, 255, 0) if label == "Day" else (0, 0, 255)  # Green for day, red for night
    if label == "Day":
        color = (0, 255, 0)
        # Uncomment these for debugging purposes
        # debug_path = os.path.join(day_folder, f"day_{frame_number}.jpg")
        # cv2.imwrite(debug_path, frame)
    else:
        color = (0, 0, 255)
        # Uncomment these for debugging purposes
        # debug_path = os.path.join(night_folder, f"night_{frame_number}.jpg")
        # cv2.imwrite(debug_path, frame)

    # Add frame number and label to the frame
    cv2.putText(frame, f"Frame: {frame_number}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, label, (10, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Write the frame to the output video
    out.write(frame)

    #Optional: Display the frame in a window (for debugging)
    # cv2.imshow("Frame", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed {frame_number} frames. Output saved as {output_path}.")
