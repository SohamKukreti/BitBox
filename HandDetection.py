import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)



offset = 20
imgSize = 300
counter = 0
folder = "Data/A"

while True:
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

    if key == ord('s'):
        cv2.imwrite(f"{folder}/Image_{counter}.jpg",imgWhite)
        print(counter)
        counter+=1
    if key == 27:
        cv2.destroyAllWindows()
        sys.exit()
