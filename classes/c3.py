import random

class Mylist(list): # inherits from list
    pass
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)



# object

a = Mylist([12,121,3,2,4,5,6,67,7,77,])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list = ",a.get_random())