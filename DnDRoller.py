'''
Ryan Muncy
04/25/2023

DnD Roller
This program aims to automatically roll a 20 sided dice until it has enough results to make a character in DnD. Additional Functionality to auto-pick stats will be added based on user preference.
'''

import random

def rollDie(n):
    #rolls an n-sided die
    x = random.randrange(1, n+1)
    return(x)

def makeNumber():
    #determins a single ability off 5e dice roll rules
    rollList = []
    for i in range(4):
         rollList.append(rollDie(6))
    ##print(rollList)
    rollList.sort()
    ##print(rollList)
    rollList.pop()
    ##print(rollList)
    x = sum(rollList)
    ##print(x)
    return(x)

def rollAbilities():
    #creates a list of numbers, one for each ability
    abilityList = []
    for i in range(6):
        a = makeNumber()
        abilityList.append(a)
        ##print(a)
    ##print(abilityList)
    return(abilityList)

class dndChar:

    def __init__(self, charName, charRace, charClass):
        self.charName = str(charName)
        self.charRace = charRace
        self.charClass = charClass
        self.Strength = self.charRace.strBuff
        self.Dexterity = self.charRace.dexBuff
        self.Constitution = self.charRace.constBuff
        self.Intelligence = self.charRace.intBuff
        self.Wisdom = self.charRace.wisBuff
        self.Charisma = self.charRace.charBuff

    def show(self):
        print('Your characters name is ', self.charName, '. They are a(n)', self.charRace.name, self.charClass.name, 'Their abilities are as follows \n', 'Strength:', self.Strength, 'Dexterity:', self.Dexterity, 'Constitution:', self.Constitution, 'Intelligence:', self.Intelligence, 'Wisdom:', self.Wisdom, 'Charisma:', self.Charisma)

    def assignAbilities(self):
        aList = rollAbilities()
        aList.sort()
        self.Strength += aList[self.charClass.strPriority]
        self.Dexterity += aList[self.charClass.dexPriority]
        self.Constitution += aList[self.charClass.constPriority]
        self.Intelligence += aList[self.charClass.intPriority]
        self.Wisdom += aList[self.charClass.wisPriority]
        self.Charisma += aList[self.charClass.charPriority]

class ClassBarbarian:

    def __init__(self):
        self.name = 'Barbarian'
        self.strPriority = 5
        self.constPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.intPriority = pList[1]
        self.wisPriority = pList[2]
        self.charPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassBard:

    def __init__(self):
        self.name = 'Bard'
        self.dexPriority = 4
        self.charPriority = 5
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.strPriority = pList[0]
        self.intPriority = pList[1]
        self.wisPriority = pList[2]
        self.constPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassCleric:

    def __init__(self):
        self.name = 'Cleric'
        self.wisPriority = 5
        self.charPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.intPriority = pList[1]
        self.strPriority = pList[2]
        self.constPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassDruid:

    def __init__(self):
        self.name = 'Druid'
        self.intPriority = 4
        self.wisPriority = 5
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.strPriority = pList[1]
        self.constPriority = pList[2]
        self.charPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassFighter:

    def __init__(self):
        self.name = 'Fighter'
        self.strPriority = 5
        self.constPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.intPriority = pList[1]
        self.wisPriority = pList[2]
        self.charPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassMonk:

    def __init__(self):
        self.name = 'Monk'
        self.strPriority = 3
        self.dexPriority = 5
        self.wisPriority = 4
        pList = []
        while len(pList) < 3:
            x = rollDie(3) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.constPriority = pList[0]
        self.intPriority = pList[1]
        self.charPriority = pList[2]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassPaladin:

    def __init__(self):
        self.name = 'Paladin'
        sself.strPriority = 3
        self.charPriority = 4
        self.wisPriority = 5
        pList = []
        while len(pList) < 3:
            x = rollDie(3) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.constPriority = pList[0]
        self.intPriority = pList[1]
        self.dexPriority = pList[2]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassRanger:

    def __init__(self):
        self.name = 'Ranger'
        self.strPriority = 3
        self.dexPriority = 5
        self.wisPriority = 4
        pList = []
        while len(pList) < 3:
            x = rollDie(3) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.constPriority = pList[0]
        self.intPriority = pList[1]
        self.charPriority = pList[2]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassRogue:

    def __init__(self):
        self.name = 'Rogue'
        self.dexPriority = 5
        self.intPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.strPriority = pList[0]
        self.constPriority = pList[1]
        self.wisPriority = pList[2]
        self.charPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassSorcerer:

    def __init__(self):
        self.name = 'Sorcerer'
        self.charPriority = 5
        self.constPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.intPriority = pList[1]
        self.wisPriority = pList[2]
        self.strPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassWarlock:

    def __init__(self):
        self.name = 'Warlock'
        self.charPriority = 5
        self.wisPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.intPriority = pList[1]
        self.strPriority = pList[2]
        self.constPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class ClassWizard:

    def __init__(self):
        self.name = 'Wizard'
        self.intPriority = 5
        self.wisPriority = 4
        pList = []
        while len(pList) < 4:
            x = rollDie(4) - 1
            if x not in pList:
                pList.append(x)
        ##print(pList)
        self.dexPriority = pList[0]
        self.strPriority = pList[1]
        self.constPriority = pList[2]
        self.charPriority = pList[3]
        ##print(self.strPriority, self.constPriority, self.dexPriority, self.intPriority, self.wisPriority, self.charPriority)

class RaceDragonborn:

    def __init__(self):
        self.name = 'Dragonborn'
        self.strBuff = 2 
        self.dexBuff = 0
        self.constBuff = 0
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 1
        
class RaceGnome:

    def __init__(self):
        self.name = 'Gnome'
        self.strBuff = 0
        self.dexBuff = 0
        self.constBuff = 0
        self.intBuff = 2
        self.wisBuff = 0
        self.charBuff = 0
        
class RaceDwarf:

    def __init__(self):
        self.name = 'Dwarf'
        self.strBuff = 0 
        self.dexBuff = 0
        self.constBuff = 2
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 0
        
class RaceElf:

    def __init__(self):
        self.name = 'Elf'
        self.strBuff = 0 
        self.dexBuff = 2
        self.constBuff = 0
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 0
        
class RaceHalfElf:

    def __init__(self):
        self.name = 'Half-Elf'
        self.strBuff = 1 
        self.dexBuff = 0
        self.constBuff = 1
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 2
        
class RaceHalfling:

    def __init__(self):
        self.name = 'Halfing'
        self.strBuff = 0 
        self.dexBuff = 2
        self.constBuff = 0
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 0
        
class RaceHalfOrc:

    def __init__(self):
        self.name = 'Half-Orc'
        self.strBuff = 2 
        self.dexBuff = 0
        self.constBuff = 1
        self.intBuff = 0
        self.wisBuff = 0
        self.charBuff = 0
        
class RaceHuman:

    def __init__(self):
        self.name = 'Human'
        self.strBuff = 1 
        self.dexBuff = 1
        self.constBuff = 1
        self.intBuff = 1
        self.wisBuff = 1
        self.charBuff = 1
        
class RaceTiefling:

    def __init__(self):
        self.name = 'Tiefling'
        self.strBuff = 1
        self.dexBuff = 0
        self.constBuff = 0
        self.intBuff = 1
        self.wisBuff = 0
        self.charBuff = 2

x = 0
y = 0
z = 0

print("Please enter STOP to stop the program at any time.")
while True:
    x = input("What is your characters name? ")
    if x == 'STOP':
        exit()
    else:
        break
while True:
    y = input("What is your characters race? ").lower()
    if 'tiefling' in y:
        y = RaceTiefling()
        break
    elif 'human' in y:
        y = RaceHuman
        break
    elif 'orc' in y:
        y = RaceHalfOrc()
        break
    elif 'halfling' in y:
        y = RaceHalfling()
        break
    elif 'elf' and not 'half' in y:
        y = RaceElf()
        break
    elif 'half' and 'elf' in y:
        y = RaceHalfElf()
        break
    elif 'dwarf' in y:
        y = RaceDwarf()
        break
    elif 'gnome' in y:
        y = RaceGnome()
        break
    elif 'dragonborn' in y:
        y = RaceDragonborn()
        break
    elif 'stop' in y:
        exit()
    else:
        print("Sorry I do not recognize that one.")
while True:
    z = input("What is your characters class? ").lower()
    if 'ranger' in z:
        z = ClassRanger()
        break
    elif 'monk' in z:
        z = ClassMonk()
        break
    elif 'wizard' in z:
        z = ClassWizard()
        break
    elif 'warlock' in z:
        z = ClassWarlock()
        break
    elif 'sorcerer' in z:
        z = ClassSorcerer()
        break
    elif 'rogue' in z:
        z = ClassRogue()
        break
    elif 'paladin' in z:
        z = ClassPaladin()
        break
    elif 'fighter' in z:
        z = ClassFighter()
        break
    elif 'druid' in z:
        z = ClassDruid()
        break
    elif 'cleric' in z:
        z = ClassCleric()
        break
    elif 'bard' in z:
        z = ClassBard()
        break
    elif 'barbarian' in z:
        z = ClassBarbarian()
        break
    elif 'stop' in z:
        exit()
    else:
        print("Sorry I do not recognize that one.")

userCharOne = dndChar(x, y, z)
userCharOne.assignAbilities()
userCharOne.show()
