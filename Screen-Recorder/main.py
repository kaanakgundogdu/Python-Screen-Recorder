import recorder
### DEPENDENCIES
# Pillow 
# pyautogui
# cv2
# win32api
# numpy
###

rec=recorder.Recorder()
while True:
    rec.record()
    
    if  rec.is_closed():
        break
rec.stop_recorder()