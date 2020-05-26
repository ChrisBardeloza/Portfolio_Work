from monster_class import monster
from skills_base_class import skill
class goblin(skill):
    def create_skill1(self):
        skill1=skill('Bite','Goblin bites', True)
        return skill1
    def create_skill2(self):
        skill2=skill('Bash','Swings club', True)
        return skill2
    def create_skill3(self):
        skill3=skill('Scratch','Scratches', True)
        return skill3
    def __init__(self,name, dictionary={'attack':20, 'defense':20, 'hp':100, 'mp':20}):
        self.name=name
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

class gremlin(skill):
    def create_skill1(self):
        skill1=skill('Stab','Stabs',True)
        return skill1
    def create_skill2(self):
       skill2=skill('Bite','gremlin bites',True)
       return skill2
    def create_skill3(self):
        skill3=skill('Dodge','Dodges Attack', True)
        return skill3
    def __init__(self,name, dictionary={'attack':20, 'defense':20, 'hp':60, 'mp':20}):
        self.name=name
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

class bear(skill):
    def create_skill1(self):
        skill1=skill('Bite','Bear bites',True)
        return skill1
    def create_skill2(self):
        skill2=skill('Roar','Bear Roars!',True)
        return skill2
    def create_skill3(self):
        skill3=skill('Paw Strike','Bear Claws',True)
        return skill3
    def init(self,name, dictionary={'attack':40, 'defense':70, 'hp':100, 'mp':20}):
        self.name=name
        self.skill1=self.create_skill1()
        self.skill2=self.create_skill2()
        self.skill3=self.create_skill3()
        self.dictionary=dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)