class Job:
    # class variable
    jumlah_Job = 0

    def __init__(self, input_name, input_life, input_armor, input_power):
        # instance variable
        self.name = input_name
        self.life = input_life
        self.armor = input_armor
        self.power = input_power

        Job.jumlah_Job += 1

    # method void / method TANPA RETURN & TANPA ARGUMEN
    def hiFive(self):
        print("mari kita tos tosan " + self.name)

    # method DENGAN ARGUMEN & TANPA RETURN
    def boosting(self, boost):
        self.life += boost

    def getBoost(self):
        return self.life


Job1 = Job('Rusher', 56, 80, 99)
Job2 = Job('Ranger', 40, 95, 65)
Job3 = Job('Scouter', 70, 90, 83)
Job4 = Job('Flanker', 60, 80, 93)

print(Job1.__dict__)
print(Job2.__dict__)
print(Job3.__dict__)
print(Job4.__dict__)

Job1.hiFive()
Job1.boosting(35)

print(Job1.life)
print(Job1.getBoost())
