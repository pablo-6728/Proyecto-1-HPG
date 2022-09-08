from turtle import *
pos = [
        [-100 , 100], 
        [-100, -100], 
        [100, -100], 
        [100, 100]
    ]

#funcion que mueve el cuadrado generado 50 espacios a la derecha
def moveSquare(pos):
    up()
    clear()
    newpos = pos

    for i in range(0, 4):
        for j in range(0, 2):
            
            newpos[i][j] = newpos[i][j] + 50
    
    
    #dibujo del nuevo cuadrado
    goto(newpos[0][0], newpos[0][1])
    down()
    goto(newpos[1][0], newpos[1][1])
    goto(newpos[2][0], newpos[2][1])
    goto(newpos[3][0], newpos[3][1])
    goto(newpos[0][0], newpos[0][1])



def drawSquare(pos):
    goto(pos[0][0], pos[0][1])
    down()
    goto(pos[1][0], pos[1][1])
    goto(pos[2][0], pos[2][1])
    goto(pos[3][0], pos[3][1])
    goto(pos[0][0], pos[0][1])

    for i in range(4):
        moveSquare(pos)
    

up()
speed(0)
drawSquare(pos)
done()