import random
import os
from subprocess import call

def clear():
    call('clear' if os.name =='posix' else 'cls')

newline = '\n'

def randstat():
    return random.randint(0,10)

def additem(item_name):
    p1.equipment.append(item_name)

class Character:
    def __init__(self,combatskill,endurance):
        self.combatskill = combatskill
        self.endurance = endurance
        self.crowns = randstat()
        self.equipment = ["Map","Axe"]
        self.disciplines = []
        self.meals = 1

p1 = Character(randstat() +10 , randstat() + 20)

def printdisc():
    for x in p1.disciplines:
        print(x)

def printstats():
    print(f'''
    
    Combat Skill: {p1.combatskill}
    Endurance:  {p1.endurance}
    Crowns:  {p1.crowns}
    Equipment:  {p1.equipment}
    Meals:  {p1.meals}
    
    Your Disciplines:
    {printdisc()}
    ''')

disciplinelist = [
    "Camouflage",
    "Hunting",
    "Sixth Sense",
    "Tracking",
    "Healing",
    "Mindshield",
    "Mindblast",
    "Animal Kinship",
    "Mind Over Matter",
    "Weaponskill",
]

weaponlist = [
    "Dagger",
    "Spear",
    "Mace",
    "Short Sword",
    "Warhammer",
    "Sword",
    "Axe",
    "Quarterstaff",
    "Broadsword",
]

def randweapon():
    x = randstat()
    if x == 0:
        weapon = weaponlist[0]
    elif x == 1:
        weapon = weaponlist[1]
    elif x == 2:
        weapon = weaponlist[2]
    elif x == 3:
        weapon = weaponlist[3]
    elif x == 4: 
        weapon = weaponlist[4]
    elif x == 5 or x == 7:
        weapon = weaponlist[5]
    elif x == 6:
        weapon = weaponlist[6] 
    elif x == 8:
        weapon = weaponlist[7]
    elif x == 9:
        weapon = weaponlist[8]
    print(f'You have chosen the discipline "weaponskill".  You will recieve 2 bonus combat points when carrying the {weapon}.')

def randitem():
    x = randstat()
    if x == 1:
        item = weaponlist[5]
        additem(item)
    elif x == 2:
        item = "Helmet (Special Items).  This adds 2 ENDURANCE points to your total."
        additem("Helmet")
        p1.endurance = p1.endurance + 2
    elif x == 3:
        item = "Two Meals"
        p1.meals = 3
    elif x == 4:
        item = "Chainmail Waistcoat (Special Items).  This adds 4 ENDURANCE points to your total."
        additem("Chainmail Waistcoat")
        p1.endurance = p1.endurance + 4
    elif x == 5:
        item = weaponlist[2]
        additem(item)
    elif x == 6:
        item = "Healing Potion (Backpack Item). This can restore 4 ENDURANCE points to your total, when swallowed after combat. You only have enough for one dose."
        p1.equipment.append("Healing Potion")
    elif x == 7:
        item = weaponlist[7]
        additem(item)
    elif x == 8:
        item = weaponlist[1]
        additem(item)
    elif x == 9:
        item = "12 Gold Crowns"
        p1.crowns = p1.crowns + 12
    elif x == 0:
        item = weaponlist[8]
        additem(item)
    print(f'You also find the following item:\n{item}')


if __name__ == "__main__":
    randitem()
    printstats()










