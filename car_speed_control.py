from car_config import *

def set_left_motor_speed(speed_value: int):
    clamped_speed = max(MIN_MOTOR_SPEED, min(abs(speed_value), MAX_MOTOR_SPEED))
    if speed_value > 0:
        MOTOR_LEFT_FORWARD_PIN.write_analog(clamped_speed)
        MOTOR_LEFT_BACKWARD_PIN.write_analog(0)
    else:
        MOTOR_LEFT_FORWARD_PIN.write_analog(0)
        MOTOR_LEFT_BACKWARD_PIN.write_analog(clamped_speed)

def set_right_motor_speed(speed_value: int):
    clamped_speed = max(MIN_MOTOR_SPEED, min(abs(speed_value), MAX_MOTOR_SPEED))
    if speed_value > 0:
        MOTOR_RIGHT_FORWARD_PIN.write_analog(clamped_speed)
        MOTOR_RIGHT_BACKWARD_PIN.write_analog(0)
    else:
        MOTOR_RIGHT_FORWARD_PIN.write_analog(0)
        MOTOR_RIGHT_BACKWARD_PIN.write_analog(clamped_speed)

def full_stop_car():
    set_left_motor_speed(0)
    set_right_motor_speed(0)
    display.show(Image.SAD)

def move_forward(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(speed)
    set_right_motor_speed(speed)
    display.show(Image.ARROW_N)

def move_backward(speed: int = DEFAULT_MOTOR_SPEED):
    set_left_motor_speed(-speed)
    set_right_motor_speed(-speed)
    display.show(Image.ARROW_S)

if __name__ == "__main__":
    move_forward(800)
    sleep(2000)
    full_stop_car()
