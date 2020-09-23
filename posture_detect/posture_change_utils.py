import cv2


def face_detect(frame, face_cascade, s_f=1.2, m_n=5, m_s=30):
    """
    Method to detect a face from a webcam using OpenCV

    Inputs
        frame: snapshot from video feed
        face_cascade: face classifier from pre-trained model
    Outputs
        x: horizontal position of the detected face in the frame
        y: vertical position of the detected face in the frame
        w: width of the detected face in the frame
        h: height of the detected face in the frame
    """

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=s_f,
        minNeighbors=m_n,
        minSize=(m_s, m_s),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces


def draw_rectangle(faces, frame, posture=False):
    """
    Method to draw rectangle around face with indication to fix posture

    Inputs
        faces: face object which holds information on location and size of detected faces
        frame: snapshot from video feed where face was found
        posture: Indication that posture is wavering when True
    """

    for (x, y, w, h) in faces:
        if posture:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


def proximity_change(baseline_face, w, h, threshold):
    """
    Method to calculate the change in the proximity to the camera compared with a threshold

    Inputs
        baseline_face: Initial face object capture of what is deemed "correct" posture
        w, h: width and height of the detected face object
        threshold: degree of change necessary for the change to be flagged
    Outputs
        boolean indicated whether the change is flagged
    """
    
    w_dif_percent = abs((w-baseline_face[0][2])/baseline_face[0][2])
    h_dif_percent = abs((h-baseline_face[0][3])/baseline_face[0][3])
    return (w_dif_percent or h_dif_percent) > threshold


def lateral_change(baseline_face, x, y, threshold):
    """
    Method to calculate the change in the lateral movement compared with a threshold

    Inputs
        baseline_face: Initial face object capture of what is deemed "correct" posture
        x, y: horizontal and vertical positions of the face center within the frame
        threshold: degree of change necessary for the change to be flagged
    Outputs
        boolean indicated whether the change is flagged
    """

    x_dif_percent = abs((x-baseline_face[0][0])/baseline_face[0][0])
    y_dif_percent = abs((y-baseline_face[0][1])/baseline_face[0][1])
    return (x_dif_percent or y_dif_percent) > threshold


def posture_change(baseline_face, faces, threshold=0.5):
    """
    Method to calculate the change in the size of the detected face

    Inputs
        baseline_face: Initial face object capture of what is deemed "correct" posture
        faces: face object which holds information on location and size of detected faces
        threshold: degree of change necessary for the posture to be flagged
    Outputs
        boolean indicated whether the posture is flagged
    """

    if len(faces) > 0 and len(baseline_face) > 0:
        for x, y, w, h in faces:
            prox = proximity_change(baseline_face, w, h, threshold)
            sides = lateral_change(baseline_face, x, y, threshold)
            if prox or sides:
                return True
            else:
                return False
    else:
        return False
