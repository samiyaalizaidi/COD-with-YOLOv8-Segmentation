import matplotlib.pyplot as plt
import numpy as np

# Define multiple datasets (you can modify this according to your datasets)
datasets = {
    'COD-10K': {'total_images': 6000, 'images_used': 4000},
    'MoCA': {'total_images': 37000, 'images_used': 4000},
    'NC4K': {'total_images': 4121, 'images_used': 4000}
}

# Prepare data for the bar chart
categories = ['Images Used', 'Images Unused']
dataset_names = list(datasets.keys())
num_datasets = len(dataset_names)
bar_width = 0.5  # Width of the bars

# Calculate the number of unused images and used images for each dataset
unused_images = [datasets[name]['total_images'] - datasets[name]['images_used'] for name in dataset_names]
used_images = [datasets[name]['images_used'] for name in dataset_names]

# Create the bar chart
plt.figure(figsize=(8, 8))

# Plot bars for unused images
bars1 = plt.bar(dataset_names, used_images, color='lightblue', label='Images Being Used', width=bar_width)

# Plot bars for used images on top of the unused images
bars2 = plt.bar(dataset_names, unused_images, bottom=used_images, color='purple', label='Images Not Being Used', width=bar_width)

# Adding labels and title
plt.xlabel('Datasets')
plt.ylabel('Number of Images')
plt.title('Actual Number of Images vs. Images Being Used in the Dataset')
plt.legend()

# Display the bar chart
plt.show()
