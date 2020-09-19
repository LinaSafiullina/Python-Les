import random

class Animals():
    def __init__(self, name):
        self.name = name

    def __add__(self, b):
        new_name = self.name +"о" + b.name
        return Animals(new_name)


animals= ["кот", "волк", "пёс", "медоед", "осел", "додо"]

animals_cl=[]

for a in animals:
    animals_cl.append(Animals(a))

new_animal = random.choice(animals_cl) + random.choice(animals_cl)
print("Новое животное зовут", new_animal.name)
