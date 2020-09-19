import random

class warrior:
    health = 100

    def hit(self, target1, target2):
        if target1.health>0:
            target1.health-=20
            if target2 == warrior1:
                target2 = "Warrior1"
            if target2 == warrior2:
                target2 = "Warrior2"
            print(target2, " has attacked")
            print(target1.health, "left")
        if target1.health ==0:
            print(target2, " has won")

warrior1 = warrior()
warrior2 = warrior()

q = int(input("Enter 1 to let some warrior attack. Enter 2 to stop program:"))

while q!=2:
    if q ==1:
        j = random.randint(1,3)
        if j%2 == 0:
            warrior1.hit(warrior2, warrior1)
            q = int(input("Enter 1 to let some warrior attack:"))
        else:
            warrior2.hit(warrior1, warrior2)
            q = int(input("Enter 1 to let some warrior attack:"))
    else:
         print("Wrong input.")
         break
