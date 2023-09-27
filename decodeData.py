import cv2
import numpy as np

from PIL import Image


def decodeData():
    stringBinary = ""
    message = ""
    counter = 0
    img = cv2.imread("Alu_with_text.bmp")
    h, w, c = img.shape
    for i in range(0, h):
        for j in range(0, w):
            for c in range(0, 3):
                if counter < 20:
                    binColorValue = list(format(img[i][j][c], "08b"))
                    stringBinary = stringBinary + binColorValue[7]
                    if binColorValue[7] == "0":
                        counter = counter + 1
                    else:
                        counter = 0
    while stringBinary != "":
        i = chr(int(stringBinary[:8], 2))
        message = message + i
        stringBinary = stringBinary[8:]
    return message


print("Hidden text: ", decodeData())
