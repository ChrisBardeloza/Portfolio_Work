#This is for the race attribute in Character class
from skills_base_class import skill
class human(skill):
    def create_skill0(self):
        skill0=skill('Adrenaline Rush', 'Speed Increase', False)
        return skill0
    def __init__(self):
        self.skill0=self.create_skill0()

    #Adrenaline Rush
        #have 2 turns instead of 1 per round
            #can only activate after taking damage


class elf(skill):
    def create_skill0(self):
        skill0=skill('Protection of the Ancients', 'Regenerates HP', False )
        return skill0
    def __init__(self):
        self.skill0=self.create_skill0()
    #Protections of the Ancestors
        #Regen 20 hp per round
            # starts if is_in_combat==true


class dwarf(skill):
    def create_skill0(self):
        skill0=skill('Battle Cry', 'Increases Combat Tactics', False)
        return skill0
    def __init__(self):
        self.skill0=self.create_skill0()
    #Battle cry 
        # Take 50% less damage and do 50% more damage
            # activate below 60% hp
