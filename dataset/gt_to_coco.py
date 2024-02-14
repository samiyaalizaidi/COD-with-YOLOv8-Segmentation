# Template by: https://github.com/bnsreenu
"""
This code automates the conversion of binary masks representing different object categories into the COCO (Common Objects in Context) JSON format. 

The code is based on the following folder structure for training and validation images and masks. You need to change the code based on your folder structure or organize your data to the format below.

../sample data/   # Primary data folder for the project
├── train/           
│   ├── images/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── gt/        
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
├── val/ 
│   ├── images/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
│   ├── gt/       
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
├── test/ 
│   ├── images/
│   │   ├── image01.png
│   │   ├── image02.png
│   │   └── ...
└── ...


For each binary mask, the code extracts contours using OpenCV. These contours represent the boundaries of objects within the images.This is a key step in converting binary masks to polygon-like annotations. 

Convert the contours into annotations, including bounding boxes, area, and segmentation information. Each annotation is associated with an image ID, category ID, and other properties required by the COCO format.

The code also creates an images section containing metadata about the images, such as their filenames, widths, and heights.

All the annotations, images, and categories are assembled into a dictionary that follows the COCO JSON format. This includes sections for "info," "licenses," "images," "categories," and "annotations."

Finally, the assembled COCO JSON data is saved to a file, making it ready to be used with tools and frameworks that support the COCO data format.

"""

import glob
import json
import os
import cv2

MASK_EXT = 'jpg'
ORIGINAL_EXT = 'jpg'
image_id = 0
annotation_id = 0

def images_annotations_info(maskpath):
    """
    Process the binary masks and generate images and annotations information.

    :param maskpath: Path to the directory containing binary masks
    :return: Tuple containing images info, annotations info, and annotation count
    """
    global image_id, annotation_id
    annotations = []
    images = []

    # Iterate through categories and corresponding masks
    for mask_image in glob.glob(os.path.join(maskpath, f'*.{MASK_EXT}')):
        original_file_name = f'{os.path.basename(mask_image).rsplit(".", 1)[0]}.{ORIGINAL_EXT}'
        mask_image_open = cv2.imread(mask_image)
        
        # Get image dimensions
        height, width, _ = mask_image_open.shape

        # Create or find existing image annotation
        if original_file_name not in map(lambda img: img['file_name'], images):
            image = {
                "id": image_id + 1,
                "width": width,
                "height": height,
                "file_name": original_file_name,
            }
            images.append(image)
            image_id += 1
        else:
            image = [element for element in images if element['file_name'] == original_file_name][0]

        # Find contours in the mask image
        gray = cv2.cvtColor(mask_image_open, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

        # Create annotation for each contour
        for contour in contours:
            bbox = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            segmentation = contour.flatten().tolist()

            annotation = {
                "iscrowd": 0,
                "id": annotation_id,
                "image_id": image['id'],
                "category_id": 0,
                "bbox": bbox,
                "area": area,
                "segmentation": [segmentation],
            }

            # Add annotation if area is greater than zero
            if area > 0:
                annotations.append(annotation)
                annotation_id += 1

            

    return images, annotations, annotation_id


def process_masks(mask_path, dest_json):
    global image_id, annotation_id
    image_id = 0
    annotation_id = 0

    # Initialize the COCO JSON format with categories
    coco_format = {
        "info": {},
        "licenses": [],
        "images": [],
        "categories": 1, 
        "annotations": [],
    }

    # Create images and annotations sections
    coco_format["images"], coco_format["annotations"], annotation_cnt = images_annotations_info(mask_path)

    # Save the COCO JSON to a file
    with open(dest_json, "w") as outfile:
        json.dump(coco_format, outfile, sort_keys=True, indent=4)

    print("Created %d annotations for images in folder: %s" % (annotation_cnt, mask_path))

if __name__ == "__main__":
    train_mask_path = "../Datasets/Kvasir-SEG-Split/train/gt"
    train_json_path = "../Datasets/Kvasir-SEG-Split/train/train.json"
    process_masks(train_mask_path, train_json_path)

    val_mask_path = "../Datasets/Kvasir-SEG-Split/val/gt"
    val_json_path = "../Datasets/Kvasir-SEG-Split/val/val.json"
    process_masks(val_mask_path, val_json_path)

    test_mask_path = "../Datasets/Kvasir-SEG-Split/test/gt"
    test_json_path = "../Datasets/Kvasir-SEG-Split/test/test.json"
    process_masks(test_mask_path, test_json_path)