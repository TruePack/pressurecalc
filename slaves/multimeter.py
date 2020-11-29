import minimalmodbus


class Client:
    def __init__(self):
        instrument = minimalmodbus.Instrument('COM3', 37)
        instrument.serial.timeout = 3
        instrument.serial.baudrate = 9600

        self.instrument = instrument
