import cv2
import pytesseract
import dlib
import numpy as np
import re

# Initialize face detector
detector = dlib.get_frontal_face_detector()

# Function to mask Aadhaar number
def mask_aadhaar(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    aadhaar_match = re.search(r'\b\d{12}\b', text)
    
    if aadhaar_match:
        aadhaar_num = aadhaar_match.group()
        masked = 'XXXX-XXXX-' + aadhaar_num[-4:]
        cv2.putText(image, masked, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return image, masked
    
    return image, None

# Function to detect liveness
def detect_liveness(prev_faces, curr_faces):
    if not prev_faces or not curr_faces:
        return False
    movement = abs(prev_faces[0].left() - curr_faces[0].left()) + abs(prev_faces[0].top() - curr_faces[0].top())
    return movement > 10

# Start video capture
cap = cv2.VideoCapture(0)
prev_faces = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Mask Aadhaar number
    masked_frame, masked_num = mask_aadhaar(frame.copy())
    if masked_num:
        print("Masked Aadhaar Number:", masked_num)
    
    # Detect face and check liveness
    curr_faces = detector(frame, 1)
    is_live = detect_liveness(prev_faces, curr_faces)
    status = "Live" if is_live else "Photo Detected"
    
    # Display status on frame
    cv2.putText(masked_frame, status, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Show output
    cv2.imshow('SecureKYC', masked_frame)
    prev_faces = curr_faces
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
