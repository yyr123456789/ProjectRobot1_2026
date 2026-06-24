from microbit import *

# Left motor pins
MOTOR_LEFT_FORWARD = pin0
MOTOR_LEFT_BACKWARD = pin1

# Right motor pins
MOTOR_RIGHT_FORWARD = pin2
MOTOR_RIGHT_BACKWARD = pin8

# Speed limits
MIN_MOTOR_SPEED = 200
MAX_MOTOR_SPEED = 1023
DEFAULT_MOTOR_SPEED = 600

# Global storage for encrypted data
stored_encrypted_face_data = None
