import random
from Classes.warriorNPC import WarriorNPC

# NPC Classes
warrior = WarriorNPC(9, "melee", "humanoid", "medium", "", "sword")
# pb.getOptimalBonusSet(warrior)
warrior.heroic = True
warrior.printSummary()

def randomMeleeWarrior( level):
    races = {
        1: "humanoid",
        2: "dwarf",
        3: "gnome"
    }
    race = races.get(random.randrange(1,4,1))
    armors = {
        1: "medium",
        2: "heavy"
    }
    armor = armors.get(random.randrange(1,3,1))
    shields = {
        1: "light",
        2: "heavy",
        3: "tower"
    }
    weapons = {
        1: "halberd2H",
        2: "curved2H",
        3: "mace2H",
        4: "sword2H",
        5: "axe2H",
        6: "club2H",
        7: "sword",
        8: "longsword",
        9: "axe",
        10: "hammer",
        11: "curved",
        12: "mace"
    }
    
    shieldBool = random.randrange(0,2,1)
    if shieldBool == 0:
        weapon = weapons.get(random.randrange(1,13,1))
        shield = ""
    if shieldBool == 1:
        weapon = weapons.get(random.randrange(7,13,1))
        shield = shields.get(random.randrange(1,4,1))
    return WarriorNPC(level, "melee", race, armor, shield, weapon)
    
warriorR = randomMeleeWarrior(9)
warriorR.printSummary()
    