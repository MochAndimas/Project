"""module compresser

Put this module in the same directory images you want to compress
"""

import os
from PIL import Image
import performance_decorator


@performance_decorator.performance
def landscape(imgdir, savefldr):
    """CONVERTER landscape"""

    image = os.listdir(imgdir)
    check_folder = os.path.exists(savefldr)

    if not check_folder:
        os.makedirs(savefldr)

    for filename in image:
        img = Image.open(f"{imgdir}/{filename}")
        img_compress = img.resize((1080, 777), Image.ANTIALIAS)
        clean_name = os.path.splitext(filename)[0]
        img_compress.save(f"{savefldr}/{clean_name}.png",
                          optimize=True, quality=90)
        print("all done!!")


@performance_decorator.performance
def portrait(imgdir, savefldr):
    """CONVERTER portrait"""

    image = os.listdir(imgdir)
    check_folder = os.path.exists(savefldr)

    if not check_folder:
        os.makedirs(savefldr)

    for filename in image:
        img = Image.open(f"{imgdir}/{filename}")
        img_compress = img.resize((1080, 1350), Image.ANTIALIAS)
        clean_name = os.path.splitext(filename)[0]
        img_compress.save(f"{savefldr}/{clean_name}.png",
                          optimize=True, quality=90)
        print("all done!!")


if __name__ == "__main__":
    # landscape(input("image folder? "), input("where to save? "))
    portrait(input("image folder? "), input("where to save? "))
