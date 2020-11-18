import math
from Classes.playerCharacter import PlayerCharacter


class ProtectionBonuses:
    __ARMOR_MASTERWORK = 150
    __ARMOR_BONUS_FACTOR = 1000
    __SHIELD_BONUS_FACTOR = 1000
    __NATURAL_ARMOR_BONUS_FACTOR = 2000
    __DEFLECTION_BONUS_FACTOR = 2000
    __LUCK_BONUS_FACTOR = 2500
    __SAVE_RESISTANCE_BONUS_FACTOR = 1000

    armor = False
    natural = False
    deflection = False
    shield = False
    other = False
    save = False

    saveBonus = 0
    maxBonus = 0
    maxSurplus = 0
    maxArmorBonus = 0
    maxShieldBonus = 0
    maxNaturalArmorBonus = 0
    maxDeflectionBonus = 0
    maxOtherBonus = 0

    def __init__(self):
        self.__reset__()

    def __reset__(self):
        self.saveBonus = 0
        self.maxBonus = 0
        self.maxSurplus = 0
        self.maxArmorBonus = 0
        self.maxShieldBonus = 0
        self.maxNaturalArmorBonus = 0
        self.maxDeflectionBonus = 0
        self.maxOtherBonus = 0

    def setForCharacter(self, character):
        self.__reset__()
        self._setResistanceBonus(character)
        protectionBudget = character.getProtectionBudget() - self.getPrice(self.saveBonus,
                                                                           self.__SAVE_RESISTANCE_BONUS_FACTOR)
        threshold = 6
        self._setMaxBonus(protectionBudget, threshold)
        self._setMaxSurplus(protectionBudget, threshold)
        self._setOptimalBonusSet(protectionBudget, threshold)

    def _setResistanceBonus(self, character):
        if self.save:
            self.saveBonus = math.floor(math.sqrt(character.level))
            saveCost = self.getPrice(self.saveBonus, self.__SAVE_RESISTANCE_BONUS_FACTOR)
            maxCost = character.getSaveBudget()
            if saveCost > maxCost:
                self.saveBonus = math.floor(math.sqrt(maxCost / self.__SAVE_RESISTANCE_BONUS_FACTOR))
        else:
            self.saveBonus = 0

    def getPrice(self, bonus, factor):
        return bonus * bonus * factor

    def getBonusTreshold(self, character):
        return math.floor(math.sqrt(character.level))

    def _setMaxBonus(self, protectionBudget, threshold):
        self.maxBonus = 0
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            if self.getCostOfBonuses(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                     otherBonus) < protectionBudget:
                                totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus,
                                                                shieldBonus, otherBonus)
                                if totalBonus > self.maxBonus:
                                    self.maxBonus = totalBonus

    def getCostOfBonuses(self, armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus, otherBonus):
        if self.armor:
            armorBonusPrice = self.getPrice(armorBonus, self.__ARMOR_BONUS_FACTOR) + self.__ARMOR_MASTERWORK
        else:
            armorBonusPrice = 0

        if self.natural:
            naturalArmorBonusPrice = self.getPrice(naturalArmorBonus, self.__NATURAL_ARMOR_BONUS_FACTOR)
        else:
            naturalArmorBonusPrice = 0

        if self.deflection:
            deflectionBonusPrice = self.getPrice(deflectionBonus, self.__DEFLECTION_BONUS_FACTOR)
        else:
            deflectionBonusPrice = 0

        if self.shield:
            shieldBonusPrice = self.getPrice(shieldBonus, self.__SHIELD_BONUS_FACTOR) + self.__ARMOR_MASTERWORK
        else:
            shieldBonusPrice = 0

        if self.other:
            otherBonusPrice = self.getPrice(otherBonus, self.__LUCK_BONUS_FACTOR)
        else:
            otherBonusPrice = 0

        return armorBonusPrice + naturalArmorBonusPrice + deflectionBonusPrice + shieldBonusPrice + otherBonusPrice

    def getTotalBonus(self, armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus, otherBonus):
        if self.armor == False:
            armorBonus = 0
        if self.natural == False:
            naturalArmorBonus = 0
        if self.deflection == False:
            deflectionBonus = 0
        if self.shield == False:
            shieldBonus = 0
        if self.other == False:
            otherBonus = 0

        return armorBonus + naturalArmorBonus + deflectionBonus + shieldBonus + otherBonus

    def _setMaxSurplus(self, protectionBudget, threshold):
        self.maxSurplus = 0
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            otherBonus)
                            if totalBonus == self.maxBonus:
                                surplus = protectionBudget - self.getCostOfBonuses(armorBonus,
                                                                                   naturalArmorBonus,
                                                                                   deflectionBonus,
                                                                                   shieldBonus,
                                                                                   otherBonus)
                                if surplus > self.maxSurplus:
                                    self.maxSurplus = surplus

    def _setOptimalBonusSet(self, protectionBudget, threshold):
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            otherBonus)
                            if totalBonus == self.maxBonus:
                                surplus = protectionBudget - self.getCostOfBonuses(armorBonus,
                                                                                   naturalArmorBonus,
                                                                                   deflectionBonus,
                                                                                   shieldBonus,
                                                                                   otherBonus)
                                if surplus == self.maxSurplus:
                                    if self.armor:
                                        self.maxArmorBonus = armorBonus
                                    if self.natural:
                                        self.maxNaturalArmorBonus = naturalArmorBonus
                                    if self.deflection:
                                        self.maxDeflectionBonus = deflectionBonus
                                    if self.shield:
                                        self.maxShieldBonus = shieldBonus
                                    if self.other:
                                        self.maxOtherBonus = otherBonus

    def printOptimalBonusSet(self):
        print("AC Bonus:   +{0:<2d}    Surplus: {1:}gp".format(self.maxBonus,
                                                                                 math.floor(self.maxSurplus)))
        print("Cloak of Resistance +{0:<2d}".format(self.saveBonus))
        print("Magic Armor +{0:<2d}    Magic Shield +{1:<2d}".format(self.maxArmorBonus, self.maxShieldBonus))
        print("Amulet of Natural Armor +{0:<2d}    Ring of Protection +{1:<2d}".format(self.maxNaturalArmorBonus,
                                                                         self.maxDeflectionBonus))
        print("Ring of Luck +{0:<2d}".format(self.maxOtherBonus))
