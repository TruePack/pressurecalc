from time import sleep
from typing import NoReturn

from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave


def start_engine_and_getting_pressure(frequency: FrequencySlave,
                                      pressure: PressureSlave) -> NoReturn:
    pressure_unit = pressure.get_pressure_unit()
    frequency.set_frequency(5000)
    while True:
        print(pressure.get_pressure())
        sleep(1)