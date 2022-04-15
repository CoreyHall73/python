# from owner import Ninja
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


# my_treats = ['Cheese','Lettuce',"Napkins"]
# my_pet_food = ['Salmon','Avocado']

# Lady = Pet("lady", "Cacapoo", "Judges you", "Sniff")
# Corey = Ninja("Corey", "Hall", my_treats, my_pet_food, Lady)

# Corey.walk()
# Corey.feed()
# Corey.bathe()