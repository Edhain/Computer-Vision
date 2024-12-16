# Day Night Classifier

## Project Overview
This project implements an image processing-based classifier that determines whether a specific frame in a video is captured during day or night time. By analyzing visual characteristics of each frame, the classifier provides real-time day/night detection.

## Features
- Image processing-based classification
- Automatic day/night frame detection

## Input
[Input Video](https://www.youtube.com/watch?v=x1Os8NcSrbI&t=1s)

## Technical Approach
The classifier uses advanced image processing techniques to determine day or night frames by analyzing:
- Brightness levels

*Note: Need to update and us better techniques in future*

## Dependencies
- Python 3.11
- OpenCV
- NumPy

## Usage
Download video and rename it "**Input.mp4**" and run the python script.

## Method Details
- Converts frames to grayscale
- Calculates average brightness
- Applies thresholding techniques

## Output
![Project Demo](output_4x.gif)

## Contact
Manas Pareek - manasdps@gmail.com