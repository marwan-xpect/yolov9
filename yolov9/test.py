# import torch
# from pathlib import Path
# from models.common import DetectMultiBackend
# from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
# from utils.general import (
#     check_img_size, scale_boxes, non_max_suppression
# )
# from utils.torch_utils import select_device, smart_inference_mode
from utils.plots import Annotator, colors
import cv2
import matplotlib.patches as patches

import numpy as np
import matplotlib.pyplot as plt



# Create a batch of dummy images
num_images = 5  # Simulate 5 images
dummy_images = [np.ones((640, 640, 3), dtype=np.uint8) * 255 for _ in range(num_images)]

# Loop through each dummy image
for idx, dummy_image in enumerate(dummy_images):
    plt.figure(figsize=(8, 6))
    plt.imshow(dummy_image)
    plt.axis('off')
    plt.title(f"Dummy Image {idx + 1}")
    plt.show()
    plt.close()  # Close the figure after showing to avoid memory issues
