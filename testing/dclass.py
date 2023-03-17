from dataclasses import dataclass, field
import random
def randstat():
    return random.randint(0,10)

@dataclass
class Stats:
    combatskill: int = 0
    endurance: int = 0
    
    def __add__(self, other):
        combatskill = self.combatskill + other.combatskill
        endurance = self.endurance + other.endurance
        stats = Stats(combatskill, endurance)
        return stats

    def __remove__(self, other):
        combatskill = self.combatskill - other.combatskill
        endurance = self.endurance - other.endurance
        stats = Stats(combatskill, endurance)
        return stats

@dataclass
class Equipment:
    name: str
    description: str
    stats: Stats

@dataclass
class Player:
    stats: Stats
    equipment: list = field(default_factory=list)
    disciplines: list = field(default_factory=list)
    meals: int = 1
    crowns: int = randstat()

    @property
    def base_stats(self):
        self.combatskill = randstat() + 10
        self.endurance = randstat() + 20
        self.maxendurance = self.endurance

    @property  
    def equip(self, equipment: Equipment):
        self.equipment.add(equipment)

    def drop(self, equipment: Equipment):
        self.equipment.remove(equipment)

@dataclass
class Enemy:
    name: str
    stats: Stats
    immunities: bool = False
    special_skills: list = field(default_factory=list)

@dataclass
class Encounter:
    text: str
    encounter_num: int
    ##'options' will be the number of choices for a given encounter. Potentially add a function that will print all of the choice options as defined by the 'Choice' class
    options: int
    
    #### optional skill check


    #### optional item check


    ### optional meal check

    meal_check: bool = False
    if meal_check and "Hunting" not in Player.disciplines:
        Player.endurance = Player.endurance - 3

    #### encounter options and associated text
    
    @dataclass
    class Choice:
        def check_skill(x):
            if x in Player.disciplines:
                pass
            else:
                print('You do not possess that skill')
        #choice_num will be the number the player needs to input
        choice_num: int
        text: str
        #'result' will run the encounter for the associated encounter number
        result: int
        skillcheck: bool = False
        if skillcheck:
            x = skillname
            check_skill(x)
    
    ### logic to proceed to next encounter         

@dataclass
class Discipline:
    name: str
    description: str

    def discipline_check(self, name):
        if name == "Weaponskill":
            x = randstat()
            weaponlist = ["Dagger","Spear","Mace","Short Sword","Warhammer","Sword","Axe","Sword","Quarterstaff","Broadsword"]
            if weaponlist[x] in Player.equipment:
                Player.combatskill = Player.combatskill + 2
        elif name == "Healing":
            if Encounter.type != "combat" and Player.endurance < Player.maxendurance:
                Player.endurance +=1
        elif name == "Mindblast" and "Mindblast" not in Enemy.immunities:
            Player.combatskill = Player.combatskill + 2
        elif name == "Hunting":
            Encounter.meal_check = False
        elif name == "Mindshield":
            if "Mindblast" in Enemy.special_skills:
                Enemy.special_skills.remove("Mindblast")

##Disciplines - these will go into a different file later for legibility

hunting = Discipline("Hunting", "This skill ensures that a Kai Lord will never starve in the wild. He will always be able to hunt for food for himself except in areas of wasteland and desert. The skill also enables a Kai Lord to be able to move stealthily when stalking his prey.")
camouflage = Discipline("Camouflage", "This Discipline enables a Kai Lord to blend in with his surroundings. In the countryside, he can hide undetected among trees and rocks and pass close to an enemy without being seen. In a town or city, it enables him to look and sound like a native of that area, and can help him to find shelter or a safe hiding place.")



###   EXAMPLE ENCOUNTER  ###
e1 = Encounter("You must make haste for you sense it is not safe to linger by the smoking remains of the ruined monastery. The black-winged beasts could return at any moment. You must set out for the Sommlending capital of Holmgard and tell the King the terrible news of the massacre: that the whole of the Kai warriors, save yourself, have been slaughtered. Without the Kai Lords to lead her armies, Sommerlund will be at the mercy of their ancient enemy, the Darklords.\n\nFighting back tears, you bid farewell to your dead kinsmen. Silently, you promise that their deaths will be avenged. You turn away from the ruins and carefully descend the steep track.\n\nAt the foot of the hill, the path splits into two directions, both leading into a large wood.\n\n", 1, 3)

c1 = e1.Choice(1, "If you wish to use your Kai Discipline of Sixth Sense, turn to 141", 141, skillcheck = True)
c2 = e1.Choice(2, "If you wish to take the right path into the wood, turn to 85.", 85)
c3 = e1.Choice(3, "If you wish to follow the left track, turn to 275.", 275)


e85 = Encounter("The path is wide and leads straight into thick undergrowth. The trees are tall here and unusually quiet. You walk for over a mile when suddenly you hear the beating of large wings directly above you. Looking up, you are shocked to see the sinister black outline of a Kraan diving to attack you.", 85, 2)


######

if __name__ == "__main__":
    print(hunting.description)
    



    

