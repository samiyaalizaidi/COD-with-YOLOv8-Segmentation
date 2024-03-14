import os
import shutil

label_path_train = ""
label_path_test  = ""
label_path_val   = ""
images_path_base = ""
destination      = ""

folders = os.listdir(images_path_base)
counter = 0

for folder in folders:
    # directory for each folder
    subfolder_path = os.path.join(images_path_base, folder)
    # go inside the subfolder
    for file in os.listdir(subfolder_path):
        # create the filename
        name = f"{folder}_{os.path.splitext(file)[0]}.txt"
        # choose from any of these folders
        if name in os.listdir(label_path_train): 
            indiv_label_path = os.path.join(label_path_train, name)
            shutil.copy(indiv_label_path, destination)

        elif name in os.listdir(label_path_test): 
            indiv_label_path = os.path.join(label_path_test, name)
            shutil.copy(indiv_label_path, destination)

        elif name in os.listdir(label_path_val): 
            indiv_label_path = os.path.join(label_path_val, name)
            shutil.copy(indiv_label_path, destination)

        counter += 1

print(f"{counter} labels copied!")
