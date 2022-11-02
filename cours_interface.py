'''Module d'interface pour BloodBowl '''

# on commence toujours par importer le module tkinter
from tkinter import *

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

# entrée (Il faut utiliser la classe StringVar )
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

# checkbutton
# tabulation \t dans le texte bouton marche
bouton = Checkbutton(fenetre, text="\tTexte de la checkbox")
bouton.pack()

# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peut-être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
liste.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# pour finir, on lance la boucle programme
fenetre.mainloop()

# that's all, folks!
# mais c'est tout petit

