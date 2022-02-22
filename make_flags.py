import os
import shutil
from PIL import Image, ImageDraw

def main():
    source_dir = "res\\content\\gameplay\\common\\flags"
    target_dir = "out\\content\\gameplay\\common\\flags"

    shutil.rmtree(target_dir, ignore_errors=True)
    os.makedirs(target_dir)

    flags = os.listdir(source_dir)
    for filename in flags:
        print(filename)
        target_image = os.path.join(target_dir, filename)
        flag = Image.new('RGBA', (4, 4), (0, 0, 0, 0))
        flag.save(target_image, "DDS")


main()
