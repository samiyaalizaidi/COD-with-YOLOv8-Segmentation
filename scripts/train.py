"""
train.py
    Script to train the YOLOv8 Segmentation model.
"""
# import the library
from ultralytics import YOLO

# path to the YAML file
dataset = ""

# load the pretrained models
model = YOLO('yolov8n-seg.yaml')
model = YOLO('yolov8n-seg.pt')

# name of the dataset
name = ""

# set parameters
epochs = 100
batch_size = 8
early_stopping = 50

# train
custom_model = model.train(data=dataset,
                           epochs=epochs,
                           batch=batch_size,
                           patience=early_stopping,
                           name=name)
