import minimalmodbus
from time import sleep
import random


FREQUENCY = random.random()


class Client:
    def __init__(self):
        instrument = minimalmodbus.Instrument('COM3', 49,
                                              close_port_after_each_call=True)
        instrument.serial.timeout = 3
        instrument.serial.baudrate = 9600

        self.instrument = instrument

    def get_frequency(self) -> int:
        # frequency = self.instrument.read_register(2)
        frequency = FREQUENCY
        return frequency

    def run_forward(self):
        try:
            # self.instrument.write_register(8192, 11)
            pass
        except minimalmodbus.InvalidResponseError:
            pass

    def set_frequency(self, value) -> None:
        self.stop()
        # Set value
        try:
            pass
            # self.instrument.write_register(8193, value)
        except Exception:
            pass
        # Run command
        try:
            pass
            # self.instrument.write_register(8192, 2)
        except Exception:
            pass
        try:
            pass
            # self.instrument.write_register(107, 1000)
        except Exception:
            pass
        FREQUENCY = value
        return

    def set_speed_up(self, value_for_up: int) -> None:
        frequency = self.get_frequency()
        frequency_after_up = frequency + value_for_up
        return FREQUENCY
        # self.instrument.write_register(100, frequency_after_up)

    def stop(self):
        pass
        # self.instrument.write_register(8192, 1)
