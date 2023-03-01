class Pokemon:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.original_hp = hp
        print(f"{self.name}'s attack:{self.attack}, hp:{self.hp}")


    def check_hp(self):
        print(f"{self.name}'s current hp is {self.hp}")


    def fight(self, enemy):
        if self.hp == 0:
            print(f"{self.name} can't fight")
        else:
            print(f"{self.name} is fighting {enemy.name}")
            if enemy.hp >= self.attack:
                enemy.hp -= self.attack
            else:
                enemy.hp = 0


    def recover(self):
        if self.hp + 20 >= self.original_hp:
            self.hp = self.original_hp
        else:
            self.hp += 20
        print(f"{self.name} recover")


# pikachu = Pokemon('Pikachu', 20, 50)
# pikachu.check_hp()
# charmander = Pokemon('Charmander', 15, 30)
# charmander.check_hp()
# pikachu.fight(charmander)
# charmander.check_hp()
# pikachu.fight(charmander)
# charmander.check_hp()
# charmander.recover()
# charmander.check_hp()
# charmander.recover()
# charmander.check_hp()
