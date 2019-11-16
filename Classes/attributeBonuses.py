from Classes.playerCharacter import PlayerCharacter
import math


class AttributeBonuses:
    __ATTRIBUTE_BONUS_FACTOR = 1000

    maxBonus = 0
    maxSurplus = 0

    def __init__(self):
       self.__reset__()

    def __reset__(self):
        self.maxBonus = 0
        self.maxSurplus = 0

    def setForCharacter(self, character):
        self._setMaxBonus(character)

    def getPrice(self, bonus, factor):
        return bonus * bonus * factor

    def _setMaxBonus(self, character):
        self.maxBonus = 2 * math.floor(math.sqrt(character.getMagicBudget() / (4 * self.__ATTRIBUTE_BONUS_FACTOR)))
    
    def _setMaxSurplus(self, character):
        self.maxSurplus = character.getMagicBudget() - self.getPrice(self.maxBonus, self.__ATTRIBUTE_BONUS_FACTOR)

    def printOptimalBonus(self, character):
        print("Attributbonus:  +{0:<2d}    Überschüssiges Gold: +{1:<2d}".format(self.maxBonus, math.floor(self.maxSurplus)))
