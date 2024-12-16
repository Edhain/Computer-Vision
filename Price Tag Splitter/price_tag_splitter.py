import cv2
import os
import numpy as np

def split_price_tags(img_path, output_folder):
    # Read the image
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    
    # Number of rows and columns
    rows = 6
    cols = 3
    
    # Calculate the approximate dimensions of each split
    split_height = np.ceil(height / rows).astype(int)
    split_width = np.ceil(width / cols).astype(int)
    
    print(f"Image dimensions: {height}x{width}")
    print(f"Split dimensions: {split_height}x{split_width}")

    # Iterate through the rows and columns
    for row in range(rows):
        for col in range(cols):
            # Calculate the start (top-left corner) coordinates
            x1 = col * split_width
            y1 = row * split_height
            
            # Calculate the end (bottom-right corner) coordinates
            x2 = min(x1 + split_width, width)  # Ensure it doesn't exceed the width
            y2 = min(y1 + split_height, height)  # Ensure it doesn't exceed the height
            
            # Extract the price tag region
            price_tag = img[y1:y2, x1:x2]
            
            # Save the split image
            filename = f"split_image_{row}_{col}.jpg"
            filepath = output_folder + filename
            print(f"Saving: {filepath}")
            cv2.imwrite(filepath, price_tag)

    return

debug_folder = "data"
os.makedirs(debug_folder, exist_ok=True)
path = 'input.jpg'
output_folder = 'data/'

split_price_tags(path,output_folder)