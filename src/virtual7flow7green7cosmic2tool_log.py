# Development Log
# Started at 2025-04-03 09:06:17

# Added some random functionality
# Improved performance


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Update at 2025-04-04 04:10:04
# Optimized the algorithm
# Refactored the code


from PIL import Image

def resize_image(image_path, size):
    with Image.open(image_path) as img:
        resized = img.resize(size)
        return resized

def convert_to_grayscale(image_path):
    with Image.open(image_path) as img:
        return img.convert('L')