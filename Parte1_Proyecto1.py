from tkinter.ttk import setup_master
from turtle import *
from math import *

# Dibuja un círculo usando el algoritmo de Bresenham_Midpoint.
def drawCircle(centroX: int, centroY: int, radio: int):
    x, y, r = radio, 0, radio

    P = 1 - r

    up()
    while x > y:
        y += 1

        if P <= 0:
            P = P + 2*y + 1

        else:
            x -= 1
            P = P + 2*y - 2*x + 1

        if x < y:
            break

        goto(x + centroX, y + centroY)
        dot(2, "purple")
        goto(-x + centroX, y + centroY)
        dot(2, "purple")
        goto(x + centroX, -y + centroY)
        dot(2, "purple")
        goto(-x + centroX, -y + centroY)
        dot(2, "purple")

        if x != y:
            goto(y + centroX, x+ centroY)
            dot(2, "purple")
            goto(-y + centroX, x + centroY)
            dot(2, "purple")
            goto(y + centroX, -x + centroY)
            dot(2, "purple")
            goto(-y + centroX, -x + centroY)
            dot(2, "purple")

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

speed(0)
drawCartesianPlane()
drawCircle(0, 0, 100)
drawSquare()
done()