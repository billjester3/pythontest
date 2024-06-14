import gamepad
import time

if __name__ == "__main__":
    gamepad = gamepad.Gamepad('/dev/input/event0')
    while True:
        print('X={}, Y={}'.format(gamepad.getX(), gamepad.getY()))
        time.sleep(1.0)