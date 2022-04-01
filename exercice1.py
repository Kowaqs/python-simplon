from random import randrange

nombreAleatoire = randrange(124)
choixUtilisateur = -1
compteur = 0
while  choixUtilisateur != nombreAleatoire :
	 
	choixUtilisateur = int(input("Choisit un nombre entre 0 et 123\n"))
	compteur = compteur+ 1
	if nombreAleatoire==choixUtilisateur :
		print ("Gagné")
	elif nombreAleatoire > choixUtilisateur : 
		print("Essaie plus grand")
	else :
		print("Essaie moins grand") 


print("Vous avez réussi en ", compteur) 