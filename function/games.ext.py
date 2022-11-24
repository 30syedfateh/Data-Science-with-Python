import pgzrun

HEIGHT = 800
WIDTH = 800

pgzrun.go()

def update():
    #print('updating')
    p.x-=3
    p.angle=-10
    if p.x>WIDTH:
        p.x=10
    print(p.x,p.y)
pgzrun.go()    