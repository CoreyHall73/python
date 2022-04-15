from pet import Pet
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


my_treats = ['Cheese','Lettuce',"Napkins"]
my_pet_food = ['Salmon','Avocado']

Lady = Pet("lady", "Cacapoo", "Judges you", "Sniff")
Corey = Ninja("Corey", "Hall", my_treats, my_pet_food, Lady)

Corey.walk()
Corey.feed()
Corey.bathe()