import matplotlib.pyplot as plt

# Define the sizes of the datasets
colors = ['violet', 'lightblue', 'yellow', 'red', 'blue']
dataset_sizes = [10000, 18321, 4121, 1250, 76]
dataset_labels = ['COD10K', 'MoCA', 'NC4K', 'CAMO', 'CHAMELEON']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(dataset_sizes, labels=dataset_labels, autopct='%1.1f%%', startangle=140, colors=colors)
# plt.title('Distribution of Datasets')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
