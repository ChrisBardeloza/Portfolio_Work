# Character sheet
from entity import entity
class Character(entity):
    def __init__(self, Name, Race, Gender,Combat_Class):
        self.name=Name
        self.race=Race
        self.gender=Gender
        self.combat_class=Combat_Class
      

    def do_damage(self,target):
        self.deal_damage(self.combat_class,target.monster_class)