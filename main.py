from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave
from measures.frequency import start_engine_and_getting_pressure
from matplotlib import pyplot
from random import random
import tkinter as tk
from flows.base_flows import get_pressure_and_show_graphic
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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


def configure_canvas(window: tk.Tk) -> None:
    figure = pyplot.figure(1)
    plot_widget = FigureCanvasTkAgg(figure, master=window).get_tk_widget()
    plot_widget.grid(row=1, column=0)


def create_button(window: tk.Tk, pressure: PressureSlave,
                  frequency: FrequencySlave):
    button = tk.Button(
        window, text="Нажми!",
        command=lambda: get_pressure_and_show_graphic(window, pressure,
                                                      frequency))
    button.place(x=5, y=5, width=200, height=40)
    button.bind("<Button-1>")


def setup():
    window = configure_window()
    create_button(window)
    configure_canvas(window)
    pressure = PressureSlave()
    frequency = FrequencySlave()
    window.mainloop()
    get_pressure_and_show_graphic(window, pressure, frequency)


if __name__ == '__main__':
    main()
