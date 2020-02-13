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
        opponent.being_attacked(self)
        print('')

    def being_attacked(self, opponent):
        print(self.name + ' being attacked by ' + opponent.name)


rusher = Player('Rusher', 100, 100, 80, 93)
scouter = Player('Scouter', 100, 100, 88, 88)
flanker = Player('Flanker', 100, 100, 77, 91)
sniper = Player('Sniper', 100, 100, 77, 99)

rusher.attacking(scouter)
flanker.attacking(sniper)
