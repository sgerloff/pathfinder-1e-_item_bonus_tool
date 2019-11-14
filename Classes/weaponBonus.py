import math
from Classes.playerCharacter import PlayerCharacter


class WeaponBonus:
    WEAPON_MASTERWORK = 300
    WEAPON_BONUS_FACTOR = 2000

    def getMaxWeaponBonus(self, character):
        weaponBudget = character.getWeaponBudget()
        if weaponBudget > self.WEAPON_MASTERWORK:
            weaponBudget = character.getWeaponBudget() - self.WEAPON_MASTERWORK
            return math.floor(math.sqrt(weaponBudget / self.WEAPON_BONUS_FACTOR))
        else:
            return 0

    def getMaxSurplus(self, character):
        weaponBudget = character.getWeaponBudget() - self.WEAPON_MASTERWORK
        weaponBonus = self.getMaxWeaponBonus(character)
        return math.floor(weaponBudget - weaponBonus * weaponBonus * self.WEAPON_BONUS_FACTOR)

    def getOptimalBonus(self, character):
        maxBonus = self.getMaxWeaponBonus(character)
        maxSurplus = self.getMaxSurplus(character)
        print("Waffenbonus:    +{0:<2d}    Überschüssiges Gold: {1:<10d}".format(maxBonus, maxSurplus))
