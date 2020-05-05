class goblin:
    def __init__(self, name):
        self.name=name
    def bite(self):
        print('Goblin bites')
    def bash(self):
        print('Swings club')
    def scratch(self):
        print('Scratches')
    def init(self, dictionary={'attack':20, 'defense':20, 'hp':100, 'mp':20}):
        for k, v in dictionary.items():
            setattr(self, k, v)

class gremlin:
    def __init__(self, name):
        self.name=name
    def stab(self):
        print('Stabs')
    def bite(self):
        print('gremlin bites')
    def dodge(self):
        print('Dodges Attack')
    def init(self, dictionary={'attack':20, 'defense':20, 'hp':60, 'mp':20}):
        for k, v in dictionary.items():
            setattr(self, k, v)

class bear:
    def __init__(self, name):
        self.name=name
    def bite(self):
        print('Bear bites')
    def roar(self):
        print('Bear Roars!!!!!')
    def claw(self):
        print('Bear Claws')
    def init(self, dictionary={'attack':40, 'defense':70, 'hp':100, 'mp':20}):
        for k, v in dictionary.items():
            setattr(self, k, v)