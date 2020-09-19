import random

class Solder:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def follow_the_hero(self, hero):
        print("Солдат под номером ", self.number, " следует за героем ", hero.number)

class Hero(Solder):
    def __init__(self, number, team, level):
        Solder.__init__(self, number, team)
        self.level = level

    def growth_level(self):
        self.level +=1
        print("У героя ", self.number, "повысился уровень")

s1 = []
s2 = []

h1 = Hero(1, 1, 0)
h2 = Hero(2, 2, 0)

n=2

while n<22:
    s = Solder(n+1, random.randint(1,3))
    n+=1

    if s.team ==1:
        s1.append(s)
        s2.append(s)
    elif s.team == 2:
        s1.append(s)
        s2.append(s)

print("Количество солдат героя", h1.number, "составляет", len(s1), \
      "\nКоличество солдат героя", h2.number, "составляет", len(s2))

if len(s1) > len(s2):
    h1.growth_level()
    s = random.choice(s1)
    s.follow_the_hero(h1)
elif len(s1) < len(s2):
    h2.growth_level()
    s = random.choice(s2)
    s.follow_the_hero(h2)
else:
    print("Уровни равные")
