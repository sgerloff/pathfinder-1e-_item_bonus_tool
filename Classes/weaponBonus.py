import math
from Classes.playerCharacter import PlayerCharacter


class WeaponBonus:
    __WEAPON_MASTERWORK = 300
    __WEAPON_BONUS_FACTOR = 2000

    maxBonus = 0
    maxSurplus = 0

    def __init__(self):
        self.__reset__()

    def __reset__(self):
        self.maxBonus = 0
        self.maxSurplus = 0

    def setForCharacter(self, character):
        self.__reset__()
        self._setMaxBonus(character)
        self._setMaxSurplus(character)

    def _setMaxBonus(self, character):
        self.__reset__()
        weaponBudget = character.getWeaponBudget()
        if weaponBudget > self.__WEAPON_MASTERWORK:
            weaponBudget = self._getWeaponBudget(character)
            self.maxBonus = math.floor(math.sqrt(weaponBudget / self.__WEAPON_BONUS_FACTOR))
        else:
            self.maxBonus = 0

    def _setMaxSurplus(self, character):
        weaponBudget = self._getWeaponBudget(character)
        self.maxSurplus = math.floor(weaponBudget - self.maxBonus * self.maxBonus * self.__WEAPON_BONUS_FACTOR)

    def _getWeaponBudget(self, character):
        budget = character.getWeaponBudget() - self.__WEAPON_MASTERWORK
        if budget > 0:
            return character.getWeaponBudget() - self.__WEAPON_MASTERWORK
        else:
            return character.getWeaponBudget()

    def printOptimalBonus(self):
        print("Magic Weapon +{0:<2d}    Surplus: {1:}gp".format(self.maxBonus, self.maxSurplus))
