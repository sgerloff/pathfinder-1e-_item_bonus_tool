import sys

from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus
from Classes.attributeBonuses import AttributeBonuses

from Classes.playerCharacter import PlayerCharacter
from Classes.nonPlayerCharacter import NonPlayerCharacter

wb = WeaponBonus()
pb = ProtectionBonuses()
pb.armor = True
pb.shield = True
pb.save = True
pb.natural = True
pb.deflection = True
pb.other = True
ab = AttributeBonuses()
#

known_types = ["pc", "npc", "hnpc"]
level = -1
character = PlayerCharacter(1)

if len(sys.argv) < 3:
    print("Usage: {} <type = pc/npc/hnpc> <level = 1-20> <optional: 'asrndo'>".format(sys.argv[0]))
    print("Optional: a = armor, s = shield, r = cloak of resistance, n = amulet of natural armor, d = ring of protection, o = ring of luck/...")
    exit()
else:
    if sys.argv[1] in known_types:
        level = int(sys.argv[2])
        if level > 0 and level < 21:
            print("")
        else:
            print("Level out of range!")
            exit()
    else:
        print("Unknown type {} != pc, npc, hnpc".format(sys.argv[1]))
        exit()

if len(sys.argv) == 4:
    list_of_characters = list(sys.argv[3])
    if "a" in list_of_characters:
        pb.armor = True
    else:
        pb.armor = False
    if "s" in list_of_characters:
        pb.shield = True
    else:
        pb.shield = False
    if "r" in list_of_characters:
        pb.save = True
    else:
        pb.save = False
    if "n" in list_of_characters:
        pb.natural = True
    else:
        pb.natural = False
    if "d" in list_of_characters:
        pb.deflection = True
    else:
        pb.deflection = False
    if "o" in list_of_characters:
        pb.other = True
    else:
        pb.other = False

if sys.argv[1] == "pc":
    character = PlayerCharacter(level)
elif sys.argv[1] == "npc":
    character = NonPlayerCharacter(level)
    character.heroic = False
elif sys.argv[1] == "hnpc":
    character = NonPlayerCharacter(level)
    character.heroic = True

wb.setForCharacter(character)
wb.printOptimalBonus()
print("")
pb.setForCharacter(character)
pb.printOptimalBonusSet()
print("")
ab.setForCharacter(character)
ab.printOptimalBonus(character)

