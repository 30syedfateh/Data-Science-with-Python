import pgzrun

HIEGHT = 600
WIDTH = 1200

p = Actor('ironman', center=(WIDTH//2, HIEGHT//2))

title = "IRON-MAN GAME"

def draw():
    screen.fill('white')
    screen.draw.text(title,(10,10),fontsize=30, color='black')
    p.draw()

def p_move():
    '''function to move player'''
    if keyboard.left:
        p.x -= 3
    if keyboard.right:
        p.x += 3
    if keyboard.up:
        p.y -= 3
    if keyboard.down:
        p.y += 3

def handle_boundary():
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def update():
    p_move()# function call
    handle_boundary() # function call
    print(p.x, p.y, p.angle)

pgzrun.go()