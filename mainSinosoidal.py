import tkinter as tk
from tkinter.constants import LEFT
import tkinter.messagebox as msg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import parametric as prm
import json
import fileW as fw
root= tk.Tk()
root.title("Cathodic Ray Tube simulator")

sinusoidal=True

colores=["lightyellow","khaki","yellow"]
color="lightyellow"

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
def cambiarColor(_=None):
    pos =int(voltajeAceleracion.get())-1
    color=colores[pos]

def cambiarModo():
    global sinusoidal
    print(sinusoidal)
    sinusoidal= not sinusoidal
    if sinusoidal:
        LabelModo.config(text="Mode: sinusoidal")
        w1Entry.config(state="normal")
        w2Entry.config(state="normal")
        phaseEntry.config(state="normal")
        VoltajeX.config(state="disabled")
        VoltajeY.config(state="disabled")

    else:
        w1Entry.config(state="disabled")
        w2Entry.config(state="disabled")
        phaseEntry.config(state="disabled")
        LabelModo.config(text="Mode: normal")
        VoltajeX.config(state="normal")
        VoltajeY.config(state="normal")

def readJson():

    file = "sinusoidal.json"
    graphdata = open(file,"r")
    data = json.load(graphdata)
    graphdata.close()
    return data

def updateJson(_=None):

    try:
        dic={
        "e": -1.602e-19,
        "me": 9.11e-31,
        "l": 20,
        "v": 7.90e5,
        "d": 0.003,
        "phase": float(phaseEntry.get()),
        "w": float(w1Entry.get()),
        "w2": float(w2Entry.get()),
        "vx":float(VoltajeX.get()),
        "vy":float(VoltajeY.get()),
        "color":colores[int(voltajeAceleracion.get())-1]

        }
        
        fw.updateValues(dic)
    except ValueError:
        msg.showerror(title="VALOR INVALIDO",message="Los valores deben ser numericos")

def animate(i):
    graphdata = open("sinusoidal.json","r")
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
    vx = data['vx']
    vy=data['vy']
    color = data['color']
    data1 = {'X': prm.get_x(e,me,l,v,d,w2,phase,sinusoidal,vx),
            'Y': prm.get_y(e,me,l,v,d,w,sinusoidal,vy)
            }

    datax={'X':data1['X']}
    datay={'Y':data1['Y']}


    if sinusoidal:

        
        ax.clear()
        ax.plot(data1['X'],data1['Y'],color=color)
        ax2.clear()
        ax2.plot(datax['X'],prm.createIndexes(datax['X']),color=color)
        ax3.clear()
        ax3.plot(prm.createIndexes(datay['Y']),datay['Y'],color=color)

    else:


        ax.clear()
        ax.set_xlim([-190, 190])
        ax.set_ylim([-190, 190])
        ax.spines.left.set_position('center')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('center')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.plot(data1['X'],data1['Y'],marker='o',color=color)
        
        ax2.clear()
        ax2.plot(datax['X'],0,marker='o',color=color)
        ax2.set_xlim([-190, 190])
        ax2.set_ylim([-190, 190])
        ax3.clear()
        ax3.plot(0,datay['Y'],marker='o',color=color)
        ax3.set_xlim([-190, 190])
        ax3.set_ylim([-190, 190])
        

        

    ax.set_title('Front View')
    ax2.set_title('Horizontal View')
    ax3.set_title('Vertical View')


diccionarioValores = readJson()
ani = animation.FuncAnimation(figure1,animate,interval=500)
ani2 = animation.FuncAnimation(figure2,animate,interval=500)
ani3 = animation.FuncAnimation(figure3,animate,interval=500)
canvas1 = tk.Canvas(root, width = 400, height = 500)
canvas1.pack()




VoltajeX  =tk.Scale(
    None,
    from_ = -0.1,
    to = 0.1,
    orient = tk.HORIZONTAL ,
    resolution = .01,
    ####################
    command=updateJson
    ####################
)

canvas1.create_window(200, 50, window=VoltajeX)
vxLabel = tk.Label(root, text = "Voltage X") 
canvas1.create_window(120,55,window=vxLabel)

VoltajeY  =tk.Scale(
    None,
    from_ = -0.1,
    to = 0.1,
    orient = tk.HORIZONTAL ,
    resolution = .01,
    ####################
    command=updateJson
    ####################
)

canvas1.create_window(200, 100, window=VoltajeY)
vyLabel = tk.Label(root, text = "Voltage Y") 
canvas1.create_window(120,105,window=vyLabel)

voltajeAceleracion =tk.Scale(
    None,
    from_ = 1,
    to = 3,
    orient = tk.HORIZONTAL ,
    resolution = 1,
    ####################
    command=updateJson
    ####################
)
canvas1.create_window(200, 150, window=voltajeAceleracion)

va = tk.Label(root, text = "acceleration voltage level") 
canvas1.create_window(70,150,window=va)

w1Entry = tk.Entry(root)
w1Entry.insert(0,diccionarioValores['w'])
canvas1.create_window(200, 200, window=w1Entry)

w1 = tk.Label(root, text = "W1") 
canvas1.create_window(120,200,window=w1)


w2Entry = tk.Entry(root)
w2Entry.insert(0,diccionarioValores['w2'])
canvas1.create_window(200, 230, window=w2Entry)

w2 = tk.Label(root, text = "W2") 
canvas1.create_window(120,230,window=w2)


phaseEntry = tk.Entry(root) 
phaseEntry.insert(0,diccionarioValores['phase'])
canvas1.create_window(200, 260, window=phaseEntry)

phase = tk.Label(root, text = "Phase") 
canvas1.create_window(120,260,window=phase)

button1 = tk.Button(text='Update', command=updateJson)
canvas1.create_window(200, 300, window=button1)





buttonCambiar = tk.Button(text='Change mode', command=cambiarModo)
canvas1.create_window(200, 10, window=buttonCambiar)

LabelModo = tk.Label(root, text = "Mode: Sinusoidal") 
canvas1.create_window(310,10,window=LabelModo)


plt.show()
root.mainloop()