import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def create_figure() -> Figure:
    figure = plt.figure()
    return figure


def pre_init() -> None:
    matplotlib.use('TkAgg')  # set backend for plot as Tkinter


def clear_old_values_lines_and_add_grid(figure_number: int):
    plt.figure(figure_number)
    plt.clf()
    plt.grid(True)


def close_graph(figure: Figure) -> None:
    plt.close(figure)


def create_window() -> tk.Tk:
    window = tk.Tk()
    window.geometry('800x600')
    return window


def create_tk_widget(window: tk.Tk, figure: Figure, *, row, column
                     ) -> tk.Canvas:
    # Специальный тип "холста" для построения графиков в matplotlib
    canvas = FigureCanvasTkAgg(figure, master=window)
    # Добавляем график в виджет tkinter
    tk_widget = canvas.get_tk_widget()
    tk_widget.grid(row=row, column=column)
    return tk_widget
