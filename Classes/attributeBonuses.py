from Classes.playerCharacter import PlayerCharacter
import math

class AttributeBonuses:
    ATTRIBUTE_BONUS_FACTOR = 1000

    def getPrice(self, bonus, factor):
        return bonus*bonus*factor

    def getOptimalBonusSet(self, character):
        magicBudget = character.getMagicBudget()
        maxBonus = 2*math.floor(math.sqrt(magicBudget /(4* self.ATTRIBUTE_BONUS_FACTOR)))
        surplus = magicBudget - self.getPrice(maxBonus,self.ATTRIBUTE_BONUS_FACTOR)
        print("Attributbonus:  +{0:<2d}    Überschüssiges Gold: +{1:<2d}".format(maxBonus, math.floor(surplus)))
