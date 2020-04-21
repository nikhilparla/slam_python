#! /usr/bin/python3

import time
import cv2
cv2.namedWindow("Input")

W = 1920//2
H = 1080//2

def process_frame(img):
    #print(img.shape)
    img = cv2.resize(img, (W,H))
    cv2.imshow("Input",img)
    cv2.waitKey(33)
    #print(img.shape)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test_video.mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret==True:
            process_frame(frame)
        else:
            break
