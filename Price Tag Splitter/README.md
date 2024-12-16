# Price Tag Splitter

## Overview
The Price Tag Splitter is a Python script that takes an image of a grid of price tags and automatically splits it into individual price tag images. This can be useful for e-commerce or retail applications where you need to extract individual price tags from a larger image.

## Features
- Automatically detects the grid structure of the price tags
- Splits the image into individual price tag images
- Saves the split images to a specified output folder

## Input
Use the given **input.png** image as the input.

## How it Works

1. The script reads the input image using OpenCV.
2. It calculates the approximate dimensions of each price tag based on the image size and a predefined grid structure (6 rows, 3 columns).
3. The script then iterates through the grid, extracting each price tag region and saving it as a separate image file in the `data/` folder.

## Usage

1. Place the input image (e.g., input.jpg) in the same directory as the price_tag_splitter.py script.
2. Run the script:
```bash
python price_tag_splitter.py
```
3. The split price tag images will be saved in the data/ folder.

## Dependencies
- Python 3.11
- OpenCV
- NumPy

## Contact
Manas Pareek - manasdps@gmail.com