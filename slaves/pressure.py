import minimalmodbus
from utils import hex_to_dec
from typing import List


class Client:
    PRESSURE_UNIT_MAP = {
        0: "Па",
        1: "кПа",
        2: "% ВПИ",
        3: "мм.вод.ст.",
        4: "м.вод.ст.",
        5: "мБар",
        6: "Бар",
        7: "psi",
    }

    def __init__(self):
        instrument = minimalmodbus.Instrument("COM3", 60,
                                              close_port_after_each_call=True)
        instrument.serial.timeout = 3
        instrument.serial.baudrate = 9600

        self.instrument = instrument

    def get_pressure(self) -> float:
        pressure: float = self.instrument.read_float(hex_to_dec("0x0013"))
        return pressure

    def get_pressure_unit(self) -> str:
        pressure_unit = self.instrument.read_register(hex_to_dec("0x0015"))
        huminized_pressure_unit = self.PRESSURE_UNIT_MAP[pressure_unit]
        return huminized_pressure_unit

    def get_temperature(self) -> float:
        temperature: float = self.instrument.read_float(hex_to_dec("0x0011"))
        return temperature
