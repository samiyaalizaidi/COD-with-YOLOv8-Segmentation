"""
tranfer_few.py
    Script to transfer a specific number of images from one directory to another along with the GTs and labels.
"""
import os
import shutil
import random

def transfer_few_files(input_dir_base: str, output_dir_base: str, num_files: int, labels:bool = True , gt:bool=True):
    """
    Transfer files from one directory to another. You can also tranfer the labels and/or binary masks if required.

    Args:
        input_dir_base: path to the input directory where all the subfolders are
        output_dir_base: path to the output directory where all the subfolders are
        num_files: number of random files to be transferred
        labels: confirms whether labels should be transferred or not; true by default
        gt: confirms whether binary masks should be transferred or not; true by default

    Returns:
        None
    """

    # create the output directory if it doesn't already exist
    os.makedirs(output_dir_base, exist_ok=True)

    # create paths
    image_input = os.path.join(input_dir_base, 'images')
    labels_input, gt_input = "", ""

    # create directories' path if set to true
    if labels: labels_input = os.path.join(input_dir_base, 'labels')
    if gt: gt_input = os.path.join(input_dir_base, 'gt')

    # create paths for output as well
    image_output = os.path.join(output_dir_base, 'images')
    labels_output, gt_output = "", ""

    # create directories if set to true
    if labels: 
        labels_output = os.path.join(output_dir_base, 'labels')
        os.makedirs(labels_output, exist_ok=True)

    if gt: 
        gt_output = os.path.join(output_dir_base, 'gt')
        os.makedirs(gt_output, exist_ok=True)

    # Get a list of all files in the image directory
    img_files = os.listdir(image_input)

    # randomly select image
    selected_images = random.sample(img_files, num_files)

    # to maintain count
    counter = 0

    # transfer files
    for image in selected_images:
        # copy the images
        source_path = os.path.join(image_input, image)
        destination_path = os.path.join(image_output, image)
        shutil.copy2(source_path, destination_path)

        # copy the labels (if required)
        if labels:
            filename = os.path.splitext(image)[0]
            filename = f'{filename}.txt'
            source_path = os.path.join(labels_input, filename)
            destination_path = os.path.join(labels_output, filename)
            shutil.copy2(source_path, destination_path)

        # copy the binary masks (if required)
        if labels:
            filename = os.path.splitext(image)[0]
            filename = f'{filename}.png'
            source_path = os.path.join(gt_input, filename)
            destination_path = os.path.join(gt_output, filename)
            shutil.copy2(source_path, destination_path)

        counter += 1

    print(f'{counter} files were copied!')

# RUN THE CODE

base_input = "../Datasets/base" # base directory of the input
base_output = "../Datasets/MoCA+base" # base directory of the output
num_files = 1326 # number of files to be transferred

transfer_few_files(base_input, base_output, num_files)