#this will be a funtion for Monsters and Combat_classes to inherit

class entity:
    def deal_damage(self,attacherCombatclass,defendercombatclass):
        # depending on witch class self is you will know to use self.combatclass or self.monsters
        defendercombatclass.hp-=attacherCombatclass.attack
        # for index in range(entity.dictionary):
        #     index[0]-= (index[1]+index[2])
        


        

