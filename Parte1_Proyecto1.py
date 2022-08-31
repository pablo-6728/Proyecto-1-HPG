from turtle import *


#TODO: algoritmo que genere un circulo
def drawCircle():
    pass


#TODO: algoritmo que genere un cuadrado
def drawSquare():
    #para esta parte tenemos que hacer 4 lineas usando el algoritmo DDA
    pass


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
done()