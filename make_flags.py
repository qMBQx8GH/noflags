import os
import json
from PIL import Image, ImageDraw

def main():
    os.makedirs("out\\content\\gameplay\\common\\flags", exist_ok=True)

    flags = os.listdir('res\\content\\gameplay\\common\\flags')
    for filename in flags:
        source_image = "res\\content\\gameplay\\common\\flags\\%s" % filename
        target_image = "out\\content\\gameplay\\common\\flags\\%s" % filename
        print(source_image)

        flag = Image.open(source_image).convert('RGBA')
        draw = ImageDraw.Draw(flag)
        draw.rectangle([(0,0), flag.size], fill = (0,0,0,0) )

        if os.path.exists(target_image):
            os.unlink(target_image)
        flag.save(target_image, "DDS")


main()
