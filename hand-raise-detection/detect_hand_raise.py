import cv2

# Load the cascade
haar_cascade_hand = cv2.CascadeClassifier('data\\haarcascades\\aGest.xml')
haar_cascade_palm = cv2.CascadeClassifier('data\\haarcascades\\palm.xml')
haar_cascade_fist = cv2.CascadeClassifier('data\\haarcascades\\fist.xml')
haar_cascade_closed_frontal_palm=cv2.CascadeClassifier('data\\haarcascades\\closed_frontal_palm.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,620)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = haar_cascade_hand.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in hand:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    palm = haar_cascade_palm.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in palm:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    fist = haar_cascade_fist.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in fist:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    closed_palm=haar_cascade_closed_frontal_palm.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in closed_palm:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    # Stop if q key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()