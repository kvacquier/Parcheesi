def init():
    global jeu
    jeu = Jeu()

class Jeu(object):
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
    pass