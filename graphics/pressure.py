from tkinter import Tk as Window


def paint_graph_for_pressure(window: Window):
    pass

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math
import random

xtek = 0
global xxx, yyy1, yyy2, yyy3, yyy4
xxx = []
yyy1 = []
yyy2 = []
yyy3 = []
yyy4 = []


def updateGraphRND():
    global updateGraphRND
    global xtek
    plt.clf()
    xtek += 1
    xxx.append(xtek)
    yyy1.append(round(random.random(), 2))
    yyy2.append(round(random.random(), 2))
    yyy3.append(round(random.random(), 2))
    yyy4.append(round(random.random(), 2))
    plt.grid(True)
    plt.plot(xxx,yyy1,'r',xxx,yyy2,'g',xxx,yyy3,'b',xxx,yyy4,'y')
    fig.canvas.draw()
    print(xtek, xxx, yyy1, yyy2, yyy3, yyy4)


def ClearGraph():
    global ClearGraph
    global xtek
    global xxx
    global yyy1, yyy2, yyy3, yyy4
    xtek = 0
    xxx = []
    yyy1 = []
    yyy2 = []
    yyy3 = []
    yyy4 = []
    plt.clf()
    plt.grid(True)
   # plt.plot(xxx,yyy)
    fig.canvas.draw()
    print(xtek, xxx, yyy1, yyy2, yyy3, yyy4)

fig = plt.figure(1)         # Инициализировать фигуру matplotlib для построения графиков

# Special type of "canvas" to allow for matplotlib graphing
# Специальный тип "холста" для построения графиков в matplotlib
plot_widget = FigureCanvasTkAgg(fig, master=root).get_tk_widget()

# Add the plot to the tkinter widget
# Добавляем график в виджет tkinter
plot_widget.grid(row=1, column=0)
# Create a tkinter button at the bottom of the window and link it with the updateGraph function
tk.Button(root, text="следующая точка", command=updateGraphRND).grid(row=0, column=0)
tk.Button(root, text="чисто", command=ClearGraph).grid(row=0, column=1)
root.mainloop()