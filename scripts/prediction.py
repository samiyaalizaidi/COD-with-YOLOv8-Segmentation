import os
import cv2
import torch
from tqdm import tqdm
from pathlib import Path
from ultralytics import YOLO

def process_images(input_dir, output_dir, model_path):
  # Load fine tuned YOLOv8(n,m,x)-seg model
  model = YOLO(model_path)

  # Create output directory for predictions to be saved (optional)
  Path(output_dir).mkdir(parents=True, exist_ok=True)
  counter = 0

  for img_name in tqdm(os.listdir(input_dir)):
    if img_name.endswith('.png'):
      img_path = os.path.join(input_dir, img_name)
      orig_img_name = img_name.rstrip(".png")

      # Read image using cv2
      test_img = cv2.imread(img_path)
      test_img_copy = test_img.copy()  # Avoid modifying original image

      # Predict on test image
      try:
        results = model.predict(source=test_img_copy)

        # Loop through predictions for this image
        for result in results:
          # Get masks and bounding boxes
          masks = result.masks.data
          boxes = result.boxes.data

          # Process each detected object
          for i in range(len(masks)):
            mask = masks[i]  # Get individual mask for each object
            box = boxes[i]  # Get corresponding bounding box (optional)

            # Convert mask to a format suitable for OpenCV (uint8 with values 0-255)
            mask = (mask * 255).byte().cpu().numpy()

            # Apply mask to the original image (weighted average for transparency)
            alpha = 0.4  # Adjust alpha for transparency of the mask
            masked_image = cv2.addWeighted(test_img_copy, 1 - alpha, mask, alpha, 0)

            # Optionally draw bounding box (modify as needed)
            # x_min, y_min, x_max, y_max = box.int().tolist()
            # cv2.rectangle(masked_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Display or save the masked image (modify as needed)
            # cv2.imshow(f"Segmented Image - {orig_img_name}", masked_image)
            # cv2.waitKey(0)
            cv2.imwrite(os.path.join(output_dir, f'{orig_img_name}_masked.png'), masked_image)

      except Exception as e:
        counter += 1
        print(f"Error: {e}")
        print("\n" * 3)
        print(f'Image Name {orig_img_name}')
        print("\n" * 3)

  print(f'Corrupted Images {counter}')

# Usage (modify paths as needed)
INPUT_DIR = "/home/ah07065/Micro/Data_Split/test/images/"
OUTPUT_DIR = "/home/ah07065/Micro/getpred/"  # Adjust for masked image output
MODEL_PATH = "/home/ah07065/Micro/runs/segment/Micro Segmentation/weights/best.pt"

process_images(input_dir=INPUT_DIR, output_dir=OUTPUT_DIR, model_path=MODEL_PATH)
