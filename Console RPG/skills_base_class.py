#this is for skill action
class skill:
    def __init__(self,name,description,is_attack_skill):
        self.name=name
        self.description=description
        self.is_attack_skill=is_attack_skill
    
    def executeskill(self,caster,target):
        return caster,target

  