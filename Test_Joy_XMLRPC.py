import RTCjoystick
import time

J = RTCjoystick.Joystick()
J.connect("/dev/input/js0")
J.info()
J.start()

def button():
    print(J.getAxis())

def motor(self, direct):
    print(direct)

J.connectButton('start', button)
name = 'hat0x'
hatX = 0

while True:
    
    
    time.sleep(0.1)

J.exit()
    

