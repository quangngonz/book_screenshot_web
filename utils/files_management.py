import os

def get_sorted_files(directory):
    files = os.listdir(directory)
    indexed_files = []

    # Extract indexes and sort files
    extracted = [(int(file.split('_')[1].split('.')[0]), file) for file in files]
    extracted.sort()  # Sort based on the extracted index

    mapped_index = {}
    next_index = 1

    for original_index, file in extracted:
        if original_index == 0:
            mapped_index[original_index] = 0
            indexed_files.append((original_index, file, 0))
        else:
            mapped_index[original_index] = next_index
            indexed_files.append((original_index, file, next_index, next_index + 1))
            next_index += 1

    return indexed_files, extracted

def load_images_in_order(directory):
    files = sorted(os.listdir(directory), key=lambda x: (int(x.split('_')[0]) if '_' in x else 0, x))
    ordered_images = [os.path.join(directory, file) for file in files]
    return ordered_images
