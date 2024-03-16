"""
bbox_from_mask.py
    This script contains the function used to generate YOLO format labels for object detection using the binary masks.
"""
import cv2
import os
class_num =0 
def generate_YOLO_bbox(input_directory: str, output_directory: str, GT_EXT='jpg'):
    """
    This function generates the YOLO object detection format bounding boxes from the provided binary masks.

    Args:
        input_directory: path to the input folder containing the binary masks.
        output_directory: directory where the generated labels should be stored.
        GT_EXT: image extension for the binary masks; png by default.
    
    Returns:
        None
    """
    global class_num
    # create the output directory if it doesn't already exist 
    os.makedirs(output_directory, exist_ok=True)
    # to keep track of the number of labels generated
    counter = 0
    # extension for the labels
    EXT = 'txt'
    # iterate over all of the binary masks provided
    for filename in os.listdir(input_directory):
        # verify the file extension
        if not filename.endswith(GT_EXT):
            print(f'The image extension, {os.path.splitext(filename)[1]}, does not match the provided extension, {GT_EXT}')
            break
        counter += 1
        # construct the full file path
        file_path = os.path.join(input_directory, filename)
        # load the segmented image
        segmented_image = cv2.imread(file_path)
        # convert the segmented image to grayscale
        gray_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)
        # threshold the grayscale image to create a binary mask
        _ , binary_mask = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
        # find contours in the binary mask
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # construct the full output path
        label_filename = f'{os.path.splitext(filename)[0]}.{EXT}'
        label_path = os.path.join(output_directory, label_filename)
        # to store the class and coordinates of all the objects found in an image   
        string_label = ''
        # extract the coordinates for all the contours found
        for contour in contours:
            x, y, width, height = cv2.boundingRect(contour)
            x_center = x + (width / 2)
            y_center = y + (height / 2)
            # normalize
            normalized_x = x_center / segmented_image.shape[1]
            normalized_y = y_center / segmented_image.shape[0]
            normalized_width = width / segmented_image.shape[1]
            normalized_height = height / segmented_image.shape[0]
            # create the string for multiple objects within the same image file
            string_label += f'{class_num} {normalized_x:.6f} {normalized_y:.6f} {normalized_width:.6f} {normalized_height:.6f}\n'

        # write the file
        with open(label_path, 'w') as output_file:
            output_file.write(string_label)

    print(f'Labels created for {counter} images.')


###############################################################################################################################
for x in range(102):
    input_dir = "D:/YOLOv8-Combined-Split/YOLOv8-Combined-Split/val/gt"
    output_dir = "D:/YOLOv8-Combined-Split/YOLOv8-Combined-Split/val/labels-detection"

    generate_YOLO_bbox(input_dir, output_dir)
    class_num+=1
