from pgzero.actor import Actor

class MyActor(Actor):
    speedx = 5
    speedy = 5

    def __init__(self, image, pos=..., anchor=..., **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.speedx = self.speedy = speed

    def move(self):
        self.x += self.speedx
        self.y += self.speedy

# actor = MyActor('ironman',(100,100),speed = 5)
print(dir(MyActor))
print(list(filter(lambda i:not i.startswth('__')or not i.startswith('_'))))

# list comprehension