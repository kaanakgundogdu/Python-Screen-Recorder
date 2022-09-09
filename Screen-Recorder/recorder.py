import pyautogui
import cv2
import numpy as np
import datetime as dt
from win32api import GetSystemMetrics

class Recorder():
    def __init__(self) -> None:
        self.w=GetSystemMetrics(0)
        self.h=GetSystemMetrics(1)
        self.current_file_name=dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.fps = 7.0
        resolution = (self.w, self.h)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        filename = "output/"+self.current_file_name+".avi"
        self.out = cv2.VideoWriter(filename, codec, self.fps, resolution)
        cv2.namedWindow("Kaan's Screen Recorder", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Kaan's Screen Recorder", 825, 480)
    
    def record(self):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.out.write(frame)
        cv2.imshow("Kaan's Screen Recorder", frame)
    
    def stop_recorder(self):
        self.out.release()
        cv2.destroyAllWindows()

    def is_closed(self):
        if cv2.waitKey(1) & 0xFF == 27: 
            return True
        if cv2.getWindowProperty("Kaan's Screen Recorder",cv2.WND_PROP_VISIBLE) < 1:        
            return True
        return False    

