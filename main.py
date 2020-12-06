import matplotlib
import tkinter as tk
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from flows.base_flows import get_pressure_and_show_graphic
from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave


def main():
    frequency = FrequencySlave()
    pressure = PressureSlave()
    #
    # start_engine_and_getting_pressure(frequency, pressure)
    #
    window = configure_window()
    create_button(window, pressure, frequency)
    window.mainloop()


def configure_window() -> tk.Tk:
    window = tk.Tk()
    window.title("График давления")
    window.geometry('800x600')
    matplotlib.use('TkAgg')
    return window


def create_button(window: tk.Tk, pressure: PressureSlave,
                  frequency: FrequencySlave):
    button = tk.Button(
        window, text="Нажми!",
        command=lambda: get_pressure_and_show_graphic(window, pressure,
                                                      frequency))
    button.place(x=5, y=5, width=200, height=40)
    button.bind("<Button-1>")


if __name__ == '__main__':
    main()
