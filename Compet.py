""" Module de gestion de Competition """

# import Races

indice=int(0)

liste=["Anonyme","VisionHD","CIGF","Belgium Bowl","BHL UBC","CdV","LDV","AMIS","The Division 2","Artagggg Bowl","SORTIR"]

def AfficheCompet():
	i = 0
	print("ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
	print("º BloodBoowl 2 : Pitch Mod   º")
	print("ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
	print("")
	print("ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
	print("º 	Menu :						  º ")
	for indice in liste:
		i = i + 1
		print("º " + indice + "	º")
	print("")
	print("ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")

def ReturnCompet(IndexCompet):
	print(liste[IndexCompet])

# AfficheCompet()

# terrain=eval(input("Choisir la competition : "))

# ReturnCompet(terrain)
# exit()
