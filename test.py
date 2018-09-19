import cv2
import numpy as np
import time
import datetime


print("If you see this, the following modules were imported successfully: \ncv2, numpy, picamera, picamera[array]\n")

# Set up date for video filenames (both output and input filenames)
d = datetime.date.today()
newvid = d.strftime("%Y-%m-%d")

# How this works:
# @reboot, I run a script using crontab that records video, I transfer it to my laptop, convert to mp4 then feed back to analysis script for computation (it can't take .h264 files)

# Initialize video capture, classifier, counter, frame position, and output video file

#vid = cv2.VideoCapture(newvid + ".mp4")
vid = cv2.VideoCapture("2018-09-19-4_22.MOV") # testing purposes only
car_classifier = cv2.CascadeClassifier("cars.xml")
count = 0
pos_frame = vid.get(cv2.CAP_PROP_POS_FRAMES)

# OUTPUT VIDEO IS NOT PLAYABLE, I FUCKING HATE THIS PIECE OF SHIT.
#output = cv2.VideoWriter(newvid + "output.avi", cv2.VideoWriter_fourcc(*"XVID"), 20.0, (640,480))

while True:
    flag, frame = vid.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(grayscale, 1.1, 3)
    # Since every car is returned in a list of rectangles, we can iterate over them to count and do other stuff.
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        count += 1

    #output.write(frame)

    print(count) #for command line debugging only
    count = 0

    # if the  frame we just read is the last frame in the file, break loop and exit.
    # amount of frames read limited for debugging purposes (its slow as hell)
    if vid.get(cv2.CAP_PROP_POS_FRAMES) == 40: #vid.get(cv2.CAP_PROP_FRAME_COUNT):
        #output.release()
        vid.release()
        break
