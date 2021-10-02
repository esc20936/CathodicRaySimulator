import tkinter as tk
import tkinter.messagebox as msg
from typing import Sequence
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import parametric as prm
import numpy as np
import json
import fileW as fw
root= tk.Tk() 
#Grafica Principal
figure1 = plt.Figure(figsize=(4,3), dpi=100)
ax = figure1.add_subplot(111)
ax.set_facecolor('xkcd:forest green')
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
#Grafica Horizontal
figure2 = plt.Figure(figsize=(4,3), dpi=100)
ax2 = figure2.add_subplot(111)
ax2.set_facecolor('xkcd:forest green')
bar2 = FigureCanvasTkAgg(figure2, root)
bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

#Grafica Horizontal
figure3 = plt.Figure(figsize=(4,3), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.set_facecolor('xkcd:forest green')
bar3 = FigureCanvasTkAgg(figure3, root)
bar3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)


def readJson():
    graphdata = open("test1.json","r")
    data = json.load(graphdata)
    graphdata.close()
    return data

def updateJson():
    try:
        dic={
        "e": -1.602e-19,
        "me": 9.11e-31,
        "l": 20,
        "v": 7.90e5,
        "d": 0.003,
        "phase": float(phaseEntry.get()),
        "w": float(w1Entry.get()),
        "w2": float(w2Entry.get())
        }
        fw.updateValues(dic)
    except ValueError:
        msg.showerror(title="VALOR INVALIDO",message="Los valores deben ser numericos")
def animate(i):
    graphdata = open("test1.json","r")
    data = json.load(graphdata)
    graphdata.close()
    e=data['e']
    me=data['me']
    l=data['l']
    v=data['v']
    d=data['d']
    phase=data['phase']
    w=data['w']
    w2=data['w2']
    data1 = {'X': prm.get_x(e,me,l,v,d,w2,phase),
            'Y': prm.get_y(e,me,l,v,d,w)
            }
    datax={'X':data1['X']}
    datay={'Y':data1['Y']}


    df1 = DataFrame(data1,columns=['X','Y'])

    dfx= DataFrame(datax,columns=['X'])
    dfy= DataFrame(datay,columns=['Y'])
    ax.clear()
    ax.plot(data1['X'],data1['Y'],color="yellow")
    ax2.clear()
    ax2.plot(datax['X'],prm.createIndexes(datax['X']),color='yellow')
    ax3.clear()
    ax3.plot(prm.createIndexes(datay['Y']),datay['Y'],color='yellow')


    ax.set_title('Vista frontal')
    ax2.set_title('Vista Horizontal')
    ax3.set_title('Visto Vertical')
diccionarioValores = readJson()
ani = animation.FuncAnimation(figure1,animate,interval=500)
ani2 = animation.FuncAnimation(figure2,animate,interval=500)
ani3 = animation.FuncAnimation(figure3,animate,interval=500)
canvas1 = tk.Canvas(root, width = 400, height = 500)
canvas1.pack()




w1Entry = tk.Entry(root) 
w1Entry.insert(0,diccionarioValores['w'])

canvas1.create_window(200, 140, window=w1Entry)
w1 = tk.Label(root, text = "W1") 
canvas1.create_window(120,140,window=w1)


w2Entry = tk.Entry(root)
w2Entry.insert(0,diccionarioValores['w2'])

canvas1.create_window(200, 170, window=w2Entry)
w2 = tk.Label(root, text = "W2") 
canvas1.create_window(120,170,window=w2)


phaseEntry = tk.Entry(root) 
phaseEntry.insert(0,diccionarioValores['phase'])

canvas1.create_window(200, 200, window=phaseEntry)
phase = tk.Label(root, text = "Phase") 
canvas1.create_window(120,200,window=phase)

button1 = tk.Button(text='Update', command=updateJson)
canvas1.create_window(200, 240, window=button1)



plt.show()
root.mainloop()