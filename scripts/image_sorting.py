import os
import shutil

def create_class_folders(main_folder, num_classes):
    for class_num in range(num_classes):
        class_folder = os.path.join(main_folder, f'Class_{class_num}')
        os.makedirs(class_folder)
        os.makedirs(os.path.join(class_folder, 'Images'))

def move_images_to_class_folders(image_txt_file, source_images_folder, main_folder):
    with open(image_txt_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        image_name, class_num = line.strip().split(' ')
        class_num = int(class_num)
        class_folder = os.path.join(main_folder, f'Class_{class_num}', 'Images')
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

        image_source_path = os.path.join(source_images_folder, image_name)
        image_dest_path = os.path.join(class_folder, image_name)
        shutil.copy(image_source_path, image_dest_path)

def main():
    main_folder = 'Main_folder'
    image_txt_file = 'image_list.txt'
    source_images_folder = 'source_images'
    num_classes = 101

    # Create class folders
    create_class_folders(main_folder, num_classes)

    # Move images to class folders
    move_images_to_class_folders(image_txt_file, source_images_folder, main_folder)

if __name__ == "__main__":
    main()
