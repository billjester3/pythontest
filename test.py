import evdev
import time

class Gamepad:
    XAXIS_ID = 0
    YAXIS_ID = 1

    def __init__(self, deviceName):
        self.device = evdev.InputDevice(deviceName)
        self.currentX = 0
        self.currentY = 0

    def getX(self):
        return self.getJoystickValue(self.XAXIS_ID)
    
    def getY(self):
        return -1*self.getJoystickValue(self.YAXIS_ID)
    
    def getJoystickValue(self, axis):
        absinfo = self.device.absinfo(axis)
        return 2.0*(absinfo.value-  absinfo.min)/(absinfo.max - absinfo.min) - 1.0

if __name__ == "__main__":
    gamepad = Gamepad('/dev/input/event0')
    while True:
        print('X={}, Y={}'.format(gamepad.getX(), gamepad.getY()))
        time.sleep(1.0)


