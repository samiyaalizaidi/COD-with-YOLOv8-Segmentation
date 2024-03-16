import os

def rename_class_folders(rename_txt_file, main_folder):
    with open(rename_txt_file, 'r') as file:
        class_names = file.readlines()

    for class_num, class_name in enumerate(class_names):
        class_name = class_name.strip()
        class_folder_old = os.path.join(main_folder, f'Class_{class_num}')
        class_folder_new = os.path.join(main_folder, class_name)
        os.rename(class_folder_old, class_folder_new)

def main():
    main_folder = 'Main_folder'
    rename_txt_file = 'class_names.txt'

    # Rename class folders
    rename_class_folders(rename_txt_file, main_folder)

if __name__ == "__main__":
    main()
