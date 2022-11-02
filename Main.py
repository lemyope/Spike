from Compet import *
from Races import *


AfficheCompet()
terrain=eval(input("Choisir la competition : "))
ReturnCompet(terrain)

print("============================")

ListRaces()
indexRace=eval(input("Race ? = "))
ReturnRace(indexRace)

