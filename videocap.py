from picamera import PiCamera
import time
import datetime

# Initialize camera object to record.
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 20

newvid = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M") + ".h264"

# Give time for camera to initialize
time.sleep(0.5)

camera.start_recording(newvid)
camera.wait_recording(20)
camera.stop_recording()
print("Done recording.\n")
