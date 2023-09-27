import cv2
import numpy as np
from PIL import Image


def encodeData(mess):
    binMess = [bin(ord(char))[2:].zfill(8) for char in mess]
    binMess = "".join(binMess)
    binMessList = list(map(int, binMess))
    img = cv2.imread("Alu.bmp")
    # print(img)
    h, w, c = img.shape
    strNum = 0
    for i in range(0, h):
        for j in range(0, w):
            for c in range(0, 3):
                binColorValue = list(format(img[i][j][c], "08b"))
                if strNum < len(str(binMess)):
                    binColorValue[7] = str(binMessList[strNum])
                else:
                    binColorValue[7] = "0"
                img[i][j][c] = int("".join(binColorValue), 2)

                strNum = strNum + 1
    cv2.imwrite("Alu_with_text.bmp", img)
    print("Text has been hidden")


encodeData("This is secret text")
