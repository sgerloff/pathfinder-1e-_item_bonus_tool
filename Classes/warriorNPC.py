import math
import random
from Classes.nonPlayerCharacter import NonPlayerCharacter
from Classes.attributeBonuses import AttributeBonuses
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus


class WarriorNPC(NonPlayerCharacter):
    __hitDice = 10
    
    type = "melee"
    race = "humanoid"

    armorType = "medium"
    shieldType = "heavy"

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

    def __init__(self):
        self.type = "melee"
        self.race = "humanoid"
        self.armorType = "medium"
        self.shieldType = "heavy"

    def __init__(self, level, type, race, armorType, shieldType):
        self.setLevel(level)
        self.type = type
        self.race = race
        self.armorType = armorType
        self.shieldType = shieldType
        if self.shieldType != "":
            self._protectionBonus.shield = True

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
        if self.race == "humanoid":
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
        return math.floor(self.level / 3.) + self.getAttributeBonus(self.getWisdom()) + self._protectionBonus.saveBonus

    def getReflexSave(self):
        return math.floor(self.level / 3.) + self.getAttributeBonus(self.getDexterity) + self._protectionBonus.saveBonus

    def getFortitudeSave(self):
        return math.floor(self.level / 2) + 2 + self.getAttributeBonus(
            self.getConstitution()) + self._protectionBonus.saveBonus

    def getBaseAttackBonus(self):
        return self.level

    def getMeleeAttackBonus(self):
        return self.getAttributeBonus(self.getStrength()) + self._weaponBonus.maxBonus

    def getRangeAttackBonus(self):
        return self.getAttributeBonus(self.getDexterity()) + self._weaponBonus.maxBonus

    def getArmorClass(self):
        self._protectionBonus.deflection = True
        self._protectionBonus.natural = True

        armorClass = 10

        if self.armorType == "medium":
            armorClass += 5
        if self.shieldType == "heavy":
            armorClass += +2
            self._protectionBonus.shield = True
        armorClass += self._protectionBonus.maxArmorBonus

        armorClass += self.getAttributeBonus(self.getDexterity())

        return armorClass
        
    def getInitiativeBonus(self):
        return self.getAttributeBonus(self.getDexterity())
    
    def getRandomHitPoints(self):
        hitPoints=0
        for i in range(0,self.level,1):
            hitPoints += random.randrange(1,self.__hitDice,1)
        return hitPoints + self.getAttributeBonus(self.getConstitution())
        
    def getMeanHitPoints(self):
        return round((0.5*(self.__hitDice+1) + self.getAttributeBonus(self.getConstitution()) )*self.level)
    
    def getStandardDeviationHitPoints(self):
        return math.floor(math.sqrt(1.5*self.getMeanHitPoints()))
                
    def printSummary(self):
        print( "Warrior: {0:<15s}, Armor: {1:<10s}, Shield: {2:<10s}".format(self.type+" "+self.race, self.armorType, self.shieldType) )
        print( "HP: {0:>4d}±{1:<3d}, Initiative: {2:<2d}".format(self.getMeanHitPoints(),self.getStandardDeviationHitPoints() , self.getInitiativeBonus()) )
        print("AC: {0:<2d}".format(self.getArmorClass()))
        