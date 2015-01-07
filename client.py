from SimpleCV import Image
import cv2

from Settings import IMAGES_PATH
from ocr.OCR import recognize_face

__author__ = 'laurogama'


def test_ocr():
    print "Opening image"
    # img = Image(IMAGES_PATH + "obama.png", cv2image=True)
    # img = cv2.imread(IMAGES_PATH + "obama.png")
    img = cv2.imread(IMAGES_PATH + "obama.png")
    if img is not None:
        print "Recognize faces"
        recognize_face(img)
        return
    print "image not loaded"

if __name__ == "__main__":
    test_ocr()