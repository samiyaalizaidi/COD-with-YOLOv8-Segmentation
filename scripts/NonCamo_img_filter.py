import os
import shutil

def filter_and_copy_images(source_folder, destination_folder):
    # Make sure the destination folder exists, create it if necessary
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is an image and the name contains "NonCAM"
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and 'NonCAM' not in filename:
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Copy the file to the destination folder
            shutil.copy2(source_path, destination_path)
            print(f"Image '{filename}' copied to '{destination_folder}'")

# Example usage
source_directory = '/path/to/source_folder'
destination_directory = '/path/to/destination_folder'

filter_and_copy_images(source_directory, destination_directory)
