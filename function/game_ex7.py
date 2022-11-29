import pgzrun

WIDTH = 1000
HEIGHT = 600

scr=0

def draw():
    if scr==0:
       screen.fill('black')
       screen.draw.text('Amazing game',(WIDTH/2,HEIGHT/2),fontsize=100, color='white',align='center')
       screen.draw.text('Press space to start',center=(WIDTH/2,HEIGHT/2+100),fontsize=50,color='white',align='center')
    elif scr==1:
         screen.fill('white')
         screen.draw.text('Game is running',(WIDTH/2,HEIGHT/2),fontsize=100, color='black',align='center')
         screen.draw.text('Press escape to end the Game',center=(WIDTH/2,HEIGHT/2+100),fontsize=50,color='red',align='center')






def update():
    global scr
    if keyboard.space:
        scr=1
    elif keyboard.space and scr==0:

pgzrun.go()