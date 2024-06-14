import evdev

class Gamepad:
    XAXIS_ID = 0
    YAXIS_ID = 1
    XBUTTON_ID = 304
    YBUTTON_ID = 307
    ABUTTON_ID = 305
    BBUTTON_ID = 306
    LBUMPER_ID = 308
    RBUMPER_ID = 309

    def __init__(self, deviceName):
        self.device = evdev.InputDevice(deviceName)
        self.currentX = 0
        self.currentY = 0

    def getX(self):
        return self.getJoystickValue(self.XAXIS_ID)
    
    def getY(self):
        return -1*self.getJoystickValue(self.YAXIS_ID)
    
    def isAButtonPressed(self):
        return self.isButtonPressed(self.ABUTTON_ID)

    def isBButtonPressed(self):
        return self.isButtonPressed(self.BBUTTON_ID)

    def isXButtonPressed(self):
        return self.isButtonPressed(self.XBUTTON_ID)
    
    def isYButtonPressed(self):
        return self.isButtonPressed(self.YBUTTON_ID)

    def getJoystickValue(self, axis):
        absinfo = self.device.absinfo(axis)
        return 2.0*(absinfo.value-  absinfo.min)/(absinfo.max - absinfo.min) - 1.0

    def isButtonPressed(self, button):
        keys = self.device.active_keys()
        return button in keys




