import math
from Classes.playerCharacter import PlayerCharacter


class ProtectionBonuses:
    ARMOR_MASTERWORK = 150
    ARMOR_BONUS_FACTOR = 1000
    SHIELD_BONUS_FACTOR = 1000
    NATURAL_ARMOR_BONUS_FACTOR = 2000
    DEFLECTION_BONUS_FACTOR = 2000
    LUCK_BONUS_FACTOR = 2500
    SAVE_RESISTANCE_BONUS_FACTOR = 1000

    armor = True
    natural = False
    deflection = False
    shield = False
    other = False
    save = False

    def getPrice(self, bonus, factor):
        return bonus * bonus * factor

    def getBonusTreshold(self, character):
        return math.floor(math.sqrt(character.level))

    def getMaxBonus(self, protectionBudget, threshold):
        maxBonus = 0
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            if self.getCostOfBonuses(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                     otherBonus) < protectionBudget:
                                totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus,
                                                                shieldBonus, otherBonus)
                                if totalBonus > maxBonus:
                                    maxBonus = totalBonus
        return maxBonus

    def getCostOfBonuses(self, armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus, otherBonus):
        if self.armor == True:
            armorBonusPrice = self.getPrice(armorBonus, self.ARMOR_BONUS_FACTOR) + self.ARMOR_MASTERWORK
        else:
            armorBonusPrice = 0

        if self.natural == True:
            naturalArmorBonusPrice = self.getPrice(naturalArmorBonus, self.NATURAL_ARMOR_BONUS_FACTOR)
        else:
            naturalArmorBonusPrice = 0

        if self.deflection == True:
            deflectionBonusPrice = self.getPrice(deflectionBonus, self.DEFLECTION_BONUS_FACTOR)
        else:
            deflectionBonusPrice = 0

        if self.shield == True:
            shieldBonusPrice = self.getPrice(shieldBonus, self.SHIELD_BONUS_FACTOR) + self.ARMOR_MASTERWORK
        else:
            shieldBonusPrice = 0

        if self.other == True:
            otherBonusPrice = self.getPrice(otherBonus, self.LUCK_BONUS_FACTOR)
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

    def getMaxSurplus(self, protectionBudget, threshold):
        maxSurplus = -1
        maxBonus = self.getMaxBonus(protectionBudget, threshold)
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            otherBonus)
                            if totalBonus == maxBonus:
                                surplus = protectionBudget - self.getCostOfBonuses(armorBonus,
                                                                                   naturalArmorBonus,
                                                                                   deflectionBonus,
                                                                                   shieldBonus,
                                                                                   otherBonus)
                                if surplus > maxSurplus:
                                    maxSurplus = surplus
        return maxSurplus

    def getResistanceBonus(self, character):
        if self.save == True:
            saveBonus = math.floor(math.sqrt(character.level))
            saveCost = self.getPrice(saveBonus, self.SAVE_RESISTANCE_BONUS_FACTOR)
            maxCost = character.getSaveBudget()
            if saveCost > maxCost:
                saveBonus = math.floor(math.sqrt(maxCost / self.SAVE_RESISTANCE_BONUS_FACTOR))
        else:
            saveBonus = 0
        return saveBonus

    def getOptimalBonusSet(self, character):
        saveResistanceBonus = self.getResistanceBonus(character)
        protectionBudget = character.getProtectionBudget() - self.getPrice(saveResistanceBonus,
                                                                           self.SAVE_RESISTANCE_BONUS_FACTOR)
        threshold = 6
        maxBonus = self.getMaxBonus(protectionBudget, threshold)
        maxSurplus = self.getMaxSurplus(protectionBudget, threshold)
        maxArmorBonus = 0
        maxNaturalArmorBonus = 0
        maxDeflectionBonus = 0
        maxShieldBonus = 0
        maxOtherBonus = 0
        for armorBonus in range(0, threshold, 1):
            for naturalArmorBonus in range(0, threshold, 1):
                for deflectionBonus in range(0, threshold, 1):
                    for shieldBonus in range(0, threshold, 1):
                        for otherBonus in range(0, threshold, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            otherBonus)
                            if totalBonus == maxBonus:
                                surplus = protectionBudget - self.getCostOfBonuses(armorBonus,
                                                                                   naturalArmorBonus,
                                                                                   deflectionBonus,
                                                                                   shieldBonus,
                                                                                   otherBonus)
                                if surplus == maxSurplus:
                                    if self.armor == True:
                                        maxArmorBonus = armorBonus
                                    if self.natural == True:
                                        maxNaturalArmorBonus = naturalArmorBonus
                                    if self.deflection == True:
                                        maxDeflectionBonus = deflectionBonus
                                    if self.shield == True:
                                        maxShieldBonus = shieldBonus
                                    if self.other == True:
                                        maxOtherBonus = otherBonus
        print("Bonus auf RK:   +{0:<2d}    Überschüssiges Gold: {1:<10d}".format(maxBonus, math.floor(maxSurplus)))
        print("Resistenzbonus: +{0:<2d}".format(saveResistanceBonus))
        print("Rüstungsbonus:  +{0:<2d}    Schildbonus: +{1:<2d}".format(maxArmorBonus, maxShieldBonus))
        print("Natürlicher RB: +{0:<2d}    Ablenkbonus: +{1:<2d}".format(maxNaturalArmorBonus, maxDeflectionBonus))
        print("Anderer Bonus:  +{0:<2d}".format(maxOtherBonus))

        optimalBonus = {
            "total": maxBonus,
            "armor": maxArmorBonus,
            "shield": maxShieldBonus,
            "natural": maxNaturalArmorBonus,
            "deflection": maxDeflectionBonus,
            "other": maxOtherBonus,
            "surplus": maxSurplus
        }
        return optimalBonus
