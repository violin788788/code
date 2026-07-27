from PIL import Image
import os,sys

input_directory = "cheka"

imgs = [f for f in os.listdir(input_directory) if f.lower().endswith(".png")]


imgs = sorted(
    imgs,
    key=lambda x: int(x.split("_")[1].split(".")[0])
)


images = []
for f in imgs:
    img = Image.open(os.path.join(input_directory, f)).convert("RGB")
    images.append(img)
    print(f)

out_name = os.path.basename(os.path.normpath(input_directory)) + ".pdf"
if images:
    images[0].save(out_name, save_all=True, append_images=images[1:])