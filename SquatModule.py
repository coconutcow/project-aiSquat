import cv2
import mediapipe as mp
import time
import math


class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 255, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        x1,y1=self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]


        # Calculate Angles
        angle = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle += 360
        # elif angle>180:
        #     angle=360-angle
        print(angle)

        # Draw Points and Lines
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)
            cv2.line(img,(x2,y2),(x3,y3),(255,255,255),2)
            cv2.circle(img, (x1, y1), 5, (0, 255, 204), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (0, 255, 204), 2)
            cv2.circle(img, (x2, y2), 5, (0, 255, 204), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 255, 204), 2)
            cv2.circle(img, (x3, y3), 5, (0, 255, 204), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (0, 255, 204), 2)
            cv2.putText(img, "aiSquat/sabharwal.dev", (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
            cv2.putText(img,str(int(angle)),(x2-200,y2+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)

        return angle

def main():
    cap = cv2.VideoCapture(0)
    beginTime = 0

    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        #
        # if len(lmList):
        #     print(lmList)
        if len(lmList) != 0:
            detector.findAngle(img, 24, 26, 28)

        currentTime = time.time()

        fps = 1 / (currentTime - beginTime)

        beginTime = currentTime

        cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
