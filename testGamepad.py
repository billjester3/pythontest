import cc4hpibot
import time

if __name__ == "__main__":
    cc4hpibot = cc4hpibot.Gamepad('/dev/input/event0')
    while True:
        print('X={}, Y={}, A={}'.format(cc4hpibot.getX(), cc4hpibot.getY(), cc4hpibot.isAButtonPressed()))
        time.sleep(1.0)