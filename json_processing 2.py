import json


path = "/Users/arshi/Desktop/Handwritten-Text-Recognition-in-Real-Time/kaggle_data_json/7.json"
# Open and read the JSON file
with open(path, 'r') as file:
    data = json.load(file)

# Now 'data' contains the parsed JSON as a Python dictionary



formatted_result = []

for idx in range(len(data['text'])):
    temp_json = {
                    "original_width": 1024,
                    "original_height": 1024,
                    "image_rotation": 0,
                    "value": {
                        "rotation": 0,
                    },
                    "id": f"bb{idx}",
                    "from_name": "transcription",
                    "to_name": "image",
                    "type": "textarea"
    }
    temp_json['value']['text'] = [data['text'][idx]]
    temp_json['value']['x'] = (data['left'][idx]/1024)*100
    temp_json['value']['y'] = (data['top'][idx]/1024)*100
    temp_json['value']['width'] = (data['width'][idx]/1024)*100
    temp_json['value']['height'] = (data['height'][idx]/1024)*100

    formatted_result.append(temp_json)


with open('output.json', 'w') as file:
    json.dump(formatted_result, file, indent=7)
