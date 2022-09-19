import cv2
import time
import SquatModule as sq

cap = cv2.VideoCapture(0)
beginTime = 0

detector = sq.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    if len(lmList):
        print(lmList)
    currentTime = time.time()

    fps = 1 / (currentTime - beginTime)

    beginTime = currentTime

    cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)

    cv2.waitKey(1)
