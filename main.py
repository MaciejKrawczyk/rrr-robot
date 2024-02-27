from Encoder import Encoder
from Motor import Motor
from RRRRobot import RRRRobot

ENCODER1_OUTPUT_PIN_ID_PLUS = 0
ENCODER1_OUTPUT_PIN_ID_MINUS = 0

ENCODER2_OUTPUT_PIN_ID_PLUS = 0
ENCODER2_OUTPUT_PIN_ID_MINUS = 0

ENCODER3_OUTPUT_PIN_ID_PLUS = 0
ENCODER3_OUTPUT_PIN_ID_MINUS = 0

MOTOR1_INPUT_PIN_ID_PLUS = 0
MOTOR1_INPUT_PIN_ID_MINUS = 0

MOTOR2_INPUT_PIN_ID_MINUS = 0
MOTOR2_INPUT_PIN_ID_PLUS = 0

MOTOR3_INPUT_PIN_ID_PLUS = 0
MOTOR3_INPUT_PIN_ID_MINUS = 0

ARM1_LENGTH = 1
ARM2_LENGTH = 1
ARM3_LENGTH = 1

if __name__ == '__main__':

    encoder1 = Encoder(ENCODER1_OUTPUT_PIN_ID_PLUS, ENCODER1_OUTPUT_PIN_ID_MINUS)
    encoder2 = Encoder(ENCODER2_OUTPUT_PIN_ID_PLUS, ENCODER2_OUTPUT_PIN_ID_MINUS)
    encoder3 = Encoder(ENCODER3_OUTPUT_PIN_ID_PLUS, ENCODER3_OUTPUT_PIN_ID_MINUS)

    motor1 = Motor(MOTOR1_INPUT_PIN_ID_PLUS, MOTOR1_INPUT_PIN_ID_MINUS, encoder1)
    motor2 = Motor(MOTOR2_INPUT_PIN_ID_PLUS, MOTOR2_INPUT_PIN_ID_MINUS, encoder2)
    motor3 = Motor(MOTOR3_INPUT_PIN_ID_PLUS, MOTOR3_INPUT_PIN_ID_MINUS, encoder3)

    robot = RRRRobot(motor1, motor2, motor3, ARM1_LENGTH, ARM2_LENGTH, ARM3_LENGTH)

    robot.initialize()