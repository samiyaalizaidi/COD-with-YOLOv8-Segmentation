"""
create_empty_txt.py

"""
import os

def create_text(file_path: str):
    """
    Creates an empty text file.

    Args: 
        file_path: path for the empty text file that needs to be created

    Returns:
        None
    """
    # Open the file in write mode ('w')
    # If the file doesn't exist, it will be created
    # If the file already exists, its contents will be truncated (emptied)
    with open(file_path, 'w') as file:
        # The file is now open and empty
        pass



def create_empty_txt(input_img_directory: str, output_txt_directory: str, string_condition: str):
    """
    This function creates empty text files with the same names as the image files containing a particular string in the name.

    Args:
        input_img_directory: path to the directory containing all the images whose corresponding txt is required
        output_txt_directory: path to the directory where empty text files should be stored.
        string_condition: particular string required in the filename that needs an empty txt file.

    Returns:
        None
    """
    # extract the names of all the files
    img_names = os.listdir(input_img_directory)

    counter = 0

    for filename in img_names:
        # only go through the files that have a certain string in them
        if string_condition not in filename: continue
        # change the file extension to .txt
        filename = os.path.splitext(filename)[0] + '.txt'
        # create the path
        path = os.path.join(output_txt_directory, filename)
        # calling the function to create one text file
        create_text(path)
        # increment the counter value to keep track
        counter += 1

    print(f'{counter} empty text files created!')

# RUN
input_img_directory = "../Datasets/YOLOv8-Combined-Split/test/images" # path to the images
output_path = "../Datasets/YOLOv8-Combined-Split/test/labels" # location to save the empty txt    
string = 'NonCAM' # The required string

create_empty_txt(input_img_directory, output_path, string)