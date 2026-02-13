from PIL import Image
import pillow_heif
import os

# Register HEIF opener
pillow_heif.register_heif_opener()

directory = 'Valentines' # Your folder name

for filename in os.listdir(directory):
    if filename.upper().endswith(".HEIC"):
        filepath = os.path.join(directory, filename)
        img = Image.open(filepath)
        # Save as JPG
        img.save(filepath.replace('.HEIC', '.jpg').replace('.heic', '.jpg'), "JPEG")
        print(f"Converted {filename}")