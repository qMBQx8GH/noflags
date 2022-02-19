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
        source_image = os.path.join(source_dir, filename)
        target_image = os.path.join(target_dir, filename)

        flag = Image.open(source_image).convert('RGBA')
        print(source_image, flag.size)

        draw = ImageDraw.Draw(flag)
        draw.rectangle([(0,0), flag.size], fill = (0,0,0,0) )

        if os.path.exists(target_image):
            os.unlink(target_image)
        flag.save(target_image, "DDS")


main()
