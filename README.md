# pathfinder-1e-_item_bonus_tool
I have developed this tool to aid my decision making on distributing loot as a DM, but also for the players to check which magic items the Pathfinder 1e rule set expects them to have. Treat the output as advise but not as a rule 'must have'. The logic is very basic and does not account for various circumstances that might be important in your campaign, such as availability of magic items. Note in particular, at very high levels this tool will suggest magic items that can be crafted, but are not available by default (Ring of Protection +6 and higher)

I have initially developed this tool on my phone (shout out to Pydroid 3) during commuting. As such it may need some serious polishing at some point. However, this project is mostly on hold, as my group moved on from Pathfinder 1e.

# Basic Usage GUI
Execute
```sh
python optimal_pc_boni_gui.py 
```
and you will be greeted with a graphic user interface:

![Alt text](https://github.com/sgerloff/pathfinder-1e-_item_bonus_tool/blob/master/gui_guide.jpg?raw=true "Title")

* In the top row you can chose your character level as well as type, e.g. player characters, non-player characters and heroic NPC's. Both options determine the total gold available to the character.

* (1) Next chose the which kind of armor is available to the character, according to armor proficiencies and slots available. Note that natural armor bonus, deflection bonus and similar refer to the usual default items (amulet of natural armor, ring of protection), but can in principle also be provided by other magic items or abilities. Since they do not stack, you should check them off in some cases.

* (2) Finally, your choices will generate a list of suggested items, as well as state remaining gold. The total bonus to the AC is listed as a quick reference for DM's to gauge appropriate attack modifiers for potential monster and encounters.  

# Basic Usage from Command Line
If you prefer to get the output from the command line use for example
```sh
python magicItemSuggestions.py pc 9 "asrn" 
```
This will provide item suggestions for a player character at level 9 with armor, shield, cloak of resistance and an amulett of natural armor. To enbale the deflection bonus or other boni add "d" or "o" to the string, similarly remove the entries to disable them.

# Simple Encounter Generator
This tool can be reused to generate random encounters of NPC's of a particular level, using 
```sh
python warriorEncounter.py 6 4
```
which will list 6 NPC's each level 4. Every NPC will be randomly equiped with ranged or melee weapons, random race, and random armor.

```sh
1. NPC:

Warrior: melee halfelf  , Armor: medium    , Shield:
HP:   26±6  , Init: 0 , Speed:  4F
AC: 15, Touch: 10, Flat: 15
Ref.: 1 , Will: 1 , Fort.: 5
CMB: 7 , CMD: 17
AB: +7 / +0 / +0 / +0 , halberd2H: 4+1D10 x3


2. NPC:

Warrior: melee halforc  , Armor: heavy     , Shield:
HP:   26±6  , Init: 0 , Speed:  4F
AC: 17, Touch: 10, Flat: 17
Ref.: 1 , Will: 1 , Fort.: 5
CMB: 7 , CMD: 17
AB: +7 / +0 / +0 / +0 , sword: 3+1D6 19-20/x2


3. NPC:

Warrior: melee halfelf  , Armor: medium    , Shield:
HP:   26±6  , Init: 0 , Speed:  4F
AC: 15, Touch: 10, Flat: 15
Ref.: 1 , Will: 1 , Fort.: 5
CMB: 7 , CMD: 17
AB: +7 / +0 / +0 / +0 , axe: 3+1D8 x3


4. NPC:

Warrior: range halfelf  , Armor: light     , Shield:
HP:   26±6  , Init: 3 , Speed:  6F
AC: 15, Touch: 13, Flat: 12
Ref.: 4 , Will: 0 , Fort.: 5
CMB: 4 , CMD: 17
AB: +7 / +0 / +0 / +0 , longbow: 0+1W8 x3


5. NPC:

Warrior: melee dwarf    , Armor: medium    , Shield:
HP:   30±6  , Init: 0 , Speed:  4F
AC: 15, Touch: 10, Flat: 15
Ref.: 1 , Will: 2 , Fort.: 6
CMB: 6 , CMD: 16
AB: +6 / +0 / +0 / +0 , curved: 2+1D6 18-20/x2


6. NPC:

Warrior: range halfelf  , Armor: light     , Shield:
HP:   26±6  , Init: 3 , Speed:  6F
AC: 15, Touch: 13, Flat: 12
Ref.: 4 , Will: 0 , Fort.: 5
CMB: 4 , CMD: 17
AB: +7 / +0 / +0 / +0 , crossbow: 0+1W8 19-20/x2
```

If you want to use this for your DM purposes I recommend to alter the output and specifications to your needs. This example is a proof of concept at best.
