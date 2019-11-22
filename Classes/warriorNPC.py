import math
import random
from Classes.nonPlayerCharacter import NonPlayerCharacter
from Classes.attributeBonuses import AttributeBonuses
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus

import math
from Classes.nonPlayerCharacter import NonPlayerCharacter
from Classes.attributeBonuses import AttributeBonuses
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus


class WarriorNPC(NonPlayerCharacter):
    __hitDice = 10

    type = "melee"
    race = "human"

    size = "normal"

    armorType = "medium"
    shieldType = "heavy"
    weaponType = "sword"

    _attributeBonus = AttributeBonuses()
    _protectionBonus = ProtectionBonuses()
    _weaponBonus = WeaponBonus()

    _baseStrength = {
        "melee": 13,
        "range": 11
    }

    _baseDexterity = {
        "melee": 11,
        "range": 13
    }

    _baseConstitution = {
        "melee": 12,
        "range": 12
    }

    _baseIntelligence = {
        "melee": 9,
        "range": 10
    }

    _baseWisdom = {
        "melee": 10,
        "range": 9
    }

    _baseCharisma = {
        "melee": 8,
        "range": 8
    }

    _damageDice = {
        "sword": "1D6 19-20/x2",
        "longsword": "1D8 19-20/x2",
        "axe": "1D8 x3",
        "hammer": "1D8 x3",
        "curved": "1D6 18-20/x2",
        "mace": "1D8 x2",
        "halberd2H": "1D10 x3",
        "curved2H": "2D4 18-20/x2",
        "mace2H": "1D10 19-20/x2",
        "sword2H": "2D6 19-20/x2",
        "axe2H": "1D12 x3",
        "club2H": "1D10 x2",
        "bow": "1W6 x3",
        "longbow": "1W8 x3",
        "crossbow": "1W8 19-20/x2",
        "heavycrossbow": "1W10 19-20/x2"
    }

    def __init__(self, level, type, race, armorType, shieldType, weaponType):
        self.setLevel(level)
        self.type = type
        self.race = race
        self._setSize()
        self.armorType = armorType
        self.shieldType = shieldType
        if self.shieldType != "":
            self._protectionBonus.shield = True
        self.weaponType = weaponType

    def _setSize(self):
        if self.race == "gnome":
            self.size = "small"
        if self.race == "halfling":
            self.size = "small"

    def setLevel(self, level):
        self.level = level

        self._protectionBonus.armor = True
        self._protectionBonus.natural = True
        self._protectionBonus.deflection = True
        self._protectionBonus.other = False
        self._protectionBonus.save = True

        self._protectionBonus.setForCharacter(self)
        self._weaponBonus.setForCharacter(self)
        self._attributeBonus.setForCharacter(self)

    def addFavoriteAttributeBonus(self):
        bonus = math.floor(self.level / 4.)
        bonus += self._attributeBonus.maxBonus
        if self.race == "human" or self.race == "halforc" or self.race == "halfelf":
            bonus += 2
        return bonus

    def getStrength(self):
        strength = self._baseStrength.get(self.type)
        if self.race == "gnome":
            strength -= 2
        if self.race == "halfling":
            strength -= 2
        if self.type == "melee":
            strength += self.addFavoriteAttributeBonus()
        if self.heroic:
            strength += 2
        return strength

    def getDexterity(self):
        dexterity = self._baseDexterity.get(self.type)
        if self.race == "elvish":
            dexterity += 2
        if self.race == "halfling":
            dexterity += 2
        if self.type == "range":
            dexterity += self.addFavoriteAttributeBonus()
        if self.heroic:
            dexterity += 2
        return dexterity

    def getConstitution(self):
        constitution = self._baseConstitution.get(self.type)
        if self.heroic:
            constitution += 2
        if self.race == "dwarf":
            constitution += 2
        if self.race == "elvish":
            constitution -= 2
        if self.race == "gnome":
            constitution += 2
        return constitution

    def getIntelligence(self):
        intelligence = self._baseIntelligence.get(self.type)
        if self.race == "elvish":
            intelligence += 2
        if self.race == "halfling":
            intelligence += 2
        if self.heroic:
            if self.type == "melee":
                intelligence += 1
            if self.type == "range":
                intelligence += 2
        return intelligence

    def getWisdom(self):
        wisdom = self._baseWisdom.get(self.type)
        if self.race == "dwarf":
            wisdom += 2
        if self.heroic:
            if self.type == "melee":
                wisdom += 2
            if self.type == "range":
                wisdom += 1
        return wisdom

    def getCharisma(self):
        charisma = self._baseCharisma.get(self.type)
        if self.race == "dwarf":
            charisma -= 2
        if self.race == "gnome":
            charisma += 2
        if self.heroic:
            charisma += 0
        return charisma

    def getWillSave(self):
        raceBonus = 0
        if self.race == "halfling":
            raceBonus += 1
        return math.floor(self.level / 3.) + self.getAttributeBonus(
            self.getWisdom()) + self._protectionBonus.saveBonus + raceBonus

    def getReflexSave(self):
        raceBonus = 0
        if self.race == "halfling":
            raceBonus += 1
        return math.floor(self.level / 3.) + self.getAttributeBonus(
            self.getDexterity()) + self._protectionBonus.saveBonus + raceBonus

    def getFortitudeSave(self):
        raceBonus = 0
        if self.race == "halfling":
            raceBonus += 1
        return math.floor(self.level / 2) + 2 + self.getAttributeBonus(
            self.getConstitution()) + self._protectionBonus.saveBonus + raceBonus

    def getBaseAttackBonus(self):
        return self.level

    def getMeleeAttackBonus(self):
        sizeBonus = 0
        if self.size == "small":
            sizeBonus = 1
        return self.getAttributeBonus(self.getStrength()) + self._weaponBonus.maxBonus + sizeBonus

    def getRangeAttackBonus(self):
        sizeBonus = 0
        if self.size == "small":
            sizeBonus = 1
        return self.getAttributeBonus(self.getDexterity()) + self._weaponBonus.maxBonus + sizeBonus

    def getArmorClass(self):

        armorClass = 10

        if self.armorType == "light":
            armorClass += 2
        if self.armorType == "medium":
            armorClass += 5
        if self.armorType == "heavy":
            armorClass += 7

        if self.shieldType == "light":
            armorClass += 1
        if self.shieldType == "heavy":
            armorClass += 2
        if self.shieldType == "tower":
            armorClass += 4

        if self.size == "small":
            armorClass += 1

        armorClass += self._protectionBonus.maxBonus

        armorClass += self.getAttributeBonus(self.getDexterity())

        return armorClass

    def getTouchArmorClass(self):
        armorClass = 10
        armorClass += self._protectionBonus.maxDeflectionBonus
        armorClass += self._protectionBonus.maxOtherBonus
        armorClass += self.getAttributeBonus(self.getDexterity())
        if self.size == "small":
            armorClass += 1
        return armorClass

    def getFlatArmorClass(self):
        armorClass = self.getArmorClass()
        armorClass -= self.getAttributeBonus(self.getDexterity())
        return armorClass

    def getInitiativeBonus(self):
        return self.getAttributeBonus(self.getDexterity())

    def getRandomHitPoints(self):
        hitPoints = 0
        for i in range(0, self.level, 1):
            hitPoints += random.randrange(1, self.__hitDice, 1)
        return hitPoints + self.getAttributeBonus(self.getConstitution())

    def getMeanHitPoints(self):
        return round((0.5 * (self.__hitDice + 1) + self.getAttributeBonus(self.getConstitution())) * self.level)

    def getStandardDeviationHitPoints(self):
        return math.floor(math.sqrt(1.5 * self.getMeanHitPoints()))

    def getCombatManeuverBonus(self):
        sizeBonus = 0
        if self.size == "small":
            sizeBonus = -1
        return self.getBaseAttackBonus() + self.getAttributeBonus(self.getStrength()) + sizeBonus

    def getCombatManeuverDefense(self):
        sizeBonus = 0
        if self.size == "small":
            sizeBonus = -1
        return 10 + self.getBaseAttackBonus() + self.getAttributeBonus(self.getStrength()) + self.getAttributeBonus(
            self.getDexterity()) + sizeBonus

    def getMovementSpeed(self):
        speed = 6
        if self.size == "small":
            speed = 4

        if self.armorType == "medium":
            speed -= math.floor(speed / 3)
        if self.armorType == "heavy":
            speed -= math.floor(speed / 3)

        if self.race == "dwarf":
            speed = 4
        return speed

    def printSummary(self):
        print("Warrior: {0:<15s}, Armor: {1:<10s}, Shield: {2:<10s}".format(self.type + " " + self.race, self.armorType,
                                                                            self.shieldType))
        print("HP: {0:>4d}±{1:<3d}, Init: {2:<2d}, Speed: {3:>2d}F".format(self.getMeanHitPoints(),
                                                                           self.getStandardDeviationHitPoints(),
                                                                           self.getInitiativeBonus(),
                                                                           self.getMovementSpeed()))
        print("AC: {0:<2d}, Touch: {1:<2d}, Flat: {2:<2d}".format(self.getArmorClass(), self.getTouchArmorClass(),
                                                                  self.getFlatArmorClass()))
        print("Ref.: {0:<2d}, Will: {1:<2d}, Fort.: {2:<d}".format(self.getReflexSave(), self.getWillSave(),
                                                                   self.getFortitudeSave()))
        print("CMB: {0:<2d}, CMD: {1:<2d}".format(self.getCombatManeuverBonus(), self.getCombatManeuverDefense()))

        firstAttack = self.getBaseAttackBonus()
        if self.type == "melee":
            firstAttack += self.getMeleeAttackBonus()
        if self.type == "range":
            firstAttack += self.getRangeAttackBonus()
        secondAttack = 0
        thirdAttack = 0
        fourthAttack = 0
        if self.getBaseAttackBonus() > 5:
            secondAttack = firstAttack - 5
        if self.getBaseAttackBonus() > 10:
            thirdAttack = firstAttack - 10
        if self.getBaseAttackBonus() > 15:
            fourthAttack = firstAttack - 15

        damageBonus = self._weaponBonus.maxBonus
        if self.type == "melee":
            damageBonus += self.getAttributeBonus(self.getStrength())
            if self.weaponType.endswith("2H"):
                damageBonus += math.floor(0.5 * self.getAttributeBonus(self.getStrength()))

        print("AB: +{0:<2d}/ +{1:<2d}/ +{2:<2d}/ +{3:<2d}, {4:s}: {5:d}+{6:s}".format(firstAttack, secondAttack,
                                                                                      thirdAttack, fourthAttack,
                                                                                      self.weaponType, damageBonus,
                                                                                      self._damageDice.get(
                                                                                          self.weaponType)))
