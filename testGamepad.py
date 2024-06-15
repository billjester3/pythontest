import cc4hpibot
import time

LEFTPIN = 12
RIGHTPIN = 18

if __name__ == "__main__":
    gamepad = cc4hpibot.Gamepad('/dev/input/event0')
    drivetrain = cc4hpibot.DriveTrain(LEFTPIN, RIGHTPIN)

    while True:
        drivetrain.arcadeDrive(gamepad.getX(), gamepad.getY())
        time.sleep(0.02)