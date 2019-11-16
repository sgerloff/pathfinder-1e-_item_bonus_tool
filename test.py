import math
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus
from Classes.attributeBonuses import AttributeBonuses

from Classes.playerCharacter import PlayerCharacter
from Classes.nonPlayerCharacter import NonPlayerCharacter

from Classes.warriorNPC import WarriorNPC

# wb = WeaponBonus()
pb = ProtectionBonuses()
pb.armor = True
pb.shield = True
pb.save = True
pb.natural = True
pb.deflection = True
pb.other = True
# ab = AttributeBonuses()
#
print("PC:")
pc = PlayerCharacter(9)
# wb.getOptimalBonus(pc)
# print("")
pb.setMaxBoni(pc)
pb.printOptimalBonusSet()
print("")
# ab.getOptimalBonusSet(pc)
#
# print("\n\nNPC:")
# npc = NonPlayerCharacter(13)
# npc.heroic = True
# wb.getOptimalBonus(npc)
# print("")
# pb.getOptimalBonusSet(npc)
# print("")
# ab.getOptimalBonusSet(npc)

# NPC Classes
warrior = WarriorNPC(1, "melee", "dwarf", "medium", "heavy")
# pb.getOptimalBonusSet(warrior)
warrior.heroic = True
print(warrior.getFortitudeSave())
print(warrior.getStrength())
print(warrior.getMeleeAttackBonus())
print(warrior.getArmorClass())
