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
  counter = 0

  for img_name in tqdm(os.listdir(input_dir)):
    if img_name.endswith('.png'):
      img_path = os.path.join(input_dir, img_name)
      orig_img_name = img_name.rstrip(".png")

      # read image using cv2
      test_img = cv2.imread(img_path)

      # predict on test_img
      try:
        results = model.predict(source=test_img.copy(), save=False, save_txt=True)
        seg_classes = list(results[0].names.values())

        for result in results:
          masks = result.masks.data
          boxes = result.boxes.data
          clss = boxes[:, 5]

          # Select a color for visualization (adjust as needed)
          mask_color = (0, 255, 0)  # Green for segmentation

          # Convert mask to a format suitable for OpenCV
          mask = masks[0].cpu().numpy().astype('uint8') * 255  # Assuming single class mask
          mask = cv2.resize(mask, (test_img.shape[1], test_img.shape[0]), interpolation=cv2.INTER_NEAREST)

          # Apply transparency based on mask values (adjust alpha value as needed)
          alpha = 0.5  # Transparency level (0 - fully transparent, 1 - fully opaque)
          mask_overlay = cv2.addWeighted(test_img.copy(), 1 - alpha, mask[..., None], alpha, 0)

          # Display or save the image with the mask overlay
          # cv2.imshow('Image with Mask', mask_overlay)  # Uncomment to display image
          cv2.imwrite(os.path.join(output_dir, f'{orig_img_name}_masked.png'), mask_overlay)

      except Exception as e:
        counter += 1
        print(f"error: {e}")
        print("\n" * 3)
        print(f'Image Name {orig_img_name}')
        print("\n" * 3)

  print(f'Corrupted Images {counter}')

# Usage (same as before)
