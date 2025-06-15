from deepface import DeepFace
import cv2
import os
import uuid

def recognize_faces(frame, db_path):
    temp_path = f"temp_{uuid.uuid4().hex}.jpg"
    cv2.imwrite(temp_path, frame)
    try:
        results = DeepFace.find(img_path=temp_path, db_path=db_path, enforce_detection=False)
        os.remove(temp_path)
        is_known = results[0].shape[0] > 0
        label = "Known" if is_known else "Unknown"
        color (0, 255, 0) if is_known else (0, 0, 255)
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        return frame, not is_known
    except Exception as e:
        print("Recognition error:", e)
        os.remove(temp_path)
        return frame, False