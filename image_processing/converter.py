"""module converter

put this module in the same directory images you want to convert
"""

import os
from PIL import Image
import performance_decorator


@performance_decorator.performance
def image_converter(imgdir, savefldr):
    """CONVERTER MODULE"""

    check_folder = os.path.exists(savefldr)
    image = os.listdir(imgdir)

    if not check_folder:
        os.makedirs(savefldr)

    for filename in image:
        img = Image.open(f"{imgdir}/{filename}")
        clean_name = os.path.splitext(filename)[0]
        img.save(f"{savefldr}/{clean_name}.png", "png")
        print("all done!!")


if __name__ == "__main__":
    image_converter(input("image folder? "), input("where to save? "))
