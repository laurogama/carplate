import os

from ocr.OCR import is_format_supported, recognize_face

__author__ = 'laurogama'


def loop_image_files(dir_path):
    files = []
    for fn in os.listdir(dir_path):
        if is_format_supported(fn):
            files.append(os.path.join(dir_path, fn))
    return files


if __name__ == "__main__":
    images = loop_image_files("images")
    for image in images:
        recognize_face(image)