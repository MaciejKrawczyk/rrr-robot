from Pin import Pin


class Encoder:
    def __init__(
            self,
            output_plus_pin: Pin,
            output_minus_pin: Pin,
    ):
        self.output_plus_pin = output_plus_pin
        self.output_minus_pin = output_minus_pin
