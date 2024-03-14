"""
half.py
    Splits a directory containing images into half. The original directory is not affected, two new directories are created.
"""
import os
import shutil
import random

def split_images(source_dir, dir1, dir2, split_ratio=0.5):
    """
    This function divides and copies the number of images in a directory to two other directories.

    Args:
        source_dir: path to the original directory
        dir1: path to the first directory 
        dir2: path to the second directory
        split_ratio: the ratio according to which the images should be divided; half by default

    Returns:
        None
    """
    # Get the list of image files in the source directory
    image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Calculate the number of images to be moved to each directory
    num_images_dir1 = int(len(image_files) * split_ratio)
    num_images_dir2 = len(image_files) - num_images_dir1

    # Randomly shuffle the list of image files
    random.shuffle(image_files)

    # Create the target directories if they don't exist
    os.makedirs(dir1, exist_ok=True)
    os.makedirs(dir2, exist_ok=True)

    # Copy images to the first directory
    for img_file in image_files[:num_images_dir1]:
        source_path = os.path.join(source_dir, img_file)
        target_path = os.path.join(dir1, img_file)
        shutil.copy2(source_path, target_path)

    # Copy images to the second directory
    for img_file in image_files[num_images_dir1:]:
        source_path = os.path.join(source_dir, img_file)
        target_path = os.path.join(dir2, img_file)
        shutil.copy2(source_path, target_path)

    print(f"Split {len(image_files)} images into {num_images_dir1} in '{dir1}' and {num_images_dir2} in '{dir2}'.")

# RUN
source_directory = "D:/YOLOv8-Combined-Split/YOLOv8-Combined-Split/train/images"
destination_directory1 = "D:/YOLOv8-Combined-Split/YOLOv8-Combined-Split/train/images-half1"
destination_directory2 = "D:/YOLOv8-Combined-Split/YOLOv8-Combined-Split/train/images-half2"

split_images(source_directory, destination_directory1, destination_directory2)