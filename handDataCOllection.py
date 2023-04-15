import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)



offset = 20
imgSize = 300
counter = 0
folderLetter = "A"
folder = f"Data/{folderLetter}"

while True:
    folder = f"Data/{folderLetter}"
    success, img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand["bbox"]

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape = imgCrop.shape



        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize / h
            wcal = math.ceil(w*k)
            if imgCrop.size > 0:
                imgResize = cv2.resize(imgCrop, (wcal, imgSize))
            else:
                continue
            imgResizeShape = imgResize.shape
            wgap = math.ceil((300-wcal)/2)
            imgWhite[ : , wgap:wcal+wgap] = imgResize


        elif aspectRatio < 1:
            k = imgSize / w
            hcal = math.ceil(h*k)
            if imgCrop.size > 0:
                imgResize = cv2.resize(imgCrop,(imgSize,hcal))
            else:
                continue
            imgResizeShape = imgResize.shape
            hgap = math.ceil((300-hcal)/2)
            imgWhite[hgap:hcal+hgap, : ] = imgResize



        cv2.imshow("ImageWhite",imgWhite)
        cv2.imshow("ImageCrop",imgCrop)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)

    if key == 13:
        cv2.imwrite(f"{folder}/Image_new{time.time()}.jpg",imgWhite)
        print(counter)
        counter+=1
    elif key == ord('a'):
        folderLetter = "A"
        counter = 0
    elif key == ord('b'):
        folderLetter = "B"
        counter = 0
    elif key == ord('c'):
        folderLetter = "C"
        counter = 0
    elif key == ord('d'):
        folderLetter = "D"
        counter = 0
    elif key == ord('e'):
        folderLetter = "E"
        counter = 0
    elif key == ord('f'):
        folderLetter = "F"
        counter = 0
    elif key == ord('g'):
        folderLetter = "G"
        counter = 0
    elif key == ord('h'):
        folderLetter = "H"
        counter = 0
    elif key == ord('i'):
        folderLetter = "I"
        counter = 0
    elif key == ord('j'):
        folderLetter = "J"
        counter = 0
    elif key == ord('k'):
        folderLetter = "K"
        counter = 0
    elif key == ord('l'):
        folderLetter = "L"
        counter = 0
    elif key == ord('m'):
        folderLetter = "M"
        counter = 0
    elif key == ord('n'):
        folderLetter = "letterN"
        counter = 0
    elif key == ord('o'):
        folderLetter = "O"
        counter = 0
    elif key == ord('p'):
        folderLetter = "P"
        counter = 0
    elif key == ord('q'):
        folderLetter = "Q"
        counter = 0
    elif key == ord('r'):
        folderLetter = "R"
        counter = 0
    elif key == ord('s'):
        folderLetter = "S"
        counter = 0
    elif key == ord('t'):
        folderLetter = "T"
        counter = 0
    elif key == ord('u'):
        folderLetter = "U"
        counter = 0
    elif key == ord('v'):
        folderLetter = "V"
        counter = 0
    elif key == ord('w'):
        folderLetter = "W"
        counter = 0
    elif key == ord('x'):
        folderLetter = "X"
        counter = 0
    elif key == ord('y'):
        folderLetter = "Y"
        counter = 0
    elif key == ord('z'):
        folderLetter = "Z"
        counter = 0


    if key == 27:
        cv2.destroyAllWindows()
        sys.exit()