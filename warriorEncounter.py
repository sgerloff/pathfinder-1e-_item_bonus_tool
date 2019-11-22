import random
from Classes.warriorNPC import WarriorNPC

def randomMeleeWarrior( level):
    races = ["human", "halforc", "halfelf", "dwarf", "gnome"]
    race = random.choice(races)
    armors = ["medium", "heavy"]
    armor = random.choice(armors)
    shields = ["light", "heavy", "tower"]
    weapons2H = ["halberd2H", "curved2H", "mace2H", "sword2H", "axe2H", "club2H", "sword", "longsword", "axe", "hammer", "curved", "mace"]
    weapons1H = ["sword", "longsword", "axe", "hammer", "curved", "mace"]
    
    shieldBool = random.randrange(0,2,1)
    if shieldBool == 0:
        weapon = random.choice(weapons2H)
        shield = ""
    if shieldBool == 1:
        weapon = random.choice(weapons1H)
        shield = random.choice(shields)
    return WarriorNPC(level, "melee", race, armor, shield, weapon)

def randomRangedWarrior(level):
    races = ["human", "halfelf", "halfling", "elvish"]
    weapons = ["bow", "longbow", "crossbow", "heavycrossbow"]
    return WarriorNPC(level, "range", random.choice(races), "light", "", random.choice(weapons))
    
        
                
warriorR = randomMeleeWarrior(9)
warriorR.printSummary()
print("")
warriorR = randomRangedWarrior(9)
warriorR.printSummary()
    