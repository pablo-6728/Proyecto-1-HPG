from tkinter.ttk import setup_master
from turtle import *
from math import *


#TODO: algoritmo que genere un circulo
# Dibuja un círculo
# Toma como referencia el centro tanto en x como en y, y el radio,
# luego dibuja el círculo con las parámetros dados.
def drawCircle(centroX: int, centroY: int, radio: int):
    # Fórmula para generar el círculo:
    # y = k +- sqrt(r^2 - (x-h)^2)

    Dominio = {
        "min": centroX - radio,
        "max": centroX + radio
    }
    x, y = 0, 0

    # Eje x:
    h = centroX

    # Eje y:
    k = centroY

    up()
    goto(Dominio["min"], centroY)

    # Parte superior
    for x in range(Dominio["min"], Dominio["max"]+1):
        y = k + sqrt(radio**2 - (x-h)**2)
        goto(x, y)
        dot(2, "blue")

    # Parte inferior
    for x in reversed(range(Dominio["min"], Dominio["max"]+1)):
        y = k - sqrt(radio**2 - (x-h)**2)
        goto(x, y)
        dot(2, "blue")

def DDA(x1: int, y1: int, x2: int, y2: int):
    dy = y2 - y1
    dx = x2 - x1

    steps = 0

    #asignar los pasos dependiendo de los deltas
    if (dx > dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    #pendientes con la division por 0
    try:
        Xinc = dx/steps
        Yinc = dy/steps
    except NameError:
        print('Division por 0')

    up()
    for i in range(steps):
        x = x1
        y = y1
        goto(x, y)
        dot(2, "red")

        x1 = x + Xinc
        y1 = y + Yinc


#TODO: algoritmo que genere un cuadrado
def drawSquare():
    #para esta parte tenemos que hacer 4 lineas usando el algoritmo DDA
    DDA(-100, 0, 0, 100)
    DDA(0, 100, 100, 0)
    DDA(100, 0, 0, -100)
    DDA(0, -100, -100, 0)


#Eje de coordenadas
def drawCartesianPlane():
    up()
    goto(300, 0)
    pendown()
    goto(-300, 0)
    up()
    goto(0,300)
    pendown()
    goto(0,-300)


drawCartesianPlane()
drawCircle(0, 0, 100)
drawSquare()
done()