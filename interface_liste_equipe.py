'''Module d'interface pour BloodBowl '''

# on commence toujours par importer le module tkinter
from tkinter import *
from Races import *

def btnFermer():
	# bouton de sortie
	bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
	bouton.pack()


# il suffit alors de déclarer l'objet Tk()
# qui deviendra la fenêtre principale
fenetre = Tk()
# Param supp de la fenetre
fenetre.title('PythonGuides')
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

# liste
liste = Listbox(fenetre)

# print("la longueur du tableau est {}".format(len(Race)))

i = 30
#i = int(len(Race))
while i>=0:
	ElementRace = Race[i]
#	print("ElementRace {} et i vaut {} ".format(ElementRace, i))
	liste.insert(i, ElementRace)
	i -= 1
	print("i vaut {}".format(i))

liste.pack()

# canvas
# canvas = Canvas(fenetre, width=640, height=320, background='blue')
# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
# canvas.pack()

btnFermer()

# pour finir, on lance la boucle programme
fenetre.mainloop()

# that's all, folks!