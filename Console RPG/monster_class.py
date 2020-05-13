from entity import entity

class monster(entity):
    def __init__(self,name,monster_class):
        self.name=name
        self.monster_class=monster_class

    def do_damage(self,target):
        self.deal_damage(self.monster_class,target.combat_class)