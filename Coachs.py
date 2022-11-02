'''Module de gestion des Coaches '''


def AfficheCoaches(Coaches):
	# for indice in Coaches:
	print("liste des Coaches {} ".format(Coaches))
		
def ReturnCoach(tCoaches):

	Coaches = tCoaches

#	print(Coaches[indice])
	
	lentab = len(Coaches)
	print("Entrer un nombre entre -1 et {} ".format(lentab))

	x = eval(input("Entrer un nombre :"))
	if x>-1 and x<lentab:
		print("ResultCoaches vaut {0} et x = {1}".format(Coaches[x],x))
	else:
		print("entrée invalide")
	

def CreatedbCoach(dbCoaches):
#	Marche pas vraiment comme elle devrait - ne pas utiliser
	NomCoach = input("Quel est le nom du coach à ajouter à liste ?")
	lentab = len(dbCoaches)
	dbCoaches.append(NomCoach)
	f = open("Coachs.csv", "w")
	f.write(dbCoaches)
	f.close()

def CreateCoach(dbCoaches):
	NomCoach = input("Quel est le nom du coach à ajouter à liste ?")
	f = open("Coachs.csv", "a")
	f.write(NomCoach)
	f.close()

def UpdateCoach(UdateChampsCoach):
	NomCoach = input("Quel est le nom du coach à mettre à jour dans la liste ?")

def DeleteCoach(NomCoach):
	NomCoach = input("Quel est le nom du coach à effecer dans la liste ?")

def ReadCoaches():
	f = open("Coachs.csv", "rt")
	ResultCoaches = f.read()
	tab = ResultCoaches.split(';')
#	tab = tab1.replace('\n',' ')
	f.close()
	return(tab)

def GetCoaches():
	rCoaches = ReadCoaches()
	return rCoaches

# ListeCoache = ReadCoaches()
# AfficheCoaches(ListeCoache)
# CreateCoach(ListeCoache)
# ReturnCoach(ListeCoache)