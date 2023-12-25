# Template by: https://github.com/bnsreenu
"""
This code transforms a dataset of images and annotations into a format suitable for training a YOLO (You Only Look Once) object detection model, and it also creates a YAML configuration file required for training the model.

It reads coco style json annotations supplied as a single json file and also images as input. 

Here are the key steps in the code:

1. Convert Images to YOLO Format: The convert_to_yolo function takes paths for input images and annotations (in JSON format), and directories to store the output images and labels. It then performs the following operations:

- Reads the input JSON file containing annotations.
- Copies all images from the input directory to the output directory.
- Normalizes the polygon segmentation data related to each image and writes them to text files, mapping them to the appropriate category 
- The resulting text files contain information about the object category and the normalized coordinates of the polygons that describe the objects.

2. Create YAML Configuration File: The create_yaml function takes paths to the input JSON file containing categories, training, validation, and optional test paths. It then:

- Extracts the category names and the number of classes.
- Constructs a dictionary containing information about class names, the number 
of classes, and paths to the training, validation, and test datasets.
- Writes this dictionary to a YAML file, which can be used as a configuration 
file for training a model (e.g., a YOLO model).
    
The text annotation file consists of lines representing individual object annotations, with each line containing the class ID followed by the normalized coordinates of the polygon describing the object.

Example structure of the YOLO annotation file:

<class_id> <normalized_polygon_coordinate_1> <normalized_polygon_coordinate_2> ... <normalized_polygon_coordinate_n>
0 0.123456 0.234567 0.345678 0.456789 ...

"""


import json
import os
import shutil
import yaml

# Function to convert images to YOLO format
def convert_to_yolo(input_images_path, input_json_path, output_images_path, output_labels_path):
    # Open JSON file containing image annotations
    f = open(input_json_path)
    data = json.load(f)
    f.close()

    # Create directories for output images and labels
    os.makedirs(output_images_path, exist_ok=True)
    os.makedirs(output_labels_path, exist_ok=True)

    # List to store filenames
    file_names = []
    for filename in os.listdir(input_images_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            source = os.path.join(input_images_path, filename)
            destination = os.path.join(output_images_path, filename)
            shutil.copy(source, destination)
            file_names.append(filename)

    

    # Function to get image annotations
    def get_img_ann(image_id):
        return [ann for ann in data['annotations'] if ann['image_id'] == image_id]

    # Function to get image data
    def get_img(filename):
        return next((img for img in data['images'] if img['file_name'] == filename), None)

    counter = 0
    
    # Iterate through filenames and process each image
    for filename in file_names:
        img = get_img(filename)
        img_id = img['id']
        img_w = img['width']
        img_h = img['height']
        img_ann = get_img_ann(img_id)

        # Write normalized polygon data to a text file
        if img_ann:
            with open(os.path.join(output_labels_path, f"{os.path.splitext(filename)[0]}.txt"), "a") as file_object:
                for ann in img_ann:
                    current_category = ann['category_id'] 
                    polygon = ann['segmentation'][0]
                    normalized_polygon = [format(coord / img_w if i % 2 == 0 else coord / img_h, '.6f') for i, coord in enumerate(polygon)]
                    file_object.write(f"{current_category} " + " ".join(normalized_polygon) + "\n")
        
        counter += 1

    print(f'{counter} labels created!')

# Function to create a YAML file for the dataset
def create_yaml(input_json_path, output_yaml_path, train_path, val_path, test_path=None):
    with open(input_json_path) as f:
        data = json.load(f)
    
    # Extract the category names
    names = ['Camo']
    
    # Number of classes
    nc = len(names)

    # Create a dictionary with the required content
    yaml_data = {
        'names': names,
        'nc': nc,
        'test': test_path if test_path else '',
        'train': train_path,
        'val': val_path
    }

    # Write the dictionary to a YAML file
    with open(output_yaml_path, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

        print('yaml created!')


if __name__ == "__main__":
    base_input_path = "../CAMO/"
    base_output_path = "../CAMO-Labels/"

    # Processing validation dataset (if needed)
    convert_to_yolo(
        input_images_path=os.path.join(base_input_path, "val/images"),
        input_json_path=os.path.join(base_input_path, "val/val.json"),
        output_images_path=os.path.join(base_output_path, "val/images"),
        output_labels_path=os.path.join(base_output_path, "val/labels")
    )

    # Processing training dataset 
    convert_to_yolo(
        input_images_path=os.path.join(base_input_path, "train/images"),
        input_json_path=os.path.join(base_input_path, "train/train.json"),
        output_images_path=os.path.join(base_output_path, "train/images"),
        output_labels_path=os.path.join(base_output_path, "train/labels")
    )
    
    # Creating the YAML configuration file
    create_yaml(
        input_json_path=os.path.join(base_input_path, "train/train.json"),
        output_yaml_path=os.path.join(base_output_path, "data.yaml"),
        train_path="../yolo output/train/images",
        val_path="../yolo output/val/images",
        test_path='../yolo output/test/images'  # or None if not applicable
    )