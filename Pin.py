from enum import Enum, auto


class PinMode(Enum):
    INPUT = auto()
    OUTPUT = auto()


class Pin:
    def __init__(self, pin_number: int, pin_mode: PinMode) -> None:
        self.pin_number = pin_number
        self.pin_mode = pin_mode

