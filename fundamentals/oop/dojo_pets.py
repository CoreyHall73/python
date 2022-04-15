class Ninja: 
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print('walked')
        return self

    def feed(self):
        self.pet.eat()
        print("Full")
        return self

    def bathe(self):
        self.pet.pet_noise()
        



class Pet:
    def __init__ (self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy, self.health)
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        print(self.health, self.energy)
        return self

    def pet_noise(self):
        print(self.noise)

my_treats = ['Cheese','Lettuce',"Napkins"]
my_pet_food = ['Salmon','Avocado']

Lady = Pet("lady", "Cacapoo", "Judges you", "Sniff")
Corey = Ninja("Corey", "Hall", my_treats, my_pet_food, Lady)

Corey.walk()
Corey.feed()
Corey.bathe()
