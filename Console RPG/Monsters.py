class goblin:
    def bite(self):
        print('Goblin bites')
    def bash(self):
        print('Swings club')
    def scratch(self):
        print('Scratches')
    def __init__(self,name, dictionary={'attack':20, 'defense':20, 'hp':100, 'mp':20}):
        self.dictionary=dictionary
        self.name=name
        for k, v in dictionary.items():
            setattr(self, k, v)

class gremlin:
    def stab(self):
        print('Stabs')
    def bite(self):
        print('gremlin bites')
    def dodge(self):
        print('Dodges Attack')
    def __init__(self,name, dictionary={'attack':20, 'defense':20, 'hp':60, 'mp':20}):
        self.dictionary=dictionary
        self.name=name
        for k, v in dictionary.items():
            setattr(self, k, v)

class bear:
    def bite(self):
        print('Bear bites')
    def roar(self):
        print('Bear Roars!!!!!')
    def claw(self):
        print('Bear Claws')
    def init(self,name, dictionary={'attack':40, 'defense':70, 'hp':100, 'mp':20}):
        self.dictionary=dictionary
        self.name=name
        for k, v in dictionary.items():
            setattr(self, k, v)