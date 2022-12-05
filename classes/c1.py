class Cat:
    name = ""
    age = 0
    furcolor = ""
    breed = ""

    def eat(self):
        print("Cat is eating!")

    def sleep(self):
        print("Cat is sleeping!")
    
# creating objects
tom = Cat()
simba = Cat()
tom.name = "Tom"
tom.age = 3
tom.furcolor = 'gray'
tom.breed = 'City Cat'
simba.name = "Simba"
simba.age = 5
simba.furcolor = 'sunny'
simba.breed = 'Lion'
# Calling methods
tom.eat()
simba.sleep()
tom.eat()

# displaying attributes
print(tom.name,tom.age,tom.furcolor,tom.breed)
print(simba.name,simba.age,simba.furcolor,simba.breed)


  