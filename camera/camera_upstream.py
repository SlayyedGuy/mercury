import cv2
from recognition.face_recognizer import recognize_faces
from alerts.alert_manager import send_alert

import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

CAMERA_URL = config['camera_url']
KNOWN_FACES_PATH = config['known_faces_path']

def start_camera():
    cap = cv2.VideoCapture(CAMERA_URL)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result_frame, unknown_detected = recognize_faces(frame, KNOWN_FACES_PATH)
        if unknown_detected:
            send_alert("Unknown person detected.")
        cv2.imshow("CCTV Feed", result_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
