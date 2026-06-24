from car_speed_control import *

def pivot_turn_left(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(-speed // 2)
    set_right_motor_speed(speed)
    display.show(Image.ARROW_W)

def pivot_turn_right(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(speed)
    set_right_motor_speed(-speed // 2)
    display.show(Image.ARROW_E)

def gentle_curve_left(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(speed // 2)
    set_right_motor_speed(speed)

def gentle_curve_right(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(speed)
    set_right_motor_speed(speed // 2)

if __name__ == "__main__":
    move_forward()
    sleep(1000)
    pivot_turn_left()
    sleep(1500)
    move_forward()
    sleep(1000)
    pivot_turn_right()
    sleep(1500)
    full_stop_car()