from dataclasses import dataclass
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
    equipment: list
    disciplines: list
    meals: int
    crowns: int

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
    mindforce: bool = False
    
@dataclass
class Encounter:
    text: str
    type: str
    skillcheck: bool = False
    #### encounter options and associated text
   
    
    ### logic to proceed to next encounter

    #### optional skill check

    #### optional item check


    ### optional meal check
    meal_check: bool = False
    if meal_check and "Hunting" not in Player.disciplines:
        Player.endurance = Player.endurance - 3


###example encounter###
1
# You must make haste for you sense it is not safe to linger by the smoking remains of the ruined monastery. The black-winged beasts could return at any moment. You must set out for the Sommlending capital of Holmgard and tell the King the terrible news of the massacre: that the whole of the Kai warriors, save yourself, have been slaughtered. Without the Kai Lords to lead her armies, Sommerlund will be at the mercy of their ancient enemy, the Darklords.
# Fighting back tears, you bid farewell to your dead kinsmen. Silently, you promise that their deaths will be avenged. You turn away from the ruins and carefully descend the steep track.
# At the foot of the hill, the path splits into two directions, both leading into a large wood.



# If you wish to use your Kai Discipline of Sixth Sense, turn to 141.
# If you wish to take the right path into the wood, turn to 85.
# If you wish to follow the left track, turn to 275.
######
@dataclass
class Discipline:
    name: str

    @property
    def namecheck(self, name):
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
                Enemy.mindforce = False




if __name__ == "__main__":
    donkey = Enemy("donkey", 2)
    print(donkey.stats)





    

