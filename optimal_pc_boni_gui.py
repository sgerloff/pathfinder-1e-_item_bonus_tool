import math
import tkinter as tk
from Classes.protectionBonuses import ProtectionBonuses
from Classes.weaponBonus import WeaponBonus
from Classes.attributeBonuses import AttributeBonuses

from Classes.playerCharacter import PlayerCharacter

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.text = tk.StringVar(self)

        self.wb = WeaponBonus()
        self.pb = ProtectionBonuses()
        self.ab = AttributeBonuses()

        self.characterLevel = tk.IntVar(self)
        self.characterLevel.set(1)

        self.armorBonus = tk.BooleanVar(self)
        self.shieldBonus = tk.BooleanVar(self)
        self.saveBonus = tk.BooleanVar(self)
        self.naturalBonus = tk.BooleanVar(self)
        self.deflectionBonus = tk.BooleanVar(self)
        self.otherBonus = tk.BooleanVar(self)

        self.master.title("Pathfinder Wealth Distributor")
        # self.master.geometry("1000x1000")
        self.pack()

        self.setCharacterLevel()
        self.setArmorCheckboxes()

        self.l = tk.Label(self, textvariable=self.text, wraplength=350, width="50", height="12")
        self.l.grid(columnspan=2)
        self.updateSummary("")

    def setCharacterLevel(self):
        cl_label = tk.Label(self, text="Character Level:")
        cl_label.grid(row=0, column=0, sticky="w")

        character_levels_list = list(range(1, 21))
        self.characterLevel.set(character_levels_list[0])

        opt = tk.OptionMenu(self, self.characterLevel, *character_levels_list, command=self.updateSummary)
        opt.config(width=1)
        opt.grid(row=0, column=1, sticky="w")

    def setArmorCheckboxes(self):
        protection_bonus_label = tk.Label(self, text="Armor Options:")
        protection_bonus_label.grid(columnspan=2, sticky="W")

        armor_cb = tk.Checkbutton(self, text='Armor', variable=self.armorBonus, onvalue=True, offvalue=False,
                                  command=self.updateArmor)
        armor_cb.grid(columnspan=2, sticky="W")

        shield_cb = tk.Checkbutton(self, text='Shield', variable=self.shieldBonus, onvalue=True, offvalue=False,
                                   command=self.updateArmor)
        shield_cb.grid(columnspan=2, sticky="W")

        save_cb = tk.Checkbutton(self, text='Cloak of Resistance', variable=self.saveBonus, onvalue=True,
                                 offvalue=False, command=self.updateArmor)
        save_cb.grid(columnspan=2, sticky="W")

        natural_cb = tk.Checkbutton(self, text='Natural Armor Bonus', variable=self.naturalBonus, onvalue=True,
                                    offvalue=False, command=self.updateArmor)
        natural_cb.grid(columnspan=2, sticky="W")

        deflection_cb = tk.Checkbutton(self, text='Deflection Bonus', variable=self.deflectionBonus, onvalue=True,
                                       offvalue=False, command=self.updateArmor)
        deflection_cb.grid(columnspan=2, sticky="W")

        other_cb = tk.Checkbutton(self, text='Other Magic Bonus (luck,...)', variable=self.otherBonus, onvalue=True,
                                  offvalue=False, command=self.updateArmor)
        other_cb.grid(columnspan=2, sticky="W")

    def updateArmor(self):
        self.pb.armor = self.armorBonus.get()
        self.pb.shield = self.shieldBonus.get()
        self.pb.save = self.saveBonus.get()
        self.pb.natural = self.naturalBonus.get()
        self.pb.deflection = self.deflectionBonus.get()
        self.pb.other = self.otherBonus.get()
        self.updateSummary("")

    def updateSummary(self, event):
        pc = PlayerCharacter(self.characterLevel.get())
        self.wb.setForCharacter(pc)
        self.pb.setForCharacter(pc)
        self.ab.setForCharacter(pc)

        total = "The expected networth is {}gp. Suggested magic items: \n\n".format(pc.networth)
        if self.wb.maxBonus > 0:
            total += "Magic weapon +{:<2d}".format(self.wb.maxBonus)
        else:
            total += "No magic weapon"
        if self.pb.maxArmorBonus > 0:
            total += ",\n Magic Armor +{:<2d}".format(self.pb.maxArmorBonus)
        if self.pb.maxShieldBonus > 0:
            total += ",\n Magic Shield +{:<2d}".format(self.pb.maxShieldBonus)
        if self.pb.saveBonus > 0:
            total += ",\n Cloak of Resistance +{:<2d}".format(self.pb.saveBonus)
        if self.pb.maxNaturalArmorBonus > 0:
            total += ",\n Amulet of Natural Armor +{:<2d}".format(self.pb.maxNaturalArmorBonus)
        if self.pb.maxDeflectionBonus > 0:
            total += ",\n Ring of Protection +{:2d}".format(self.pb.maxDeflectionBonus)
        if self.pb.maxOtherBonus > 0:
            total += ",\n Ring of Luck +{:2d}".format(self.pb.maxOtherBonus)
        if self.ab.maxBonus > 0:
            total += ",\n Belt/Circlet of ... +{:2d}.".format(self.ab.maxBonus)
        else:
            total +=", No attribute enhancing item."

        total += "\n\n total AC bonus +{:<2d}".format(self.pb.maxBonus)
        total += ", total surplus: {}gp".format(int(self.wb.maxSurplus + self.pb.maxSurplus + self.ab.maxSurplus))

        self.text.set(total)


root = tk.Tk()
myapp = App(root)
myapp.mainloop()