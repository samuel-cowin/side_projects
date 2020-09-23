"""
File to detect posture change utilizing proximity of face to camera
"""

import sys
import cv2
from posture_change_utils import face_detect, draw_rectangle, posture_change

casc_path = sys.argv[1]
face_cascade = cv2.CascadeClassifier(casc_path)
video_capture = cv2.VideoCapture(0)
input('Ready for face capture? (Enter to continue)')
_, frame = video_capture.read()
baseline_face = face_detect(frame, face_cascade, s_f=1.2, m_n=5, m_s=30)

posture = False
while True:
    # Capture frame-by-frame
    _, frame = video_capture.read()
    # Detect face and return the location and size
    faces = face_detect(frame, face_cascade, s_f=1.2, m_n=5, m_s=30)
    # Draw rectangle
    draw_rectangle(faces, frame, posture=posture)
    # Check if posture is wavering
    posture = posture_change(baseline_face, faces, threshold=0.1)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()