#this is the actual quests
from quest_class import quest
class combat_quest(quest):
    def openingDialogue(self):
        print('I need your help, adveturer!')
    def promptPlayerToAccept(self):
        accepted='yes'
        answer=''
        
        while answer != accepted:
            answer=input('Will you help!?:')
        
        if accepted== 'yes':
            self.is_accepted=True
            return self.is_accepted
        # if (accepted == 'yes')
            # self.is_accepted = true
        # return self.is_accepted
    # def doQuest():
    #     if self.is_accepted==true:

        # do combatLoop, imported from game_loops, with provided monster
