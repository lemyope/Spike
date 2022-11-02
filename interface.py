'''Module d'interface pour BloodBowl '''

# on commence toujours par importer le module tkinter
from tkinter import *
from Races import *
from Coachs import *

def btnFermer():
	# bouton de sortie
	bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
	bouton.pack(pady=20)

Tableau_des_races = GetRace()

# il suffit alors de déclarer l'objet Tk()
# qui deviendra la fenêtre principale
fenetre = Tk()
# Param supp de la fenetre
fenetre.title('BloodBowl')
fenetre.geometry('1280x720')
fenetre.config(bg='#345')

# on crée ensuite un objet Label()
# rattaché à fenetre
# pour afficher du texte non éditable
# on profite du constructeur de l'objet
# pour définir un texte "Hello World"
# dans la foulée (on peut faire autrement)
texte = Label(fenetre, text="Hello World")

# l'objet Label() nommé texte est ensuite
# rendu visible dans fenetre grâce à pack()
texte.pack()

# liste début #######################################
strTxtRaces = Label(fenetre, text="Liste des Races")
strTxtRaces.pack(pady=10)

liste = Listbox(fenetre)

i = 35
#i = int(len(Tableau_des_races))
while i>=0:
	ElementRace = Tableau_des_races[i]
	# print("ElementRace {} et i vaut {} ".format(ElementRace, i))
	plop = "{} {} ".format(i, ElementRace)
	liste.insert(i, plop)
	i -= 1
	# print("i vaut {}".format(i))

liste.pack()
# liste fin #########################################

# liste2 début #######################################
strTxtCoach = Label(fenetre, text="Liste des Coaches")
strTxtCoach.pack(pady=10)

liste2 = Listbox(fenetre)

Tableau_des_Coaches = GetCoaches()

#print("Tableau_des_Coaches vaut :{}".format(Tableau_des_Coaches))

y = 100
while y>=0:
	ElementCoach = Tableau_des_Coaches[y]
	# print("Tableau_des_Coaches vaut {} et y vaut {}".format(ElementCoach, y))
	ElementCoach2 = str(y)+" "+ElementCoach
	liste2.insert(y, ElementCoach2)
	y -= 1

liste2.pack()
# liste2 fin #########################################

def showSelected():
    show.config(text=liste2.get(ANCHOR))

Button(fenetre, text="Show selected", command=showSelected).pack(pady=10)
show = Label(fenetre)
show.pack()

# canvas
# canvas = Canvas(fenetre, width=640, height=320, background='blue')
# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
# canvas.pack()

btnFermer()

# pour finir, on lance la boucle programme
fenetre.mainloop()

# that's all, folks!