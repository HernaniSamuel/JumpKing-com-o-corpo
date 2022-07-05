import cv2
import mediapipe as mp
import pyautogui

video = cv2.VideoCapture(0)

pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils


while True:
    sucess, img = video.read()
    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape
    
    if points:
        ce = int(points.landmark[pose.PoseLandmark.LEFT_ELBOW].y*h)
        cd = int(points.landmark[pose.PoseLandmark.RIGHT_ELBOW].y*h)
        me = int(points.landmark[pose.PoseLandmark.LEFT_WRIST].y*h)
        md = int(points.landmark[pose.PoseLandmark.RIGHT_WRIST].y*h)
        oe = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].y*h)
        od = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].y*h)

        if me < ce and md > cd:
            pyautogui.keyDown('left')
        if me > ce:
            pyautogui.keyUp('left')

        if md < cd and me > ce:
            pyautogui.keyDown('right')
        if md > cd:
            pyautogui.keyUp('right')

        if me < ce and md < cd:
            pyautogui.press(['esc'])

        if oe > h/2 and od > h/2:
            pyautogui.keyDown('space')
        if oe < h/2 and od < h/2:
            pyautogui.keyUp('space')

    cv2.imshow('Teste', img)
    cv2.waitKey(5)
