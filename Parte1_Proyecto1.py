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
        "max": 0
    }
    Dominio["max"] = Dominio["min"] + 2 * radio
    x, y = 0, 0

    # Eje x:
    h = centroX

    # Eje y:
    k = centroY

    up()
    goto(Dominio["min"], centroY)
    down()

    # Parte superior
    for x in range(Dominio["min"], Dominio["max"]+1):
        y = k + sqrt(radio**2 - (x-h)**2)
        goto(x, y)

    # Parte inferior
    for x in reversed(range(Dominio["min"], Dominio["max"]+1)):
        y = k - sqrt(radio**2 - (x-h)**2)
        goto(x, y)
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