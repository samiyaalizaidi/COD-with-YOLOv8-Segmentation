from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image

model = YOLO("../best.pt")

test_img_directory = "../CAMO-Labels/test/camourflage_00090.jpg"

results = model.predict(source=test_img_directory, conf=0.3)

results_array = results[0].plot()
imgplot = plt.imshow(results_array)

# plt.figure(figsize=(12, 12))
# plt.imshow(results_array)
# plt.show()



