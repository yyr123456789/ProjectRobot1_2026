from microbit import *
import tinybit

BASE_SPEED = 160

def execute_step(direction, speed, duration):
    """
    Execute a single movement step and print the output.
    """
    print("Action: {}, Speed: {}, Time: {}ms".format(direction, speed, duration))

    if direction == "forward":
        tinybit.car_run(speed)
        display.show(Image.ARROW_N)
    elif direction == "backward":
        tinybit.car_back(speed)
        display.show(Image.ARROW_S)
    elif direction == "left":
        tinybit.car_left(speed)
        display.show(Image.ARROW_W)
    elif direction == "right":
        tinybit.car_right(speed)
        display.show(Image.ARROW_E)
    elif direction == "stop":
        tinybit.car_stop()
        display.clear()

    sleep(duration)

