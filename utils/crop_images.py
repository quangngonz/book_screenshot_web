import os
from PIL import Image
import threading

def crop_and_split_image(image_path, index, last_index):
    image = Image.open(image_path)
    crop_box = (986, 186, 6698, 4220)
    cropped_image = image.crop(crop_box)

    if index == 0 or index == last_index:
        crop_box = (2372, 186, 5314, 4220)
        cropped_image = image.crop(crop_box)
        filename = os.path.basename(image_path)
        cropped_image.save(os.path.join("crop", f'{index}.png'))
        print(f"Cropped image saved to crop/{filename}")
    else:
        width, height = cropped_image.size
        left_half = cropped_image.crop((0, 0, width // 2, height))
        right_half = cropped_image.crop((width // 2, 0, width, height))
        
        left_filename = f"{index}_L.png"
        right_filename = f"{index}_R.png"
        
        left_half.save(os.path.join("crop", left_filename))
        right_half.save(os.path.join("crop", right_filename))
        
        print(f"Cropped and split images saved: {left_filename}, {right_filename}")

def crop_images(image_paths, indexed_files):
    threads = []
    last_index = len(image_paths) - 1

    os.makedirs("crop", exist_ok=True)

    for file in os.listdir("crop"):
        os.remove(f"crop/{file}")

    for image_path, (_, file, index, *_) in zip(image_paths, indexed_files):
        thread = threading.Thread(target=crop_and_split_image, args=(image_path, index, last_index))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
