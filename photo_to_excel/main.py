from PIL import Image
import os

ext_list = [".jpg", ".jpeg"]
folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"

file_list = [i for i in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, i))]
photo_list = [i for i in file_list if os.path.splitext(i)[1].lower() in ext_list]

for image_file in photo_list:
    full_image_path = os.path.join(folder_path, image_file)
    img = Image.open(full_image_path)
    print("-"*100)
    print(f"Image: {image_file}\nPath: {full_image_path}\nSize: {img.size}")