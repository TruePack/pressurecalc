from matplotlib import pyplot
from matplotlib.figure import Figure

from graphics import base as base_graph
from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave


def get_pressure_and_show_graphic(figure: Figure, pressure: PressureSlave,
                                  frequency: FrequencySlave):
    f_values = []
    p_values = []

    base_graph.clear_old_values_lines_and_add_grid(figure.number)
    frequency.set_frequency(10)

    # Measure count
    for x in range(10):
        x += 1000
        frequency.set_frequency(x)
        frequency_value = frequency.get_frequency()
        f_values.append(frequency_value)
        pressure_value = pressure.get_pressure()
        p_values.append(pressure_value)
    pyplot.plot(f_values, p_values, 'r')
    figure.canvas.draw()
