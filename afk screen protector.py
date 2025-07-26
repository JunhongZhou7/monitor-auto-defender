import cv2
import time
from ultralytics import YOLO
import yagmail
import os
import face_recognition
import sys

# --- CONFIG ---
CHECK_INTERVAL = 5  # in seconds  
OUTPUT_IMAGE = "stranger_detected.jpg"
EMAIL_RECEIVER = ""  
EMAIL_SENDER = ""
OWNER_IMAGE = face_recognition.load_image_file()
OWNER_ENCODING = face_recognition.face_encodings(OWNER_IMAGE)[0]
# ---------------

# Load model
model = YOLO("yolov8s.pt")

# Setup webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


print("Monitoring for strangers every 5 seconds...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            continue

        results = model(frame)
        person_detected = False

        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            if class_name == "person":
                person_detected = True
                break

        if person_detected:
            owner_present = False
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            
            owner_present = any(
                face_recognition.compare_faces([OWNER_ENCODING], encoding, tolerance=0.8)[0]
                for encoding in face_encodings)


                
            if not owner_present:
                print(f"[{time.ctime()}]  !! stranger detected !!")

            # Save the frame
                cv2.imwrite(OUTPUT_IMAGE, frame)

                yag = yagmail.SMTP("your_email_here","email_code_here")
            # Send email
                yag.send(
                    to=EMAIL_RECEIVER,
                    subject="stranger detected!",
                    contents="An unknown person just passed your desktop and might be messing up your computer! check out who he/she is!",
                    attachments="stranger_detected.jpg"
                )

                print("Email sent with image.")

                os.system("powershell -Command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Application]::SetSuspendState('Suspend',$false, $false)\"")
                sys.exit()


        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("Stopped by user.")

# Cleanup
cap.release()
cv2.destroyAllWindows()

