from PIL import Image
from openpyxl import Workbook
import os

ext_list = [".jpg", ".jpeg"]
folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"

file_list = [i for i in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, i))]
photo_list = [i for i in file_list if os.path.splitext(i)[1].lower() in ext_list]

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "Name"
sheet["B1"] = "Path"
sheet["C1"] = "Date"
sheet["D1"] = "Camera"
sheet["E1"] = "Lens"
sheet["F1"] = "ISO"
sheet["G1"] = "Dimensions"


for index, image_file in enumerate(photo_list):
    full_image_path = os.path.join(folder_path, image_file)
    img = Image.open(full_image_path)
    img_size = img.size

    row = index + 3
    sheet[f"A{row}"] = image_file
    sheet[f"B{row}"] = full_image_path
    sheet[f"G{row}"] = f"{img_size[0]} * {img_size[1]}"

    exif_data = img._getexif()

    if exif_data:
        sheet[f"C{row}"] = exif_data[306]

excel_file = os.path.join(folder_path, "photo_data.xlsx")
workbook.save(excel_file)