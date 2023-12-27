"""
transfer.py
    Contains the code to transfer files from one directory to the other.
"""
import os
import shutil

def transfer_files(source_folder, destination_folder):
    """
    Moves or copies files from one directory to the other.

    Args:
        source_folder: path to the source folder.
        destination_folder: path to the destination folder.
        file_extensions: list containing the extensions of all the files to be transferred; None by default.
        move: to move the files from source to destination instead of copying; False by default.

    Returns:
        None
    """
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Filter files based on extensions if provided
    if file_extensions:
        files = [file for file in files if any(file.endswith(ext) for ext in file_extensions)]
    move = False
    # Transfer files to the destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)


        if move:
            shutil.move(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)

    print("File transfer completed.")
    print(f"{len(files)} files successfully transferred.")

def checkDirectory(source, destination):
    
    # Create destination folder if it doesn't exist
    os.makedirs(destination, exist_ok=True)

    folders = os.listdir(source)

    for folder in folders:
        srcPath = os.path.join(source, folder)
        srcPath = os.path.join(srcPath, 'GT')
        print('folder =', folder, 'path =', srcPath)
        transfer_files(srcPath, destination, folder)
    

# RUN
source_folder = 'CAMO-V.1.0-CVIU2019/CAMO-V.1.0-CVIU2019/GT'  # path of the source folder
destination_folder = 'Combined/gt'  # path of the destination folder
file_extensions = ['.txt', '.jpg', '.png']  # Specify file extensions to transfer (None for all files)
move_files = False  # Set to True to move the files instead of copying.
transfer_files(source_folder, destination_folder)
#transfer_files(source_folder, destination_folder, file_extensions, move_files)
