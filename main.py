import tkinter as tk

from matplotlib.figure import Figure

from flows.base_flows import get_pressure_and_show_graphic
from graphics import base as base_graph
from slaves.frequency import Client as FrequencySlave
from slaves.pressure import Client as PressureSlave


def main():
    frequency = FrequencySlave()
    pressure = PressureSlave()
    #
    # start_engine_and_getting_pressure(frequency, pressure)
    #
    window = init_interface(pressure, frequency)
    window.mainloop()


def init_interface(pressure: PressureSlave, frequency: FrequencySlave
                   ) -> tk.Tk:
    # Основное окно программы, содержит в себе холсты
    window = base_graph.create_window()

    # Создание двух кнопок
    first_figure = base_graph.create_figure()
    second_figure = base_graph.create_figure()

    # Инициализация кнопок, привязанных в функциям
    init_button_with_pressure(
        window, first_figure, pressure, frequency, row=0, column=0)
    init_button_with_pressure(
        window, second_figure, pressure, frequency, row=0, column=1)

    # Создание двух холстов
    base_graph.create_tk_widget(window, first_figure, row=1, column=0)
    base_graph.create_tk_widget(window, second_figure, row=1, column=1)

    # Установка сетки для холстов
    base_graph.clear_old_values_lines_and_add_grid(first_figure.number)
    base_graph.clear_old_values_lines_and_add_grid(second_figure.number)

    return window


def init_button_with_pressure(window: tk.Tk, figure: Figure,
                              pressure: PressureSlave,
                              frequency: FrequencySlave, *,
                              row: int, column: int):
    def command(): get_pressure_and_show_graphic(figure, pressure, frequency)

    button = tk.Button(window, text="Нажми!", height=1, width=50,
                       command=command)
    button.grid(row=row, column=column)


if __name__ == '__main__':
    main()
