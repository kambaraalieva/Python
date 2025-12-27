class Character():
    def __init__(self, name, _hp):
        self.name = name
        self.hp = _hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(100, value))

    def status(self):
        text = f"{self.name}: HP = {self.hp}"
        print(text)

    def heal(self, amount):
        self.hp += amount

    def take_damage(self, amount):
            self.hp -= amount

a = Character("Aijamal", 47)
a.status()
a.heal(10)
a.status()
a.take_damage(10)
a.status()

b = Character("Aida", -2)
b.status()
b.take_damage(10)
b.status()