import math
from Classes.protectionBonuses import ProtectionBonuses

networth = 46000

shield = True
luck = True

WEAPON_MASTERWORK = 300
WEAPON_RATIO = 0.25
WEAPON_BONUS_FACTOR = 2000

ARMOR_MASTERWORK = 150
PROTECTION_RATIO = 0.5
ARMOR_BONUS_FACTOR = 1000
SHIELD_BONUS_FACTOR = 1000
NATURAL_ARMOR_BONUS_FACTOR = 2000
DEFLECTION_BONUS_FACTOR = 2000
LUCK_BONUS_FACTOR = 2500

# Waffenbonus
weaponShare = WEAPON_RATIO * networth

weaponBonus = math.floor(math.sqrt((weaponShare - WEAPON_MASTERWORK) / WEAPON_BONUS_FACTOR))

weaponSurplus = math.floor(weaponShare - WEAPON_MASTERWORK - weaponBonus * weaponBonus * WEAPON_BONUS_FACTOR)

print("Waffenbonus: +{0:<2d}    Überschüssiges Gold: {1:<10d}".format(weaponBonus, weaponSurplus))

# Rüstung, Schild und anderer Schutzbonus

pb = ProtectionBonuses()

pb.armor = True
pb.natural = True
pb.deflection = True
pb.shield = True

print(pb.getMaxBonus(networth))
print(pb.getMaxSurplus(networth))
pb.getOptimalBonusSet( networth )
