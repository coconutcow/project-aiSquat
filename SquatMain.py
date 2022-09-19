import cv2
import time
import SquatModule as sq
import numpy as np
# With videos
cap = cv2.VideoCapture('SquatVideos/video2.mp4')
# Real-time with webcam
# cap = cv2.VideoCapture(0)

detector = sq.poseDetector()
count = 0
dir = 0
beginTime=0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1200, 720))
    # img = cv2.imread("SquatVideos/img1.jpg")

    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    # print(lmList)
    if len(lmList) != 0:
        # Destra
        angle = detector.findAngle(img, 24, 26, 28)
        # Sinistra
        # detector.findAngle(img, 23, 25, 27)
        per = np.interp(angle, (200, 280), (0, 100))
        # print(angle, per)
        bar=np.interp(angle,(200,280),(650,100))
        # Check for complete squat
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # Draw Bar
        # cv2.rectangle(img, (1100, 100), (1150, 650), (0, 0, 0), 3)
        # cv2.rectangle(img, (1100, int(bar)), (1150, 650), (0, 0, 0), cv2.FILLED)
        # cv2.putText(img, f'{int(per)}%', (1075, 75), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)

        # Draw Squat Count
        cv2.rectangle(img,(0,0),(90,90),(0,0,0),cv2.FILLED)
        cv2.putText(img,str(int(count)),(25,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)


    # currentTime=time.time()
    # fps=1/(currentTime-beginTime)
    # beginTime=currentTime
    # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 10)
    cv2.imshow("Image", img)

    cv2.waitKey(1)
