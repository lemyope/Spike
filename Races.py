""" Module des races de BloodBowl """
""" prototype """
""" *- ListRaces() """
""" *- indexRace=eval(input("Race ? = ")) """
""" *- ReturnRace(indexRace) """

Race=["Amazones","Bas-Fonds","Bretonniens","Chaos","Elfes Noirs","Elfes Pro","Elfes Sylvains","Gobelins","Halflings","Hauts Elfes","Hommes Lézards","Humains","Khemris","Le Cirque Kislevite","Morts-Vivants","Nains","Nains du Chaos","Necromantiques","Nordiques","Nurgles","Ogres","Orcs","Skavens","Vampires","-------------------------","Alliance de la Bienfaisance (AB)","Association du Levant (AL)","Grande Coalition Elfique (GCE)","L'entente des Petites Gens (EPG)","Ligue des Bres Superieurs (LES)","Ligue Humanoide (LH)","Pacte des Joueurs Chaotiques (PJC)","Séléction des Dieux du Chaos (SDC)","Société Anti Fourrure (SAF)","Union de L'au dela (UA)","Violent Ensemble (VE)"]

indexRace = 0

def ReturnRace(indexRace):
	print(Race[indexRace])
	
def ListRaces():
	for indice in Race:
		print(indice)
	
def GetRace():
	return(Race)


# ListRaces()
# indexRace=eval(input("Race ? = "))
# ReturnRace(indexRace)