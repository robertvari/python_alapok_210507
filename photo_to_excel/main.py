from PIL import Image
import os

folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"
file_list = os.listdir(folder_path)

photo_list = []
ext_list = [".jpg", ".jpeg", ".png"]
for i in file_list:
    name, ext = os.path.splitext(i)
    if ext.lower() not in ext_list:
        continue
    photo_list.append(i)

print(photo_list)