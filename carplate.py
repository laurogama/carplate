import subprocess
import time

from SimpleCV import Camera, Image

from Settings import *


__author__ = 'laurogama'


def take_picture():
    # Initialize the camera
    cam = Camera(0, {"width": 1280, "height": 1024})
    # Get Image from camera
    return cam.getImage()


def process_image():
    # img = take_picture()
    print "Opening image"
    img = Image(IMAGES_PATH + EXAMPLE)

    # Loop to continuously get images
    # while True:

    # Make image black and white
    print "Make image grayscale"
    img2 = img.grayscale()
    img2.save(filename=GRAYSCALE)
    # img2.applyIntensityCurve()

    print "Applying gaussian filter"
    img3 = img2.applyGaussianFilter(dia=200, highpass=True, grayscale=True)
    img3.save(filename=IMAGES_PATH + "gaussian")
    img4 = img3.binarize()
    print "Binarizing"
    img4.save(filename=BINARIZED)

    # we invert because blobs looks for white blobs, not black
    print "inverting"
    img5 = img4.invert()
    img5.save(filename=INVERTED)
    print "finding blobs"
    # you can always change parameters to find different sized blobs
    plate = img5.findBlobs()
    if plate:
        # if it finds blobs then draw around them
        plate.draw()
    img5.show()
    subprocess.call(["tesseract", INVERTED + ".png", OUTPUT_TEXT_FILE])
    time.sleep(10)


if __name__ == "__main__":
    # take_picture()
    process_image()