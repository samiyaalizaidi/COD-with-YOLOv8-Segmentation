"""
train_test_val_split.py
    Contains the functions needed to split an image and GT dataset into training, validation, and testing sets.
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

def train_test_val_split(input_folder_img, input_folder_gt, output_folder, GT_EXT, IMG_EXT,split_ratios=(0.75, 0.15, 0.1), seed=None):
    """
    This function splits a dataset containing images and their binary masks into training, testing, and validation directories.
    
    Args:
        input_folder_img: Path to the image directory which has all the images to be split into train, test, validation sets.
        input_folder_gt: Path to the binary masks' directory which has all the masks to be split into train, test, validation sets.
        output_folder: Path to the output folder.
        GT_EXT: image type of the binary masks, i.e png, jpg, etc.
        IMG_EXT: image type of the images, i.e. png, jpg, etc.
        split_ratios: desired ratio of the train:val:test directories; 75%:15%:10% by default.
        seed: to ensure the reproducibility of the split; None by default.

    Returns:
        None.
    """
    if sum(split_ratios) != 1.0:
        raise ValueError("Split ratios must add up to 1.0.")

    # Create output folders
    train_folder = os.path.join(output_folder, 'train')
    val_folder = os.path.join(output_folder, 'val')
    test_folder = os.path.join(output_folder, 'test')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Create subfolders for each directory
    train_folder_img, train_folder_gt = make_2_directories(train_folder, 'images', train_folder, 'gt')
    val_folder_img, val_folder_gt = make_2_directories(val_folder, 'images', val_folder, 'gt')
    test_folder_img, test_folder_gt = make_2_directories(test_folder, 'images', test_folder, 'gt')
 
    # List all files in the input folder
    files = os.listdir(input_folder_img)

    # Separate the files into training, validation, and test sets
    train_files, remaining_files = train_test_split(files, test_size=(1 - split_ratios[0]), random_state=seed)
    val_test_files = remaining_files
    val_files, test_files = train_test_split(val_test_files, test_size=(split_ratios[2] / (split_ratios[1] + split_ratios[2])), random_state=seed)

    # Copy files to the corresponding folders
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

    for file in test_files:
        # Get the proper extensions
        filename = file.split('.')[0]
        img = filename + '.' + IMG_EXT
        gt = filename + '.' + GT_EXT

        # Copy the image
        src_path_img = os.path.join(input_folder_img, img)
        dest_path_img = os.path.join(test_folder_img, img)
        shutil.copy(src_path_img, dest_path_img)

        # Copy the masks
        src_path_gt = os.path.join(input_folder_gt, gt)
        dest_path_gt = os.path.join(test_folder_gt, gt)
        shutil.copy(src_path_gt, dest_path_gt)

    print(f"Dataset split completed. {len(train_files)} files in training set, {len(val_files)} files in validation set, and {len(test_files)} files in test set.")

# Example usage
input_folder_img = '../Datasets/NC4K-old/images'  # path to the images
input_folder_gt = '../Datasets/NC4K-old/GT' # path to the binary masks
output_folder = '../Datasets/NC4K'
split_ratios = (0.75, 0.15, 0.1)  # Adjust the split ratios if needed
seed = 42  # Change the seed if you want reproducibility
GT_EXT = "png" 
IMG_EXT = "jpg"

train_test_val_split(input_folder_img, input_folder_gt, output_folder, GT_EXT, IMG_EXT, split_ratios, seed)
