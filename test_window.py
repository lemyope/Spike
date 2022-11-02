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

ws['bg']='white'
# frame 1
Frame1 = Frame(ws, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)
# frame 2
Frame2 = Frame(ws, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)
# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)
# Ajout de labels
Label(Frame1, text=RacesAutocomplete()).pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)


btnFermer()

ws.mainloop()