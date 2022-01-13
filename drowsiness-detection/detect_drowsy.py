import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
import imutils
from imutils import face_utils

detector = dlib.get_frontal_face_detector() #For detecting faces
landmark_path="shape_predictor_68_face_landmarks.dat"
#Path of the file - if stored in the same directory. Else, give the relative path
predictor = dlib.shape_predictor(landmark_path) #For identifying landmarks

def eye_aspect_ratio(eye):
    # Vertical eye landmarks
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # Horizontal eye landmarks
    C = dist.euclidean(eye[0], eye[3])

    # The EAR Equation
    EAR = (A + B) / (2.0 * C)
    return EAR

def mouth_aspect_ratio(mouth):
    A = dist.euclidean(mouth[13], mouth[19])
    B = dist.euclidean(mouth[14], mouth[18])
    C = dist.euclidean(mouth[15], mouth[17])

    MAR = (A + B + C) / 3.0
    return MAR


video_capture = cv2.VideoCapture(0)
yawn_status = False
yawn_count = 0
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20
COUNTER = 0
ALARM_ON = False
MAR_THRESHOLD = 14

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mstart, mend) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

while True:
    _, image_frame = video_capture.read()
    image_frame = imutils.resize(image_frame, width=900)
    image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    rects = detector(image_frame, 0)
    for rect in rects:
        shape = predictor(image_frame, rect)
        shape = face_utils.shape_to_np(shape)
        # for (x, y) in shape:
        #    cv2.circle(image_frame, (x, y), 1, (0, 0, 255), -1)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        mouth = shape[mstart:mend]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        # cv2.drawContours(image_frame, [leftEyeHull], -1, (0, 255, 0), 1)
        # cv2.drawContours(image_frame, [rightEyeHull], -1, (0, 255, 0), 1)
        # cv2.drawContours(image_frame, [mouth], -1, (0, 255, 0), 1)
        MAR = mouth_aspect_ratio(mouth)
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True
                cv2.putText(image_frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            COUNTER = 0
            ALARM_ON = False
        cv2.putText(image_frame, "EAR: {:.2f}".format(ear), (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        previous_status = yawn_status
        if MAR > MAR_THRESHOLD:
            yawn_status = True
            output_text = " Number of Yawns: " + str(yawn_count + 1)
            cv2.putText(image_frame, "You are yawning", (50, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))
            cv2.putText(image_frame, output_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

        else:
            yawn_status = False

        if previous_status == True and yawn_status == False:
            yawn_count += 1
    cv2.imshow('image_frame',image_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()