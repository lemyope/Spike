from ttkwidgets.autocomplete import AutocompleteEntry
from tkinter import *
from Races import *

# countries = [
        # 'Antigua and Barbuda', 'Bahamas','Barbados','Belize', 'Canada',
        # 'Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador ',
        # 'Grenada', 'Guatemala ', 'Haiti', 'Honduras ', 'Jamaica', 'Mexico',
        # 'Nicaragua', 'Saint Kitts and Nevis', 'Panama ', 'Saint Lucia', 
        # 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America'
        # ]

def btnFermer():
	# bouton de sortie
	bouton=Button(ws, text="Fermer", command=ws.quit)
	bouton.pack(pady=20)

def RacesAutocomplete():
	countries = GetRace()

	frame = Frame(ws, bg='#f25252')
	frame.pack(expand=True)

	Label(
		frame, 
		bg='#f25252',
		font = ('Times',21),
		text='Liste des Races de Bloodbowl 2'
		).pack()

	entry = AutocompleteEntry(
		frame, 
		width=30, 
		font=('Times', 18),
		completevalues=countries
		)
	entry.pack(padx = 20, pady = 20)

ws = Tk()
ws.title('BloodBowl - Races')
ws.geometry('400x300')
ws.config(bg='#f25252')

l = LabelFrame(ws, text="Choisir la race")
l.pack(fill="both", expand="yes")
Label(l, text="A l'intérieure de la frame").pack()
Label(l, text=RacesAutocomplete()).pack()

p = PanedWindow(ws, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, text='Volet 1', background='blue', anchor=W))
p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
p.add(Label(p, text='Volet 3', background='red', anchor=E) )
p.pack()

btnFermer()

ws.mainloop()