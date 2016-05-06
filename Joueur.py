from fonctions import *

class Cheval():
    Case=0
    Couleur="Rouge"
    EnJeu = False
    Numero = 0
    Depart=[]
    ListeMaison=[]
    PlateauAdresse=[]
    CheminMaison=[]
    CaseMaison = 0


    def initPlateau(self):
        self.Depart.append(5)
        self.Depart.append(22)
        self.Depart.append(39)
        self.Depart.append(56)

        self.ListeMaison.append(68)
        self.ListeMaison.append(17)
        self.ListeMaison.append(34)
        self.ListeMaison.append(51)

        self.PlateauAdresse.append([250,250])
        self.PlateauAdresse.append([304,483])
        self.PlateauAdresse.append([304,462])
        self.PlateauAdresse.append([304,443])
        self.PlateauAdresse.append([304,417])
        self.PlateauAdresse.append([304,390])
        self.PlateauAdresse.append([304,376])
        self.PlateauAdresse.append([304,352])
        self.PlateauAdresse.append([304,325])
        self.PlateauAdresse.append([330,306])
        self.PlateauAdresse.append([351,309])
        self.PlateauAdresse.append([372,309])
        self.PlateauAdresse.append([393,309])
        self.PlateauAdresse.append([418,309])
        self.PlateauAdresse.append([439,309])
        self.PlateauAdresse.append([462,309])
        self.PlateauAdresse.append([484,309])
        self.PlateauAdresse.append([484,250])
        self.PlateauAdresse.append([484,185])
        self.PlateauAdresse.append([467,186])
        self.PlateauAdresse.append([440,186])
        self.PlateauAdresse.append([412,186])
        self.PlateauAdresse.append([397,186])
        self.PlateauAdresse.append([370,186])
        self.PlateauAdresse.append([352,186])
        self.PlateauAdresse.append([330,186])
        self.PlateauAdresse.append([302,168])
        self.PlateauAdresse.append([302,142])
        self.PlateauAdresse.append([302,122])
        self.PlateauAdresse.append([302,99])
        self.PlateauAdresse.append([302,77])
        self.PlateauAdresse.append([302,54])
        self.PlateauAdresse.append([302,32])
        self.PlateauAdresse.append([302,9])
        self.PlateauAdresse.append([250,9])
        self.PlateauAdresse.append([185,9])
        self.PlateauAdresse.append([185,32])
        self.PlateauAdresse.append([185,54])
        self.PlateauAdresse.append([185,78])
        self.PlateauAdresse.append([185,97])
        self.PlateauAdresse.append([185,120])
        self.PlateauAdresse.append([185,144])
        self.PlateauAdresse.append([185,168])
        self.PlateauAdresse.append([169,186])
        self.PlateauAdresse.append([145,186])
        self.PlateauAdresse.append([123,186])
        self.PlateauAdresse.append([100,186])
        self.PlateauAdresse.append([78,186])
        self.PlateauAdresse.append([52,186])
        self.PlateauAdresse.append([34,186])
        self.PlateauAdresse.append([8,186])
        self.PlateauAdresse.append([8,247])
        self.PlateauAdresse.append([8,309])
        self.PlateauAdresse.append([34,309])
        self.PlateauAdresse.append([55,309])
        self.PlateauAdresse.append([77,309])
        self.PlateauAdresse.append([100,309])
        self.PlateauAdresse.append([123,309])
        self.PlateauAdresse.append([145,309])
        self.PlateauAdresse.append([169,309])
        self.PlateauAdresse.append([188,330])
        self.PlateauAdresse.append([188,352])
        self.PlateauAdresse.append([188,375])
        self.PlateauAdresse.append([188,397])
        self.PlateauAdresse.append([188,419])
        self.PlateauAdresse.append([188,442])
        self.PlateauAdresse.append([188,465])
        self.PlateauAdresse.append([188,485])
        self.PlateauAdresse.append([250,485])




    def __init__(self, Couleur, Numero):
        self.Couleur = Couleur
        self.initPlateau()
        self.Numero = Numero

    def sortir(self):
        self.EnJeu=True
        if self.Couleur=='Jaune':
            self.Case = self.Depart[0]
        elif self.Couleur=='Bleu':
            self.Case = self.Depart[1]
        elif self.Couleur=='Rouge':
            self.Case = self.Depart[2]
        elif self.Couleur=='Vert':
            self.Case = self.Depart[3]
        print ("Le cheval est sorti sur la case ", self.Case)
        return

    def adresse(self):
        if self.EnJeu == False:
            if self.Couleur == "Jaune":
                return([425,425])
            elif self.Couleur == "Rouge":
                return([80,80])
            elif self.Couleur == "Vert":
                return([80,425])
            elif self.Couleur == "Bleu":
                return([425,80])
        return (self.PlateauAdresse[self.Case])

    def mouvementpossible(self, nbDe):
        return True
#entrée: la valeur du dé
#Sauve: la valeur de la case d'arrivée
    def deplacer(self, nbDe):
        self.Case += nbDe
        if (self.Case > 68) :
            self.Case -= 68
        return

    def EstIlGagnant(self):
        if self.CheminMaison and self.CaseMaison == 8 :
            self.Arrive = True
            return True
        return False


    def EntrerCheminMaison(self):
        print("Cheval Sur Chemin Maison")
        self.Case = 0
        self.CaseMaison = 8
        self.CheminMaison = True
        return

    def AEntrerCheminMaison(self):
        if ((self.Couleur=='Jaune' and self.Case == self.ListeMaison[0])
            or (self.Couleur=='Bleu' and self.Case == self.ListeMaison[1])
            or (self.Couleur=='Rouge' and self.Case == self.ListeMaison[2])
            or (self.Couleur=='Vert' and self.Case == self.ListeMaison[3])) :
            self.EntrerCheminMaison()
        return

    def mourir(self):
        self.Case=0
        self.EnJeu=False
        return


class Joueur():
    Humain=False
    Nom=""
    Numero=1
    Couleur=""
    Points=0
    ChevauxEcurie=4

    def __init__(self, Couleur):
        self.Cheval1 = Cheval(Couleur, 1)
        self.Cheval2 = Cheval(Couleur, 2)
        self.Cheval3 = Cheval(Couleur,3)
        self.Cheval4 = Cheval(Couleur,4)
        self.Couleur = Couleur

    def sortirCheval(self):
        if self.Cheval1.EnJeu== False:
            self.Cheval1.sortir()
        elif self.Cheval2.EnJeu== False:
            self.Cheval2.sortir()
        elif self.Cheval3.EnJeu== False:
            self.Cheval3.sortir()
        elif self.Cheval4.EnJeu== False:
            self.Cheval4.sortir()
        self.ChevauxEcurie -= 1
        return

    def tourOrdi(self):
        import random
        de = NbduDe(jeu.maxide1)
        print(self.Nom , "L'ordi avez fait : " , de , "\n")
        if de == jeu.maxide and self.ChevauxEcurie != 0:
            sortie = random.randint(0,1)
            if sortie :
                self.sortirCheval()
                return False
            else :
                print("Vous n'avez pas fait sortir de cheval\n")
        if self.ChevauxEcurie == 4 :
            print("L'ordi n'a pas de chevaux dehors.\nFin du tour.\n")
            return False
        deplacer = random.randint(1,4)
        print("L'ordi veut deplacer le cheval " , deplacer , "\nFin du tour.\n")
        if deplacer == 1:
            if self.Cheval1.mouvementpossible(de):
                self.Cheval1.deplacer(de)
        if deplacer == 2:
            if self.Cheval2.mouvementpossible(de):
                self.Cheval2.deplacer(de)
        if deplacer == 3:
            if self.Cheval3.mouvementpossible(de):
                self.Cheval3.deplacer(de)
        if deplacer == 4:
            if self.Cheval4.mouvementpossible(de):
                self.Cheval4.deplacer(de)

        if self.Cheval1.EstIlGagnant() :
            self.Points += 1
        if self.Cheval2.EstIlGagnant() :
            self.Points += 1
        if self.Cheval3.EstIlGagnant() :
            self.Points += 1
        if self.Cheval4.EstIlGagnant() :
            self.Points += 1

        if self.Points == 4 :
            print("BRAVO ! ", self.Nom, "L'ordi a gagné !\nFin de la partie")
            return True

        return False

    def tour(self):
        global jeu
        if (self.Humain == False):
            return self.tourOrdi()
        else:
            de = NbduDe(jeu.maxide)
            print(self.Nom , "Vous avez fait : " , de , "\n")
            if de == jeu.maxide and self.ChevauxEcurie != 0:
                sortie = obtenirOuiNon('Voulez-vous sortir un cheval?\n')
                if sortie :
                    self.sortirCheval()
                    return False
                else :
                    print("Vous n'avez pas fait sortir de cheval\n")
            if self.ChevauxEcurie == 4 :
                print("Vous n'avez pas de chevaux dehors.\nFin du tour.\n")
                return False
            deplacer = obtenirInt('Quel cheval voulez-vous deplacer?\n')
            if deplacer == 1:
                if self.Cheval1.mouvementpossible(de):
                    self.Cheval1.deplacer(de)
            if deplacer == 2:
                if self.Cheval2.mouvementpossible(de):
                    self.Cheval2.deplacer(de)
            if deplacer == 3:
                if self.Cheval3.mouvementpossible(de):
                    self.Cheval3.deplacer(de)
            if deplacer == 4:
                if self.Cheval4.mouvementpossible(de):
                    self.Cheval4.deplacer(de)

            if self.Cheval1.EstIlGagnant() :
                self.Points += 1
            if self.Cheval2.EstIlGagnant() :
                self.Points += 1
            if self.Cheval3.EstIlGagnant() :
                self.Points += 1
            if self.Cheval4.EstIlGagnant() :
                self.Points += 1

            if self.Points == 4 :
                print("BRAVO ! ", self.Nom, "Vous avez gagne !\nFin de la partie")
                return True
            return False
        return False


