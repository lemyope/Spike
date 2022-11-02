'''Module d'interface pour BloodBowl '''

# on commence toujours par importer le module tkinter
from tkinter import *

def btnFermer():
	# bouton de sortie
	bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
	bouton.pack()


# il suffit alors de déclarer l'objet Tk()
# qui deviendra la fenêtre principale
fenetre = Tk()

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

# canvas
canvas = Canvas(fenetre, width=150, height=120, background='gray')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", 
fill="blue")
canvas.pack()
# Vous pouvez créer d'autres éléments:
# create_arc() : arc de cercle
# create_bitmap() : bitmap
# create_image() : image
# create_line() : ligne
# create_oval() : ovale
# create_polygon() : polygone
# create_rectangle() : rectangle 
# create_text() : texte
# create_window() : fenetre

btnFermer()

# pour finir, on lance la boucle programme
fenetre.mainloop()

# that's all, folks!