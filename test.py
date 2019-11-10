import math
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

print("PC:")
pc = PlayerCharacter(9)
wb.getOptimalBonus(pc)
pb.getOptimalBonusSet(pc)
ab.getOptimalBonusSet(pc)

# print("NPC:")
# npc = NonPlayerCharacter(9)
# npc.heroic = True
# wb.getOptimalBonus(npc)
# pb.getOptimalBonusSet(npc)