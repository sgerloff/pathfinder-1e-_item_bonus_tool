class ProtectionBonuses:
    ARMOR_MASTERWORK = 150
    PROTECTION_RATIO = 0.5
    ARMOR_BONUS_FACTOR = 1000
    SHIELD_BONUS_FACTOR = 1000
    NATURAL_ARMOR_BONUS_FACTOR = 2000
    DEFLECTION_BONUS_FACTOR = 2000
    LUCK_BONUS_FACTOR = 2500

    armor = True
    natural = False
    deflection = False
    shield = False
    luck = False

    def getPrice(self, bonus, factor):
        return bonus * bonus * factor

    def getMaxBonus(self, networth):
        maxBonus = -1
        for armorBonus in range(0, 5, 1):
            for naturalArmorBonus in range(0, 5, 1):
                for deflectionBonus in range(0, 5, 1):
                    for shieldBonus in range(0, 5, 1):
                        for luckBonus in range(0, 5, 1):
                            if self.getCostOfBonuses(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                     luckBonus) < self.PROTECTION_RATIO * networth:
                                totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus,
                                                                shieldBonus, luckBonus)
                                if totalBonus > maxBonus:
                                    maxBonus = totalBonus
        return maxBonus

    def getCostOfBonuses(self, armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus, luckBonus):
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

        if self.luck == True:
            luckBonusPrice = self.getPrice(luckBonus, self.LUCK_BONUS_FACTOR)
        else:
            luckBonusPrice = 0

        return armorBonusPrice + naturalArmorBonusPrice + deflectionBonusPrice + shieldBonusPrice + luckBonusPrice

    def getTotalBonus(self, armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus, luckBonus):
        if self.armor == False:
            armorBonus = 0
        if self.natural == False:
            naturalArmorBonus = 0
        if self.deflection == False:
            deflectionBonus = 0
        if self.shield == False:
            shieldBonus = 0
        if self.luck == False:
            luckBonus = 0

        return armorBonus + naturalArmorBonus + deflectionBonus + shieldBonus + luckBonus

    def getMaxSurplus(self, networth):
        maxSurplus = -1
        maxBonus = self.getMaxBonus(networth)
        for armorBonus in range(0, 5, 1):
            for naturalArmorBonus in range(0, 5, 1):
                for deflectionBonus in range(0, 5, 1):
                    for shieldBonus in range(0, 5, 1):
                        for luckBonus in range(0, 5, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            luckBonus)
                            if totalBonus == maxBonus:
                                surplus = self.PROTECTION_RATIO * networth - self.getCostOfBonuses(armorBonus,
                                                                                                   naturalArmorBonus,
                                                                                                   deflectionBonus,
                                                                                                   shieldBonus,
                                                                                                   luckBonus)
                                if surplus > maxSurplus:
                                    maxSurplus = surplus
        return maxSurplus

    def getOptimalBonusSet(self, networth):
        maxBonus = self.getMaxBonus(networth)
        maxSurplus = self.getMaxSurplus(networth)
        maxArmorBonus = 0
        maxNaturalArmorBonus = 0
        maxDeflectionBonus = 0
        maxShieldBonus = 0
        maxLuckBonus = 0
        for armorBonus in range(0, 5, 1):
            for naturalArmorBonus in range(0, 5, 1):
                for deflectionBonus in range(0, 5, 1):
                    for shieldBonus in range(0, 5, 1):
                        for luckBonus in range(0, 5, 1):
                            totalBonus = self.getTotalBonus(armorBonus, naturalArmorBonus, deflectionBonus, shieldBonus,
                                                            luckBonus)
                            if totalBonus == maxBonus:
                                surplus = self.PROTECTION_RATIO * networth - self.getCostOfBonuses(armorBonus,
                                                                                                   naturalArmorBonus,
                                                                                                   deflectionBonus,
                                                                                                   shieldBonus,
                                                                                                   luckBonus)
                                if surplus == maxSurplus:
                                    if self.armor == True:
                                        maxArmorBonus = armorBonus
                                    if self.natural == True:
                                        maxNaturalArmorBonus = naturalArmorBonus
                                    if self.deflection == True:
                                        maxDeflectionBonus = deflectionBonus
                                    if self.shield == True:
                                        maxShieldBonus = shieldBonus
                                    if self.luck == True:
                                        maxLuckBonus = luckBonus
        print("AB: +{0:<2d}  NAB: +{1:<2d}  DB +{2:<2d}  SB +{3:<2d}  LB +{4:<2d}".format(maxArmorBonus,
                                                                                          maxNaturalArmorBonus,
                                                                                          maxDeflectionBonus,
                                                                                          maxShieldBonus, maxLuckBonus))
