import math


class PlayerCharacter:
    level = -1
    networth = -1

    WEAPON_RATIO = 0.25
    PROTECTION_RATIO = 0.5
    SAVE_RATIO = 0.25
    MAGIC_RATIO = 0.15

    _networthPerLevel = {
        1: 0,
        2: 1000,
        3: 3000,
        4: 6000,
        5: 10500,
        6: 16000,
        7: 23500,
        8: 33000,
        9: 46000,
        10: 62000,
        11: 82000,
        12: 108000,
        13: 140000,
        14: 185000,
        15: 240000,
        16: 315000,
        17: 410000,
        18: 530000,
        19: 685000,
        20: 880000
    }

    def __init__(self, level):
        self.setNetworthByLevel(level)

    def setNetworthByLevel(self, level):
        self.level = level
        self.networth = self._networthPerLevel.get(level, "Error: Invalid level (2-20)")

    def getAttributeBonus(self, attribute):
        return math.floor(attribute / 2) - 5

    def getProtectionBudget(self):
        return self.PROTECTION_RATIO * self.networth

    def getSaveBudget(self):
        return self.SAVE_RATIO * self.networth

    def getWeaponBudget(self):

        return self.WEAPON_RATIO * self.networth

    def getMagicBudget(self):
        return self.MAGIC_RATIO * self.networth
