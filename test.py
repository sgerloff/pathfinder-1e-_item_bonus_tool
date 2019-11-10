import math
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus

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

print("PC:")
pc = PlayerCharacter(9)
wb.getOptimalBonus(pc)
pb.getOptimalBonusSet(pc)

print("NPC:")
npc = NonPlayerCharacter(9)
wb.getOptimalBonus(npc)
pb.getOptimalBonusSet(npc)
