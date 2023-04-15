def phrase():
    import cv2
    from cvzone.HandTrackingModule import HandDetector
    from cvzone.ClassificationModule import Classifier
    import numpy as np

    import math
    import sys


    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands = 1)
    classifier = Classifier("Model/keras_model.h5","Model/labels.txt")


    offset = 20
    imgSize = 300

    folder = "Data\C"
    counter = 0

    labels = ["Stop","Goodbye","S.O.S","How are You ? ","Everything ok ?","Thank you","Please , Excuse me","Hello","Sorry","I need Help","Lets Go","I do not understand","Stop","Goodbye","S.O.S","How are You ? ","Everything ok ?","Thank you","Please , Excuse me","Hello","Sorry","I need Help","Lets Go","I do not understand","Lets Go","I do not understand"]
    str = ""

    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x,y,w,h = hand['bbox']

            imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

            imgCrop = img[y - offset:y+h+offset,x - offset:x+w+offset]
            imgCropShape = imgCrop.shape


            aspectRatio = h/w

            if aspectRatio > 1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                if imgCrop.size > 0:
                   imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                else:
                    continue
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal)/2)
                if (x > 0 + offset and y > 0 + offset and w > 0 + offset and h > 0 + offset):
                    imgWhite[0:imgResizeShape[0], wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite)
                print(prediction,index)
                text = cv2.putText(imgOutput, f"{labels[index]}", (100,100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (17, 17, 17), 2,
                                   cv2.LINE_AA)
            elif aspectRatio < 1:
                k = imgSize/w
                hCal = math.ceil(k*h)
                if imgCrop.size > 0:
                    imgResize = cv2.resize(imgCrop,(imgSize,hCal))
                else:
                    continue
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal)/2)
                prediction, index = classifier.getPrediction(imgWhite)
                print(prediction, index)
                text = cv2.putText(imgOutput, f"{labels[index]}", (100, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (17, 17, 17), 2,
                                   cv2.LINE_AA)

        cv2.imshow("Image",imgOutput)

        key = cv2.waitKey(1)
        if key == 13:
            str+=labels[index]
        if key == ord("p"):
            print(str)
        if key == 32:
            str += " "
        if key == 8:
            str = str[:-1]
        if key == 27:
            cv2.destroyAllWindows()
            return str
