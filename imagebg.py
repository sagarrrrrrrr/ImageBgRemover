from PIL import Image
from rembg import remove

input_path = input("Image path: ").strip().strip("'")
output_path = input("Save as: ").strip().strip('"')

with Image.open(input_path) as img:
    result = remove(img)

if output_path.lower().endswith(".png") or output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
    result = result.convert("RGB")

result.save(output_path)

#C:\Users\sagar\Desktop\Imagebgremover