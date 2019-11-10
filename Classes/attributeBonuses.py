from Classes.playerCharacter import PlayerCharacter
import math

class AttributeBonuses:
    ATTRIBUTE_BONUS_FACTOR = 1000

    def getOptimalBonusSet(self, character):
        magicBudget = character.getMagicBudget()
        print("Attribute Bonus: +{0:<2d}".format(math.floor(math.sqrt(magicBudget / self.ATTRIBUTE_BONUS_FACTOR))))
