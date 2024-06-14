import gamepad
import time

if __name__ == "__main__":
    gamepad = gamepad.Gamepad('/dev/input/event0')
    while True:
        print('X={}, Y={}, A={}'.format(gamepad.getX(), gamepad.getY(), gamepad.isAButtonPressed()))
        time.sleep(1.0)