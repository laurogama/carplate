ORIGINAL = "images/original.jpg"
BINARIZED = "images/binarized.jpg"
__author__ = 'laurogama'

from SimpleCV import Camera


def take_picture():
    # Initialize the camera

    cam = Camera(0, {"width": 1280, "height": 1024})
    # Loop to continuously get images
    # while True:
    # Get Image from camera
    cam.getImage().save(ORIGINAL)
    # img = Image(ORIGINAL)
    # Make image black and white
    # img = img.binarize().save(BINARIZED)

