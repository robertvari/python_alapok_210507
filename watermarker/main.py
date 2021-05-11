from PIL import Image, ImageDraw, ImageFont
import os

ext_list = [".jpg", ".jpeg"]
folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"
dest_folder = os.path.join(folder_path, "_watermarked")
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

file_list = [i for i in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, i))]
photo_list = [i for i in file_list if os.path.splitext(i)[1].lower() in ext_list]

for image in photo_list:
    file_name, ext = os.path.splitext(image)
    image_file = os.path.join(folder_path, image)

    # open image with PIL
    img = Image.open(image_file)
    img.thumbnail((500, 500))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 30)
    draw.text((10, 10), "Hello World", fill=(255, 0, 0), font=font)

    new_image_file = os.path.join(dest_folder, f"{file_name}_watermarked{ext}")
    img.save(new_image_file)