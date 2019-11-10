import math
from Classes.playerCharacter import PlayerCharacter


class NonPlayerCharacter(PlayerCharacter):
    heroic = False
    _networthPerLevel = {
        1: 260,
        2: 390,
        3: 780,
        4: 1650,
        5: 2400,
        6: 3450,
        7: 6000,
        8: 7800,
        9: 10500,
        10: 12750,
        11: 16350,
        12: 16350,
        13: 21000,
        14: 27000,
        15: 34000,
        16: 45000,
        17: 58500,
        18: 75000,
        19: 96000,
        20: 123000,
        21: 159000
    }

    _weaponBudgetPerLevel = {
        1: 50,
        2: 100,
        3: 350,
        4: 650,
        5: 900,
        6: 1400,
        7: 2350,
        8: 2700,
        9: 3000,
        10: 3500,
        11: 4000,
        12: 6000,
        13: 8500,
        14: 9000,
        15: 12000,
        16: 17000,
        17: 19000,
        18: 24000,
        19: 30000,
        20: 40000,
        21: 55000
    }

    _protectionBudgetPerLevel = {
        1: 130,
        2: 150,
        3: 200,
        4: 800,
        5: 1000,
        6: 1400,
        7: 1650,
        8: 2000,
        9: 2500,
        10: 3000,
        11: 4000,
        12: 4500,
        13: 5500,
        14: 8000,
        15: 10500,
        16: 13500,
        17: 18000,
        18: 23000,
        19: 28000,
        20: 35000,
        21: 40000
    }

    _magicBudgetPerLevel = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 500,
        9: 1000,
        10: 2000,
        11: 3000,
        12: 4000,
        13: 5000,
        14: 7000,
        15: 9000,
        16: 11000,
        17: 16000,
        18: 20000,
        19: 28000,
        20: 35000,
        21: 44000
    }

    def getEffectiveLevel(self):
        effectiveLevel = self.level
        if self.heroic == True:
            effectiveLevel += 1
        return effectiveLevel

    def getProtectionBudget(self):
        return self._protectionBudgetPerLevel.get(self.level)

    def getSaveBudget(self):
        return math.floor(self._protectionBudgetPerLevel.get(self.level) / 3.)

    def getWeaponBudget(self):
        return self._weaponBudgetPerLevel.get(self.level)

    def getMagicBudget(self):
        return self._magicBudgetPerLevel.get(self.level)