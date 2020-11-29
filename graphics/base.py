import tkinter as tk

from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def create_figure() -> Figure:
    return pyplot.figure()


def create_tk_widget(figure: Figure, window: tk.Tk) -> tk.Canvas:
    plot_widget = FigureCanvasTkAgg(figure, master=window).get_tk_widget()
    plot_widget.grid(row=1, column=0)
    return plot_widget
