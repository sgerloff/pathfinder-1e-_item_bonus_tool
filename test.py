import math

networth = 46000

shield = True
luck = True

WEAPON_MASTERWORK = 300
WEAPON_RATIO = 0.25
WEAPON_BONUS_FACTOR = 2000

ARMOR_MASTERWORK = 150
PROTECTION_RATIO = 0.5
ARMOR_BONUS_FACTOR = 1000
SHIELD_BONUS_FACTOR = 1000
NATURAL_ARMOR_BONUS_FACTOR = 2000
DEFLECTION_BONUS_FACTOR = 2000
LUCK_BONUS_FACTOR = 2500



#Waffenbonus
weaponShare = WEAPON_RATIO * networth

weaponBonus = math.floor( math.sqrt( ( weaponShare - WEAPON_MASTERWORK ) / WEAPON_BONUS_FACTOR ) )

weaponSurplus = math.floor( weaponShare - WEAPON_MASTERWORK - weaponBonus * weaponBonus * WEAPON_BONUS_FACTOR )

print( "Waffenbonus: +{0:<2d}    Überschüssiges Gold: {1:<10d}".format( weaponBonus, weaponSurplus ) )

#Rüstung, Schild und anderer Schutzbonus		
class ProtectionBonuses:
	ARMOR_MASTERWORK = 150
	PROTECTION_RATIO = 0.5
	ARMOR_BONUS_FACTOR = 1000
	SHIELD_BONUS_FACTOR = 1000
	NATURAL_ARMOR_BONUS_FACTOR = 2000
	DEFLECTION_BONUS_FACTOR = 2000
	LUCK_BONUS_FACTOR = 2500
	
	shield = True
	luck = True
	
	def getPrice(self, bonus, factor):
		return bonus * bonus * factor
	
	def getMaxBonus( self, networth ):
		maxBonus = -1
		maxSurplus = -1
		luckBonusPrice = 0
		shieldBonusPrice = 0
		
		for armorBonus in range( 0, 5, 1 ):
			armorBonusPrice = self.getPrice( armorBonus, ARMOR_BONUS_FACTOR ) + ARMOR_MASTERWORK
			
			for naturalArmorBonus in range ( 0, 5, 1 ):
				naturalArmorBonusPrice = self.getPrice( naturalArmorBonus, NATURAL_ARMOR_BONUS_FACTOR )
				
				for deflectionBonus in range (0,5,1):
					deflectionBonusPrice = self.getPrice( deflectionBonus, DEFLECTION_BONUS_FACTOR )
					
					if shield == True:
						for shieldBonus in range( 0, 5, 1 ):
							shieldBonusPrice = self.getPrice( shieldBonus, SHIELD_BONUS_FACTOR ) + ARMOR_MASTERWORK
							
							if luck == True:
								for luckBonus in range( 0, 5, 1 ):
									luckBonusPrice = self.getPrice( luckBonus, LUCK_BONUS_FACTOR)
					
					
					totalPrice = armorBonusPrice + naturalArmorBonusPrice + deflectionBonusPrice + luckBonusPrice + shieldBonusPrice
					if totalPrice < 0.5*networth:
						totalBonus = armorBonus + naturalArmorBonus + deflectionBonus
						if totalBonus >= maxBonus:
							maxBonus = totalBonus
							
		return maxBonus

	
pb = ProtectionBonuses()
print(pb.getMaxBonus(networth))
	