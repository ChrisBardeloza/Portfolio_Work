# Combat Class 

class worrior:
    def slash(self):
        print('Swings Sword')
    def thrust(self):
        print('Thrust')
    def shield(self):
        print('Blocks Attack')
    worrior=worrior()
    worrior.attack=60
    worrior.defense=70
    worrior.hp=100
    worrior.mp=20
    {'attack':60, 'defense':70, 'hp':100, 'mp':20}

class mage:
    def fire_bolt(self):
        print('Launches Fire Bolt')
    def heal(self):
        print('Heals Target')
    def protect(self):
        print('Blocks Attack')
    def __init__(self,stats={'attack':80,'defense':40, 'hp':40, 'mp':90})

class ranger:
    def barrage(self):
        print('shoots 5 arrows')
    def dodge(self):
        print('Dodges Attack')
    def stike(self):
        print('Melee Target')
    def __init__(self,stats={'attack':70, 'defense':60, 'hp':60, 'mp':60})