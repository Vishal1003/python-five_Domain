# It is a feature of object oriented programming which enables a class to present virtual attributes.
# Virtual Attributes : Not actually stored but rather computed when requested by the objects

# Simple Game Structure

class Character:
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    @property
    def hp(self):
        return self._hp
    
    @property
    def name(self):
        return self._name
    
    def take_damage(self, damage) :
        self._hp -= damage
        self._hp = 0 if self._hp < 0 else self._hp
    
    @property
    def is_alive(self):
        return self._hp != 0

    @property
    def is_wounded(self):
        return self._hp < self._max_hp if self._hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive


bil = Character("Bil Farmer", 100)
print(bil.hp)   # So read only (by setting property)

