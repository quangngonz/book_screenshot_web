import os
from PIL import Image

from utils.files_management import get_sorted_files, load_images_in_order
from utils.crop_images import crop_images

SCREENSHOT_DIR = 'screenshots'

import os

# Get the sorted files and indexed files
indexed_files, sorted_files = get_sorted_files(SCREENSHOT_DIR)

# Get the image paths
image_paths = [os.path.join(SCREENSHOT_DIR, file[1]) for file in sorted_files]

# Crop the images
crop_images(image_paths, indexed_files)

# Load the cropped images
image = load_images_in_order('crop')

def create_pdf(image_paths, output_pdf, compress_images=False, max_size=(2480, 3508), quality=85):
    if not image_paths:
        print("No images to process.")
        return

    processed_images = []

    for img_path in image_paths:
        with Image.open(img_path) as img:
            img = img.convert("RGB")  # Ensure RGB format
            
            if compress_images:
                img.thumbnail(max_size)  # Resize while keeping aspect ratio
                
                # Save a compressed version in the same directory
                temp_path = img_path.replace('.png', '_compressed.jpg').replace('.jpeg', '_compressed.jpg')
                img.save(temp_path, "JPEG", quality=quality)
                processed_images.append(temp_path)
            else:
                processed_images.append(img_path)

    # Open processed images
    images = [Image.open(img) for img in processed_images]
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

# Create a PDF
create_pdf(image, "output.pdf")
