import cv2
import pytesseract
from pytesseract import Output
import json
import os

# Paths for the image and output JSON file
image_path = '/Users/arshi/Downloads/student_resource 3/img_data/31ZtLoCMAnL.jpg'
json_folder = '/'

# Ensure the JSON folder exists
os.makedirs(json_folder, exist_ok=True)



d = pytesseract.image_to_data(image_path, output_type=Output.DICT)
print(d)

# Create the JSON file name in the new folder
json_filename = os.path.basename(image_path).replace('.jpg', '.json').replace('.jpeg', '.json')
json_path = os.path.join(json_folder, json_filename)
print(json_path)

# Write the dictionary to a JSON file
# with open(json_path, 'w') as json_file:
#     json.dump(d, json_file, indent=4, ensure_ascii=False)
    
# print(f'Processed {image_path} and saved as {json_path}')

