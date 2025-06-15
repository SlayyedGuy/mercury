import cv2

def draw_label(frame, text, pos, color):
    cv2.putText(frame, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
