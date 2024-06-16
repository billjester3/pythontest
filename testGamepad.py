import cc4hpibot
import time

LEFTPIN = 12
RIGHTPIN = 18
INTAKEPIN = 17

INTAKESPEED = -0.5
DRIVESPEEDMULTIPLIER = 0.5

if __name__ == "__main__":
    gamepad = cc4hpibot.Gamepad('/dev/input/event0')
    intake = cc4hpibot.Motor(INTAKEPIN)
    drivetrain = cc4hpibot.DriveTrain(LEFTPIN, RIGHTPIN)

    while True:
        drivetrain.arcadeDrive(-DRIVESPEEDMULTIPLIER*gamepad.getX(), -DRIVESPEEDMULTIPLIER*gamepad.getY())
        if (gamepad.isAButtonPressed()):
            intake.setSpeed(INTAKESPEED)
        else:
            intake.stop()
        
        time.sleep(0.02)