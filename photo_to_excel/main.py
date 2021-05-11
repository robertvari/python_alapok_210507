from PIL import Image
import os

ext_list = [".jpg", ".jpeg", ".png"]
folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"
file_list = os.listdir(folder_path)

photo_list = [ i for i in file_list if ".jpg" in i.lower()]


# for i in file_list:
#     name, ext = os.path.splitext(i)
#     if ext.lower() not in ext_list:
#         continue
#     photo_list.append(i)

print(photo_list)