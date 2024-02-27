from Encoder import Encoder
from Motor import Motor
from Pin import Pin, PinMode
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

    encoder1_output_pin_plus = Pin(ENCODER1_OUTPUT_PIN_ID_PLUS, pin_mode=PinMode.OUTPUT)
    encoder1_output_pin_minus = Pin(ENCODER1_OUTPUT_PIN_ID_MINUS, pin_mode=PinMode.OUTPUT)

    encoder2_output_pin_plus = Pin(ENCODER2_OUTPUT_PIN_ID_PLUS, pin_mode=PinMode.OUTPUT)
    encoder2_output_pin_minus = Pin(ENCODER2_OUTPUT_PIN_ID_MINUS, pin_mode=PinMode.OUTPUT)

    encoder3_output_pin_plus = Pin(ENCODER3_OUTPUT_PIN_ID_PLUS, pin_mode=PinMode.OUTPUT)
    encoder3_output_pin_minus = Pin(ENCODER3_OUTPUT_PIN_ID_MINUS, pin_mode=PinMode.OUTPUT)

    motor1_input_pin_plus = Pin(MOTOR1_INPUT_PIN_ID_PLUS, pin_mode=PinMode.INPUT)
    motor1_input_pin_minus = Pin(MOTOR1_INPUT_PIN_ID_MINUS, pin_mode=PinMode.INPUT)

    motor2_input_pin_plus = Pin(MOTOR2_INPUT_PIN_ID_PLUS, pin_mode=PinMode.INPUT)
    motor2_input_pin_minus = Pin(MOTOR2_INPUT_PIN_ID_MINUS, pin_mode=PinMode.INPUT)

    motor3_input_pin_plus = Pin(MOTOR3_INPUT_PIN_ID_PLUS, pin_mode=PinMode.INPUT)
    motor3_input_pin_minus = Pin(MOTOR3_INPUT_PIN_ID_MINUS, pin_mode=PinMode.INPUT)

    encoder1 = Encoder(encoder1_output_pin_plus, encoder1_output_pin_minus)
    encoder2 = Encoder(encoder2_output_pin_plus, encoder2_output_pin_minus)
    encoder3 = Encoder(encoder3_output_pin_plus, encoder3_output_pin_minus)

    motor1 = Motor(motor1_input_pin_plus, motor1_input_pin_minus, encoder1)
    motor2 = Motor(motor2_input_pin_plus, motor2_input_pin_minus, encoder2)
    motor3 = Motor(motor3_input_pin_plus, motor3_input_pin_minus, encoder3)

    robot = RRRRobot(motor1, motor2, motor3, ARM1_LENGTH, ARM2_LENGTH, ARM3_LENGTH)

    robot.initialize()
