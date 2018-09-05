import os
def openFile():
    try:
        os.startfile('openME.txt')
    except Exception as e:
        print(str(e))
def closFile():
    try:
        os.system('TASKILL /F /IM notepad.exe')
    except Exception as e:
        print(str(e))