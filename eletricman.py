import cv2
import mediapipe as mp
import pyautogui
from time import sleep

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
        mao_esquerdaY = int(points.landmark[pose.PoseLandmark.LEFT_WRIST].y * h)#15
        mao_esquerdaX = int(points.landmark[pose.PoseLandmark.LEFT_WRIST].x * w)#15

        mao_direitaY = int(points.landmark[pose.PoseLandmark.RIGHT_WRIST].y * h)#16
        mao_direitaX = int(points.landmark[pose.PoseLandmark.RIGHT_WRIST].x * w)#16

        olho = int(points.landmark[pose.PoseLandmark.LEFT_EYE_INNER].y * h)#0

        bacia_esquerdaY = int(points.landmark[pose.PoseLandmark.LEFT_HIP].y * h)#0
        bacia_esquerdaX = int(points.landmark[pose.PoseLandmark.LEFT_HIP].x * w)#0

        bacia_direitaY = int(points.landmark[pose.PoseLandmark.RIGHT_HIP].y * h)#0
        bacia_direitaX = int(points.landmark[pose.PoseLandmark.RIGHT_HIP].x * w)#0

        ombro_esquerdoX = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].x * w)
        ombro_direitoX = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].x * w)
        ombro_esquerdoY = int(points.landmark[pose.PoseLandmark.LEFT_SHOULDER].y * h)
        ombro_direitoY = int(points.landmark[pose.PoseLandmark.RIGHT_SHOULDER].y * h)

        tronco = abs(bacia_direitaY - ombro_direitoY)
        dist_ombro = ombro_esquerdoX - ombro_direitoX

        #anda para direita
        if mao_direitaX < ombro_direitoX and mao_esquerdaX < ombro_esquerdoX:
            pyautogui.keyDown('right')
        else:
            pyautogui.keyUp('right')

        #anda para a esquerda
        if mao_esquerdaX > ombro_esquerdoX and mao_direitaX > ombro_direitoX:
            pyautogui.keyDown('left')
        else:
            pyautogui.keyUp('left')

        #soca para direita
        if ombro_direitoX - mao_direitaX > dist_ombro and mao_direitaY < (tronco/2)+ombro_direitoY or mao_esquerdaX - ombro_esquerdoX > dist_ombro and mao_esquerdaY < (tronco/2)+ombro_esquerdoY:
            pyautogui.keyDown('a')
            sleep(0.3)
        else:
            pyautogui.keyUp('a')

        #chuta para direita
        if ombro_direitoX - mao_direitaX > dist_ombro and mao_direitaY > (tronco/2)+ombro_direitoY or mao_esquerdaX - ombro_esquerdoX > dist_ombro and mao_esquerdaY > (tronco/2)+ombro_esquerdoY:
            pyautogui.keyDown('s')
            sleep(0.3)
        else:
            pyautogui.keyUp('s')

        #abaixa
        if mao_direitaY > (tronco/2)+ombro_direitoY and mao_esquerdaY > (tronco/2)+ombro_esquerdoY and mao_esquerdaX - ombro_esquerdoX < dist_ombro and ombro_direitoX - mao_direitaX < dist_ombro:
            pyautogui.keyDown('down')
            sleep(0.3)
        else:
            pyautogui.keyUp('down')

        #chute especial
        if mao_direitaY < olho and mao_esquerdaY < olho:
            pyautogui.keyDown('w')
            sleep(0.3)
        else:
            pyautogui.keyUp('w')

        # agarrar
        if ombro_direitoX - mao_direitaX > dist_ombro and ombro_direitoX - mao_esquerdaX > dist_ombro or mao_esquerdaX - ombro_esquerdoX > dist_ombro and mao_direitaX - ombro_esquerdoX > dist_ombro:
            pyautogui.keyDown('d')
            sleep(0.3)
        else:
            pyautogui.keyUp('d')
#Hernani.IATDH