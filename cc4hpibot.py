import evdev
import gpiozero

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



class Motor:
    def __init__(self, pin):
        self.servo = gpiozero.Servo(pin, pin_factory=gpiozero.pins.pigpio.PiGPIOFactory())

    def setSpeed(self, val):
        self.servo.value = val

    def stop(self):
        self.servo.mid()


class DriveTrain:
    # use BCM pin numbers, not physical pin numbers, i.e. if plugged into GPIO4 input 4 for the pin!
    def __init__(self, leftMotorPin, rightMotorPin):
        self.leftMotor = Motor(leftMotorPin)
        self.rightMotor = Motor(rightMotorPin)

    def arcadeDrive(self, drive, rotate):
        # constrain to (-1,1)
        drive = max(-1.0, min(drive, 1.0))
        rotate = max(-1.0, min(rotate, 1.0))

        # code from https://xiaoxiae.github.io/Robotics-Simplified-Website/drivetrain-control/arcade-drive/
        maximum = max(abs(drive), abs(rotate))
        total = drive + rotate
        difference = drive - rotate

        leftSpeed = 0
        rightSpeed = 0

        # set speed according to the quadrant that the values are in
        if drive >= 0:
            if rotate >= 0:  # I quadrant
                leftSpeed = maximum
                rightSpeed = difference
            else:            # II quadrant
                leftSpeed = total
                rightSpeed = maximum
        else:
            if rotate >= 0:  # IV quadrant
                leftSpeed = total
                rightSpeed = -maximum
            else:            # III quadrant
                leftSpeed = -maximum
                rightSpeed = difference

        self.leftMotor.setSpeed(leftSpeed)
        self.rightMotor.setSpeed(rightSpeed)




