from PIL import Image

# Open an image
image_name = "run"
image_extension = "png"
image_file = image_name+"."+image_extension

image = Image.open(image_file)

# Save as .ico format
ico_file = image_name+".ico"
image.save(ico_file, format="ICO")
