from Encoder import Encoder
from Pin import Pin


class Motor:
    def __init__(
            self,
            input_plus_pin: Pin,
            input_minus_pin: Pin,
            encoder: Encoder | None = None
    ) -> None:
        self.input_plus_pin = input_plus_pin
        self.input_minus_pin = input_minus_pin
        self.encoder = encoder
