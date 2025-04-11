import cv2 as cv
import os
from src.exception.exception import CustomException
import sys
import signal
from datetime import datetime

def sig_handler(signum, frame):
   cam.release()
   cv.destroyAllWindows()
   exit(0)
   
try:
    signal.signal(signal.SIGINT, sig_handler)
    # Define the directory where images will be saved
    image_dir = 'captured_images'

    # Create the directory if it doesn't exist
    os.makedirs(image_dir, exist_ok=True)
    while 1:
      # Initialize the webcam
      cam = cv.VideoCapture(0)

      # Check if the webcam is opened correctly
      if not cam.isOpened():
        print("Error: Could not open webcam.")
        exit()

     
      ret, frame = cam.read()

      # Check if the frame was captured successfully
      if not ret:
         print("Error: Failed to capture image.")
      else:
          # Define the path to save the image
          timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
          img_name = os.path.join(image_dir, f'captured_image_{timestamp}.png')
 
          # Save the captured image to the specified directory
          cv.imwrite(img_name, frame)
          print(f"Image saved as {img_name}")

except Exception as e:
   raise CustomException(e,sys)