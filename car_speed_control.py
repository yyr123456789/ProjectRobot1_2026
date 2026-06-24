from car_config import *

def clamp_speed(speed_value: int) -> int:
    abs_spd = abs(speed_value)
    return max(MIN_MOTOR_SPEED, min(abs_spd, MAX_MOTOR_SPEED))

def set_left_motor(speed_value: int):
    spd = clamp_speed(speed_value)
    if speed_value > 0:
        MOTOR_LEFT_FORWARD.write_analog(spd)
        MOTOR_LEFT_BACKWARD.write_analog(0)
    else:
        MOTOR_LEFT_FORWARD.write_analog(0)
        MOTOR_LEFT_BACKWARD.write_analog(spd)

def set_right_motor(speed_value: int):
    spd = clamp_speed(speed_value)
    if speed_value > 0:
        MOTOR_RIGHT_FORWARD.write_analog(spd)
        MOTOR_RIGHT_BACKWARD.write_analog(0)
    else:
        MOTOR_RIGHT_FORWARD.write_analog(0)
        MOTOR_RIGHT_BACKWARD.write_analog(spd)

def full_stop():
    set_left_motor(0)
    set_right_motor(0)
    display.show(Image.SAD)

def move_forward(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(speed)
    set_right_motor(speed)
    display.show(Image.ARROW_N)

def move_backward(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor(-speed)
    set_right_motor(-speed)
    display.show(Image.ARROW_S)

if __name__ == "__main__":
    move_forward(800)
    sleep(2000)
    full_stop()
