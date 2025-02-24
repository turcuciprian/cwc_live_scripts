import cv2
import sys
import os
from pathlib import Path

# support for importing custom library -- START
current_folder = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_folder, '../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# support for importing custom library -- END


from custom_library.opencv_models_methods import detect_objects

# sys.path.insert(0, original_parent_dir)

cam = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = cam.read()
        frame = cv2.resize(frame, (640, 480))
        model_path = os.path.join(current_folder, "models/haarcascade_eye.xml")
        face_clasifier = cv2.CascadeClassifier(model_path)
        eyes = face_clasifier.detectMultiScale(
            frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )
        detect_objects(image=frame, objects=eyes, lines=False, rectangles=True)
    except:
        cv2.imshow("Webcam", frame)
        cv2.waitKey(0)

    if cv2.waitKey(1) == ord("s"):
        breakpoint()
    if cv2.waitKey(1) == ord("q"):
        print(frame.shape)
        break
cam.release()
