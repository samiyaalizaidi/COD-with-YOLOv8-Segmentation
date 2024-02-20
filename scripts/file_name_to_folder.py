"""
file_name_to_folder.py
    Takes in a dataset split in train and validation and extracts the folder/class names from the file names. Then it creates a folder for each class in a seperate directory.
"""
import os 
import shutil

def file_name_to_folder(base_input_dir: str, base_output_dir: str, input_sub_dir: list):
    """
    Function to create folders using the image names.
    Args:
        base_input_dir: path to the base directory that contains sub folders.
        base_output_dir: path to the directory where the folders should be created
        input_sub_dir: subfolders within the base input directory. In the form of a list.

    Returns:
        None
    """
    # to keep track of the classes
    classes_list    = []
    # to keep track of the number of images copied
    counter = 0 
    # check both the train and val directories
    for subfolder in input_sub_dir:
        # change the path to only choose the images directory
        sub_folder_path = os.path.join(base_input_dir, subfolder)
        sub_folder_path = os.path.join(sub_folder_path, "images")
        # check the images in the images directory
        for file in os.listdir(sub_folder_path):
            # extract the folder/class name
            class_name = file.rsplit('_')
            class_name = "_".join(class_name[:-1])
            # create the source path for the file
            path_src  = sub_folder_path
            # create the destination path for the file
            path_dest = os.path.join(base_output_dir, class_name)
            # create a new directory if it doesnt already exist
            os.makedirs(path_dest, exist_ok="True")
            # if not in the list, append. To keep track
            if class_name not in classes_list:
                classes_list.append(class_name)
            # paths to the file, for both source and destination
            file_path_src  = os.path.join(path_src, file)
            file_path_dest = os.path.join(path_dest, file)
            # copy the images
            shutil.copy(file_path_src, file_path_dest)
            # increment the counter
            counter += 1

    print("Folders created:", classes_list)
    print(counter, "images copied!")        


# Driver

# base input directory
base_input_dir  = ""
# base directory to store the output
base_output_dir = ""
# sub directories in the input 
input_sub_dir   = ["train", "val"]
# call the function
file_name_to_folder(base_input_dir, base_output_dir, input_sub_dir)