import os
import cv2
import torch
from tqdm import tqdm
from pathlib import Path
from ultralytics import YOLO

def process_images(input_dir, output_dir, model_path):
    # load fine tuned YOLOv8(n,m,x)-seg model
    model = YOLO(model_path)

    # create output directory for predictions to be saved
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    counter =0


    for img_name in tqdm(os.listdir(input_dir)):
        if img_name.endswith('.jpg'):
            img_path = os.path.join(input_dir, img_name)
            orig_img_name = img_name.rstrip(".jpg")

            # read image using cv2
            test_img = cv2.imread(img_path)
            
            # predict on test_img
            try:
              results = model.predict(source=test_img.copy(), save=True, save_txt=True)
              #print("check out" , " " ,results)
              seg_classes = list(results[0].names.values())


              for result in results:
                  masks = result.masks.data
                  boxes = result.boxes.data
                  clss = boxes[:, 5]

                  #EXTRACT A SINGLE MASK WITH ALL THE CLASSES
                  obj_indices = torch.where(clss != -1)
                  obj_masks = masks[obj_indices]
                  obj_mask = torch.any(obj_masks, dim=0).int() * 255

                  # Saving the binary mask output of the prediction
                  cv2.imwrite(os.path.join(output_dir, f'{orig_img_name}_binary_mask.jpg'), obj_mask.cpu().numpy())
            except Exception as e:
              counter+=1
              print(f"error: {e}")
              print("\n"*3)
              print(f'Image Name {orig_img_name}')
              print("\n"*3)
    print(f'Corrupted Images {counter}')
              
# usage | following values need to adjusted at the time of execution based on relevant experiment requirement
INPUT_DIR = "/content/CAMO/test/images/"
OUTPUT_DIR = "./test_output1/"
MODEL_PATH = "/content/best.pt"

process_images(input_dir=INPUT_DIR, output_dir=OUTPUT_DIR, model_path=MODEL_PATH)
