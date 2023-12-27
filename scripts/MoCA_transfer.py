"""
MoCA_transfer.py
    Contains the code to transfer files from a structure similar to that of the MoCA dataset:
    ../MoCA/ 
    ├── animal_type_1/           
    │   ├── images/
    │   │   ├── image01.jpg
    │   │   ├── image02.jpg
    │   │   └── ...
    │   ├── GT/        
    │   │   ├── image01.png
    │   │   ├── image02.png
    │   │   └── ...
    ├── animal_type_2/ 
    │   ├── images/
    │   │   ├── image01.jpg
    │   │   ├── image02.jpg
    │   │   └── ...
    │   ├── GT/       
    │   │   ├── image01.png
    │   │   ├── image02.png
    │   │   └── ...
    ├── animal_type_3/ 
    │   ├── images/
    │   │   ├── image01.jpg
    │   │   ├── image02.jpg
    │   │   └── ...
    │   ├── GT/       
    │   │   ├── image01.png
    │   │   ├── image02.png
    │   │   └── ...
    └── ...

    The output structure would be:
    ../MoCA/ 
    ├── images/    
    │   ├── animal_type_1_image01.jpg
    │   ├── animal_type_2_image01.jpg
    │   ├── animal_type_3_image01.jpg
    │   └── ...
    ├── gt/        
    │   ├── animal_type_1_image01.png
    │   ├── animal_type_2_image01.png
    │   ├── animal_type_3_image01.png
    │   └── ...
    └── ...
"""
import os
import shutil

def transfer_files(source_folder, destination_folder):
    """
    Moves or copies files from one directory to the other.

    Args:
        source_folder: path to the source folder.
        destination_folder: path to the destination folder.

    Returns:
        None
    """
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # counter to keep track of the number of files copied
    counter = 0
    # Transfer files to the destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.copy2(source_path, destination_path)

        counter += 1

    print("File transfer completed.")
    print(f"{counter} files successfully transferred.")

def Change_Directory(source, destination, sub):
    """
    This function transfers all files from a directory containing subdirectories.

    Args:
        source: root directory path.
        destination: destination directory path
        sub: the folder to be selected from within the subfolders.

    Returns:
        None
    """    
    # Create destination folder if it doesn't exist
    os.makedirs(destination, exist_ok=True)
    # find all the folders within the source directory
    folders = os.listdir(source)
    # iterate through each folder one at a time
    for folder in folders:
        # change path
        srcPath = os.path.join(source, folder)
        # change path and include the subfolder as well, such as 'GT' or 'images'
        srcPath = os.path.join(srcPath, sub)
        # call the transfer files function to perform rest of the work
        transfer_files(srcPath, destination)

# RUN
source_folder = '../Datasets/MoCA-old'  # path of the source folder
destination_folder = '../Datasets/MoCA/gt'  # path of the destination folder
sub = 'GT' # tells the folder to copy the binary masks or the images

Change_Directory(source_folder, destination_folder, sub)