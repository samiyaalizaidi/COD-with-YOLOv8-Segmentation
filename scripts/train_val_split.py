"""
train_val_split.py
    Contains the functions for splitting a folder into train and val.
"""

import os
import shutil
from sklearn.model_selection import train_test_split

def make_2_directories(path1, name1, path2, name2):
    """
    Creates two directories.

    Args:
        path1: path to the first root folder
        name1: name of the directory to be created in path1
        path2: path to the second root folder
        name2: name of the directory to be created in path2

    Returns:
        join1: path to the first directory created
        join2: path to the second directory created
    """
    # Join the paths
    join1 = os.path.join(path1, name1)
    join2 = os.path.join(path2, name2)

    # Create the directories
    os.makedirs(join1, exist_ok=True)
    os.makedirs(join2, exist_ok=True)

    # Return the paths
    return join1, join2

def split_dataset(input_folder_img, input_folder_gt, output_folder, GT_EXT, IMG_EXT, split_ratio=0.8, seed=None):
    """
    This function splits a dataset into training and validation folders. Both the images and their respective binary masks are split simultaneously but in different folders.

    Args:
        input_folder_img: path to the directory containing the images
        input_folder_gt: path to the directory containing the binary masks
        output_folder: path to the output directory
        GT_EXT: image extension of the binary masks; eg., png, jpg, jpeg, etc.
        IMG_EXT: image extension of the images; eg., png, jpg, jpeg, etc.      
        split_ratio: the desired ratio for split; 80:20 by default
        seed: for the reproducability of the split; 42 by default

    Returns:
        None
    """

    if not 0 < split_ratio < 1:
        raise ValueError("Split ratio must be between 0 and 1.")

    # Create output folders
    train_folder, val_folder = make_2_directories(output_folder, 'train', output_folder, 'val')

    # Create subfolders for the training directory
    train_folder_img, train_folder_gt = make_2_directories(train_folder, 'images', train_folder, 'gt')

    # Create subfolders for the validation directory
    val_folder_img, val_folder_gt = make_2_directories(val_folder, 'images', val_folder, 'gt')

    # List all files in the input folder
    img_files = os.listdir(input_folder_img)

    # Separate the files into training and validation sets
    train_files, val_files = train_test_split(img_files, test_size=(1 - split_ratio), random_state=seed)

    # Copy files to training and validation folders
    for file in train_files:
        # Get the proper extensions
        filename = file.split('.')[0]
        img = filename + '.' + IMG_EXT
        gt = filename + '.' + GT_EXT

        # Copy the image
        src_path_img = os.path.join(input_folder_img, img)
        dest_path_img = os.path.join(train_folder_img, img)
        shutil.copy(src_path_img, dest_path_img)

        # Copy the masks
        src_path_gt = os.path.join(input_folder_gt, gt)
        dest_path_gt = os.path.join(train_folder_gt, gt)
        shutil.copy(src_path_gt, dest_path_gt)

    for file in val_files:
        # Get the proper extensions
        filename = file.split('.')[0]
        img = filename + '.' + IMG_EXT
        gt = filename + '.' + GT_EXT

        # Copy the image
        src_path_img = os.path.join(input_folder_img, img)
        dest_path_img = os.path.join(val_folder_img, img)
        shutil.copy(src_path_img, dest_path_img)

        # Copy the masks
        src_path_gt = os.path.join(input_folder_gt, gt)
        dest_path_gt = os.path.join(val_folder_gt, gt)
        shutil.copy(src_path_gt, dest_path_gt)

    print(f"Dataset split completed. {len(train_files)} files in training set and {len(val_files)} files in validation set.")

# Arguments
input_folder_img = '..\data\CAMO-V.1.0-CVIU2019\Images\Train'  # path to the images
input_folder_gt = '..\data\CAMO-V.1.0-CVIU2019\GT' # path to the binary masks
output_folder = '..\CAMO'  # path to the output folder
split_ratio = 0.8  # Change the split ratio if needed
seed = 42  # Change the seed if you want reproducibility
GT_EXT = 'png'
IMG_EXT = 'jpg'

split_dataset(
    input_folder_img, input_folder_gt, output_folder, GT_EXT, IMG_EXT
)
