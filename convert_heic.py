#!/usr/bin/env python3

import os
import sys

from PIL import Image
from pillow_heif import register_heif_opener

SUPPORTED_FORMATS = {'.png', '.jpg'}


def args_check():
    if len(sys.argv) != 2:
        print("Please provide a valid format as an argument.")
        sys.exit()

    if sys.argv[1] not in SUPPORTED_FORMATS:
        print(f"Invalid format provided: '{sys.argv[1]}'. Choose one of the supported formats: '{SUPPORTED_FORMATS}'")
        sys.exit()


def batch_convert_heic_to_jpg():
    for photo in os.listdir():
        if not photo.endswith('.HEIC'):
            continue

        try:
            with Image.open(photo) as img:
                converted_photo = photo.replace('.HEIC', '.jpg')
                img.save(converted_img)
                print(f"Successfully converted '{photo}' to '{converted_photo}'")
        except Exception as e:
            print(f"Failed to convert {photo}: {str(e)}")


if __name__ == "__main__":
    args_check()
    register_heif_opener()
    batch_convert_heic_to_jpg()
