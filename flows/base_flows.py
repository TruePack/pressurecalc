from time import sleep

import tkinter as tk
from matplotlib import pyplot

from graphics.base import create_figure, create_tk_widget
from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave


def get_pressure_and_show_graphic(window: tk.Tk, pressure: PressureSlave,
                                  frequency: FrequencySlave, gcf=pyplot.gcf()):
    f_values = []
    p_values = []
    figure = create_figure()
    create_tk_widget(figure, window)
    frequency.set_frequency(10)
    # Measure count
    for x in range(10):
        x += 1000
        frequency.set_frequency(x)
        frequency_value = frequency.get_frequency()
        f_values.append(frequency_value)
        pressure_value = pressure.get_pressure()
        p_values.append(pressure_value)
        pyplot.grid(True)
        pyplot.plot(f_values, p_values, 'r')
        figure.canvas.draw()


