from car_speed_control import *

def pivot_left(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(-speed // 2)
    set_right_motor(speed)
    display.show(Image.ARROW_W)

def pivot_right(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(speed)
    set_right_motor(-speed // 2)
    display.show(Image.ARROW_E)

def curve_left(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(speed // 2)
    set_right_motor(speed)

def curve_right(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(speed)
    set_right_motor(speed // 2)

if __name__ == "__main__":
    move_forward()
    sleep(1000)
    pivot_left()
    sleep(1500)
    move_forward()
    sleep(1000)
    pivot_right()
    sleep(1500)
    full_stop()
