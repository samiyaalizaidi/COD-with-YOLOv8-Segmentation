import os
import cv2
from tqdm import tqdm
from pathlib import Path
from ultralytics import YOLO

def process_images(input_dir, output_dir, model_path):
    # Load fine-tuned YOLOv5 model
    model = YOLO(model_path)

    # Create output directory for predictions to be saved
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    counter = 0

    for img_name in tqdm(os.listdir(input_dir)):
        if img_name.endswith('.png'):
            img_path = os.path.join(input_dir, img_name)
            orig_img_name = img_name.rstrip(".png")

            # Read image using cv2
            test_img = cv2.imread(img_path)

            # Predict on test_img
            try:
                results = model.predict(source=test_img.copy(), save=False)
                for result in results.xyxy:
                    for obj in result:
                        # Extract class label and bounding box coordinates
                        label = int(obj[5])
                        conf = obj[4]
                        if conf > 0.5:  # Consider only detections with confidence > 0.5
                            x_min, y_min, x_max, y_max = map(int, obj[:4])

                            # Draw bounding box on the image
                            cv2.rectangle(test_img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                            # Write class label and confidence on the image
                            label_text = f"{model.names[label]}: {conf:.2f}"
                            cv2.putText(test_img, label_text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Save the image with bounding boxes
                cv2.imwrite(os.path.join(output_dir, f'{orig_img_name}_segmented.png'), test_img)
            except Exception as e:
                counter += 1
                print(f"Error: {e}")
                print(f'Image Name: {orig_img_name}')

    print(f'Corrupted Images: {counter}')

# Usage | Following values need to be adjusted at the time of execution based on relevant experiment requirement
INPUT_DIR = "/home/ah07065/Micro/Data_Split/test/images/"
OUTPUT_DIR = "/home/ah07065/Micro/Results/"
MODEL_PATH = "/home/ah07065/Micro/runs/segment/Micro Segmentation/weights/best.pt"

process_images(input_dir=INPUT_DIR, output_dir=OUTPUT_DIR, model_path=MODEL_PATH)
