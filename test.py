import cv2
import pytesseract
from pytesseract import Output
import json
import os

# # Folder containing the images
# image_folder = 'kaggle_data'
# # Folder to save the JSON files
# json_folder = 'kaggle_data_json'

# # Ensure the JSON folder exists
# os.makedirs(json_folder, exist_ok=True)

# # Function to process an image and save its OCR data as JSON
# def process_image(image_path):
#     img = cv2.imread(image_path)
    
#     if img is not None:
#         # Get OCR data as a dictionary
#         d = pytesseract.image_to_data(img, output_type=Output.DICT)
        
#         # Create the JSON file name in the new folder
#         json_filename = os.path.basename(image_path).replace('.jpg', '.json').replace('.jpeg', '.json')
#         json_path = os.path.join(json_folder, json_filename)
        
#         # Write the dictionary to a JSON file
#         with open(json_path, 'w') as json_file:
#             json.dump(d, json_file, indent=4, ensure_ascii=False)
            
#         print(f'Processed {image_path} and saved as {json_path}')
#     else:
#         print(f'Error reading {image_path}')

# # Iterate over the image files from 1.jpg to 129.jpeg
# for i in range(1, 130):
#     processed = False
#     for ext in ['.jpg', '.jpeg']:
#         # Create the file name for the image
#         image_path = os.path.join(image_folder, f'{i}{ext}')
        
#         # Check if the file exists
#         if os.path.exists(image_path):
#             process_image(image_path)
#             processed = True
#             break
    
#     if not processed:
#         print(f'File {i}.jpg or {i}.jpeg does not exist.')


import cv2
import pytesseract
from pytesseract import Output
import json
import os

# Paths for the image and output JSON file
image_path = 'kaggle_data/90.jpg'
json_folder = 'kaggle_data_json'

# Ensure the JSON folder exists
os.makedirs(json_folder, exist_ok=True)



d = pytesseract.image_to_data(image_path, output_type=Output.DICT)
print(d.keys())

# Create the JSON file name in the new folder
json_filename = os.path.basename(image_path).replace('.jpg', '.json').replace('.jpeg', '.json')
json_path = os.path.join(json_folder, json_filename)
print(json_path)

# Write the dictionary to a JSON file
with open(json_path, 'w') as json_file:
    json.dump(d, json_file, indent=4, ensure_ascii=False)
    
print(f'Processed {image_path} and saved as {json_path}')

