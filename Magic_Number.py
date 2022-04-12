import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIES = 4



def demander_nombre_magique(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("Erreur, Entrez un chiffre.")
        else:
            if nombre_int > nb_max or nombre_int < nb_min:
                print("Erreur, le nombre magique est compris entre", nb_min, "et", nb_max, "réessayez.")
                nombre_int = 0
    return nombre_int





gagne = False
for i in range(0,NOMBRE_VIES):
    vies = NOMBRE_VIES - i
    print("Il vous reste", vies, "vies.")
    nombre = demander_nombre_magique(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné !")
        gagne = True
        break
    elif nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand.")
        
    else:
        print("Le nombre magique est plus petit.")
        
if not gagne:
    print("Vous avez perdu! le nombre magique était:", NOMBRE_MAGIQUE)

