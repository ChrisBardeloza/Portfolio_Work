#this is the actual quests
from quest_class import quest
from combat_quests import combat_quest
from Towns import *

quest1=combat_quest('Hello traveler.  There is a group of Goblins messing with my supply routes. I need you to help me out and deal with them.', 
'Supply Routes',
'Defeat the Goblins',
'Thank you!',
False
  )

quest2=combat_quest('Hello Traveler.  There is a Bear terrorizing the road coming from Bucsden to Eaglton.  I need you to kill it.',
'Clear the Road',
'Defeat the Bear',
'Thank you!',
False)