# Combat Class 

class warrior:
    def slash(self):
        print('Swings Sword')
    def thrust(self):
        print('Thrust')
    def shield(self):
        print('Blocks Attack')
    def init(self, dictionary={'attack':60, 'defense':70, 'hp':100, 'mp':20}):
        for k, v in dictionary.items():
            setattr(self, k, v)


class mage:
    def fire_bolt(self):
        print('Launches Fire Bolt')
    def heal(self):
        print('Heals Target')
    def protect(self):
        print('Blocks Attack')
    def __init__(self,dictionary={'attack':80,'defense':40, 'hp':40, 'mp':90}):
        for k, v in dictionary.items():
            setattr(self, k, v)

class ranger:
    def barrage(self):
        print('shoots 5 arrows')
    def dodge(self):
        print('Dodges Attack')
    def stike(self):
        print('Melee Target')
    def __init__(self,dictionary={'attack':70, 'defense':60, 'hp':60, 'mp':60}):
        for k, v in dictionary.items():
            setattr(self, k, v)