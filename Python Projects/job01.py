import random

# création une liste
mots = []

with open("./dico_france.txt") as fl :
    for l in fl :
        mots.append(l.rstrip("\n"))
word = random.choice(mots) # pour prendre un élément au hasard dans la liste
# crations les variables clé
lettres = []
faux = 0
trouve = False
vies = {"debutant": 10, "intermediare": 7, "expert": 4}


mot_cacher = ""

# print("word => ", word)
niveau = input("Bonjour, à quel niveau souhaites tu jouer ? ")
vie_restant = vies[niveau]






def prendMotCacher(lettres, word):
    """
    La fonction qui print un mot cacher avec la `lettre` et `word` donnés
    """

    liste = ["_" for l in word]

    for i in range(len(word)):
        liste[i] = word[i] if (word[i] in lettres) else "_"

    mot_cacher = " ".join(liste) # "_ _ d _ _"
    
    return mot_cacher



# Commence le jeux
while not trouve :
    print("Nombre de vie(s) restante(s) : " + str(vie_restant))

    # Si le joueur n'est pas un expert...
    if niveau != "expert":
        # ...affiche la liste des lettre proposée
        print("Lettre proposées : " + " ".join(lettres))

    mot_cacher = prendMotCacher(lettres, word)

    print(mot_cacher)

    lettre_choisi = input(" Quelle lettre proposes tu ? ")
    
    # liste_mot_cacher = mot_cacher.strip().split(" ")

    # Si la lettre proposée ou choisi ce trouve dans le mot `word`...
    if lettre_choisi in word:
        # ...ajoute la lettre choise dans la liste de `lettres`
        lettres.append(lettre_choisi)
        # prend le mot cacher encore
        mot_cacher = prendMotCacher(lettres, word)

        mot_cacher_coller = mot_cacher.replace(" ", "")

        # [Hajar]: affiche moi le probleme
        # print("mot_cacher_coller => %s & word => %s" % (mot_cacher_coller, word))

        # Si le `mot_cacher` est égale à `word`...
        if mot_cacher_coller == word:
            # ... Le joueur à gagner, informe le :)
            print("Felicitation!!! Tu a gagné !!!")
            # on arrête le jeux en attribuant `True` à `trouve`
            trouve = True

    else:
        # Sinon...
        # Le joueur perd une vie
        vie_restant -= 1
        # ajoute la lettre choise dans la liste de `lettres`
        lettres.append(lettre_choisi)

        # Si le joueur n'a plus de vie...
        if vie_restant == 0:
            # ...la partie prend fin, alors informe le :)
            print("Désolé, tu as perdu !!")
            print("Le mot était ", word)

            break # <- pour arrêter ce boucle `while` 

