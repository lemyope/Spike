from tkinter import *

fenetre = Tk()
fenetre.title('BloodBowl - Gestion des titres')
fenetre.geometry('1280x720')
fenetre.config(bg='#345')

texte = Label(fenetre, text="Gestion des titres", padx=20, pady=20)

l = LabelFrame(fenetre, text="Définir le match", height=400, width=1000, padx=20, pady=20)
l.pack(fill="both", expand="no")
Label(l, text="A l'intérieure de la frame").pack()

l2 = LabelFrame(fenetre, text="Définir les titres", height=400, width=1000, padx=20, pady=20)
l2.pack(fill="both", expand="yes")
Label(l2, text="A l'intérieure de la frame").pack()

# Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, 
# pady=5)
# Button(fenetre, text ='Bouton 1').pack(side=LEFT, padx=5, pady=5)
# Button(fenetre, text ='Bouton 2').pack(side=RIGHT, padx=5, pady=5)

fenetre.mainloop()