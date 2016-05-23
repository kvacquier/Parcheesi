class Jeu:
    plateau=[]
    securite=[]
    depart=[]
    j1 = None
    j2 = None
    j3 = None
    j4 = None
    maxide=0
    ImageChevalJaune = None
    ImageChevalRouge = None
    ImageChevalBleu = None
    ImageChevalVert = None
    background_position = None
    background_image = None

jeu = Jeu

#entrée: la valeur maximum du dé
#sortie: la valeur au hasard donnée par le dé
def NbduDe(maxi):
    import random
    de=random.randint(1,maxi)
    return(de)


#entrée: la valeur du dé, donc d'avancement du cheval et sa case de départ
#sortie: la valeur de la case d'arrivée
def CaseDarrivee(de,case):
    case=case+de
    return(case)


#entrée:la valeur du dé
#sortie:la valeur de la case d'arrivée
#fonction à utiliser uniquement au point de départ
def PremierDepart(de,case,maxi):
    if de==maxi:
        case=1
    elif de!=maxi:
        case=0

#Retourne la postion sur la carte en fonction de la case
def position_cheval(case):
    return([10,10])

#entrée:le texte a afficher pour demander au joueur un chiffre
#sortie:la valeur du chiffre
#fonction à utiliser quand on demande un chiffre aux joueurs
def obtenirInt(question):
    resultat = None
    while resultat == None:
        entree = input(question)
        try:
            resultat = int(entree)
        except ValueError:
            print("Entrez un nombre SVP.")
            resultat = None
    return resultat

#entrée:le texte a afficher pour demander au joueur un oui ou non
#sortie:true = oui - false = non
#fonction à utiliser quand on demande un oui/non aux joueurs
def obtenirOuiNon(question):
    resultat = None
    while resultat == None:
        entree = input(question)
        if entree == "oui":
            resultat = True
        elif entree == "non" :
            resultat = False
        else:
            print("Entrez oui ou non SVP.")
            resultat = None
    return resultat