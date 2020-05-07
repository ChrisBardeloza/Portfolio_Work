#this is the actual quests
from quest_class import quest
class combat_quest(quest):
    def openingDialogue:
        print('I need your help, adveturer!')
    def promptPlayerToAccept:
        accepted = input('Will you help!?')
        # if (accepted == 'yes')
            # self.is_accepted = true
        # return self.is_accepted
    def doQuest:
        # do combatLoop, imported from game_loops, with provided monster
