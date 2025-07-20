#AFK Screen Protector

This program uses YOLO v8 and your computer webcam to detect if someone is looking at your screen while your absent.
Whenever you leave your computer after runsning this program, if an unrecognized person is captured by your webcam, it:
  -- puts your computer into sleep mode
  -- sends an email with the frame image in which that person is present

#Features

  -- Real-time image capture and identification by YOLO v8 every 5 seconds
  -- face recognition package from Python library recognises your face once an image of yourself is uploaded into the program.

#Requirements:

Must have downloaded the following to ensure the program runs properly:
  -- DLIB (for python face recognition library)
  -- face_recognition from python
  -- YOLO from ultralytics
  -- public key from your email website for message sending
  -- make sure your webcam works

#Possible issues to be encounter:
  -- The face recognition library isn't that powerful. To correctly recognize your face, upload multiple pictures of yourself from different angles, distances, lights, etc.
  -- YOLO v8 is a hightly accurate yet slow model. It takes around 150 ms to correctly name and compare objects.
  
