import cv2

from Settings import IMAGES_PATH, EXAMPLE, GRAYSCALE, MEDIAN_FILTER, THRESHOLD, ERODED, OUTPUT_TEXT_FILE, \
    ALLOWED_FILE_FORMAT


__author__ = 'laurogama'
import subprocess

from SimpleCV import Camera, Image


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

    histogram = img.histogram()
    img = img.grayscale()
    img.save(filename=GRAYSCALE)
    # img2.applyIntensityCurve()
    img = img.medianFilter()
    img.save(filename=MEDIAN_FILTER)
    print "Applying gaussian filter"
    img = img.applyGaussianFilter(dia=200, highpass=True, grayscale=True)
    img.save(filename=IMAGES_PATH + "gaussian")
    img = img.threshold(50)
    img.save(filename=THRESHOLD)
    print "Applying eroding"
    img = img.erode(1)
    img.save(filename=ERODED)
    # print "Binarizing"
    # img4 = img3.binarize()
    # img4.save(filename=BINARIZED)

    # we invert because blobs looks for white blobs, not black
    # only used with Binarized
    # print "inverting"
    # img = img.invert()
    # img.save(filename=INVERTED)
    print "finding blobs"
    # you can always change parameters to find different sized blobs
    plate = img.findBlobs()
    if plate:
        # if it finds blobs then draw around them
        plate.draw()
    # img.show()
    # time.sleep(10)
    return True


def recognize_face(picture_path=None):
    if picture_path:
        print "opening file : " + picture_path
        img = cv2.imread(picture_path)
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        print "Recognizing faces"
        face_cascade = cv2.CascadeClassifier('ocr/data/haarcascades/haarcascade_frontalface_default.xml')
        # face_cascade = cv2.CascadeClassifier('data/lbpcascades/lbpcascade_frontalface.xml')
        eye_cascade = cv2.CascadeClassifier('ocr/data/haarcascades/haarcascade_eye.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        if len(faces)>0:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.imshow('img', img)
            print "click to end program"
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return None
        print "Face not recognized"
        return
    print "Filepath empty"


def execute_tesseract(filename=None):
    if filename is not None:
        subprocess.call(["tesseract", filename, OUTPUT_TEXT_FILE])
        return True
    return False


def execute_ocr():
    process_image()
    execute_tesseract(THRESHOLD + ".png")


def is_format_supported(filename):
    for file_format in ALLOWED_FILE_FORMAT:
        if str(filename).endswith(file_format):
            return True
    return False