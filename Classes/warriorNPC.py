import math
from Classes.nonPlayerCharacter import NonPlayerCharacter
from Classes.attributeBonuses import AttributeBonuses
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus

class WarriorNPC(NonPlayerCharacter):
    
    type="melee"
    race="humanoid"
    
    armorType="medium"
    shieldType="heavy"
    
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
    
    def getStrength(self):
        strength = self._baseStrength.get(self.type)
        if self.race == "gnome":
            strength -= 2
        if self.race == "halfling":
            strength -= 2
        if self.type == "melee":
            strength += math.floor(self.level/4.)
            strength += self._attributeBonus.getMaxBonus(self)
            if self.race == "humanoid":
                strength += 2
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
            dexterity += math.floor(self.level/4.)
            dexterity += self._attributeBonus.getMaxBonus(self)
            if self.race == "humanoid":
                dexterity += 2
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
        return math.floor(self.level/3.) + self.getAttributeBonus(self.getWisdom()) + self.getResistanceBonus()
    
    def getReflexSave(self):
        return math.floor(self.level/3.) + self.getAttributeBonus(self.getDexterity) + self.getResistanceBonus()
        
    def getFortitudeSave(self):
        return math.floor(self.level/2)+2 + self.getAttributeBonus(self.getConstitution()) + self.getResistanceBonus()
   
    def getResistanceBonus(self):
        self._protectionBonus.save = True
        return self._protectionBonus.getResistanceBonus(self)
        
    def getBaseAttackBonus(self):
        return self.level
        
    def getMeleeAttackBonus(self):
        return self.getAttributeBonus(self.getStrength()) + self._weaponBonus.getMaxWeaponBonus(self)
        
    def getRangeAttackBonus(self):
        return self.getAttributeBonus(self.getDexterity()) + self._weaponBonus.getMaxWeaponBonus(self)
        
    def getArmorClass(self):
        self._protectionBonus.deflection = True
        self._protectionBonus.natural = True
        
        armorClass = 10
        
        if self.armorType == "medium":
            armorClass += 5
        if self.shieldType == "heavy":
            armorClass += +2
            self._protectionBonus.shield = True
        optimalBonus = self._protectionBonus.getOptimalBonusSet(self)
        armorClass += optimalBonus.get("total")
        
        armorClass += self.getAttributeBonus(self.getDexterity())
        
        return armorClass
    
        