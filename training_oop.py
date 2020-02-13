class Player:
    def __init__(self, inputName, inputHealth, inputArmor, inputDefense, inputAttack):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        self.defense = inputDefense
        self.attack = inputAttack

    # 'opponent' merupakan object jadi penamaan argumennya bisa pake nama Class nya yaitu 'Player'
    # yg jelas lawannya harus pake argumen yg sama, jadi argument 'opponent' di attacking opponent.name
    def attacking(self, opponent):
        print(self.name + ' attacking ' + opponent.name)
        opponent.being_attacked(self, self.attack)
        print('\n')

    def being_attacked(self, opponent, opponent_damage):
        print(self.name + ' being attacked by ' + opponent.name)

        damage = abs(opponent_damage - self.defense)
        print('damage taken => ' + self.name +
              ' , damage point => ' + str(damage))

        # sudah berubah jadi integer
        self.health -= damage
        print('armor == ' + self.name + ' , remaining ==> ' + str(self.health))


# poisiton = class('name', health, armor, defense, attack)
rusher = Player('Rusher', 100, 100, 80, 93)
scouter = Player('Scouter', 100, 100, 88, 88)
flanker = Player('Flanker', 100, 100, 77, 91)
sniper = Player('Sniper', 100, 100, 77, 99)

rusher.attacking(scouter)
rusher.attacking(sniper)
rusher.attacking(flanker)

scouter.attacking(rusher)
scouter.attacking(flanker)
scouter.attacking(sniper)

flanker.attacking(sniper)
flanker.attacking(rusher)
flanker.attacking(scouter)

sniper.attacking(flanker)
sniper.attacking(scouter)
sniper.attacking(rusher)
