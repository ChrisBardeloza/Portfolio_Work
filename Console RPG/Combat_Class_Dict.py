# Combat Class 
from skills_base_class import skill

class warrior(skill):
    def create_skill1(self):
        skill1=skill('slash','Swings Sword',True)
        return skill1
    def create_skill2(self):
        skill2=skill('thrust','Thrust Sword',True)
        return skill2
    def create_skill3(self):
        skill3=skill('shield','Blocks attack',False)
        return skill3
         #negate attack
    def __init__(self, dictionary={'attack':60, 'defense':70, 'hp':100, 'mp':20}):
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)



class mage(skill):
    def create_skill1(self):
        skill1=skill('fire bolt', 'Launches Fire Bolt', True)
        return skill1
    def create_skill2(self):
        skill2=skill('heal','Heals Target', False)
        return skill2
    def create_skill3(self):
        skill3=skill('protect','Blocks Attack', False)
        return skill3
    def __init__(self, dictionary={'attack':80,'defense':40, 'hp':40, 'mp':90}):
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

class ranger(skill):
    def create_skill1(self):
        skill1=skill('barrage','shoots 5 arrows',True)
        return skill1
    def create_skill2(self):
        skill2=skill('dodge','Dodges Attack',False)
        return skill2
    def create_skill3(self):
        skill3=skill('strike','Melee Target',True)
        return skill3
    def __init__(self, dictionary={'attack':70, 'defense':60, 'hp':60, 'mp':60}):
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)