#!/usr/bin/python
# coding: utf-8

from Joueur import Joueur

import pygame
from pygame.locals import *
from fonctions import *

# Fonction Principal

def main():
    # Gestion des globales

    global Jeu
    # Reglage des parametres
    menu()

    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Programme Pygame de base')

    # Remplissage de l'arrière-plan
    jeu.background_position = [0, 0]
    jeu.background_image = pygame.image.load("background.png")

    # Definition des images des petits chevaux
    jeu.ImageChevalRouge = pygame.image.load("ChevalRouge.png")
    jeu.ImageChevalBleu = pygame.image.load("ChevalBleu.png")
    jeu.ImageChevalVert = pygame.image.load("ChevalVert.png")
    jeu.ImageChevalJaune = pygame.image.load("ChevalJaune.png")

    # Remplir le plateau
    jeu.plateau = []
    for i in range (1,69):
        jeu.plateau.append(str (i))
    jeu.securite=[11,16,28,33,45,50,62,67]
    jeu.depart=[5,22,39,56]


    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        #Bloucle De jeu
        afficher(screen)
        if jeu.j1.debutTour(0) :
            return
        afficher(screen)
        if jeu.j2.debutTour(0) :
            return
        afficher(screen)
        if jeu.j3.debutTour(0) :
            return
        afficher(screen)
        if jeu.j4.debutTour(0) :
            return

#plateau et pions affiches
def afficher(screen):
    # Affichage du Background
    global jeu
    screen.blit(jeu.background_image, jeu.background_position)

    screen.blit(jeu.ImageChevalJaune, jeu.j1.Cheval1.adresse())
    screen.blit(jeu.ImageChevalJaune, jeu.j1.Cheval2.adresse())
    screen.blit(jeu.ImageChevalJaune, jeu.j1.Cheval3.adresse())
    screen.blit(jeu.ImageChevalJaune, jeu.j1.Cheval4.adresse())
    screen.blit(jeu.ImageChevalRouge, jeu.j2.Cheval1.adresse())
    screen.blit(jeu.ImageChevalRouge, jeu.j2.Cheval2.adresse())
    screen.blit(jeu.ImageChevalRouge, jeu.j2.Cheval3.adresse())
    screen.blit(jeu.ImageChevalRouge, jeu.j2.Cheval4.adresse())
    screen.blit(jeu.ImageChevalVert, jeu.j3.Cheval1.adresse())
    screen.blit(jeu.ImageChevalVert, jeu.j3.Cheval2.adresse())
    screen.blit(jeu.ImageChevalVert, jeu.j3.Cheval3.adresse())
    screen.blit(jeu.ImageChevalVert, jeu.j3.Cheval4.adresse())
    screen.blit(jeu.ImageChevalBleu, jeu.j4.Cheval1.adresse())
    screen.blit(jeu.ImageChevalBleu, jeu.j4.Cheval2.adresse())
    screen.blit(jeu.ImageChevalBleu, jeu.j4.Cheval3.adresse())
    screen.blit(jeu.ImageChevalBleu, jeu.j4.Cheval4.adresse())


    pygame.display.flip()

def menu():
    print ("Bienvenue au jeu des petits chevaux espagnols!!!\n")

    #Creation des objets joueurs
    global jeu
    jeu.j1 = Joueur("Jaune")
    jeu.j2 = Joueur("Rouge")
    jeu.j3 = Joueur("Vert")
    jeu.j4 = Joueur("Bleu")

    combienDeJoueur = obtenirInt("Combien de personnes êtes vous? (entre 1 et 4)\n")
    while (combienDeJoueur >= 5 or combienDeJoueur <= 0):
        combienDeJoueur = obtenirInt("NON! Le nombre de joueur possible est compris entre 1 et 4\n")
    if (combienDeJoueur==1):
        print ("il y aura 3 autres participants virtuels.")
        jeu.j1.Nom = input("Comment vous appellez-vous?\n")
        jeu.j1.Humain = True
        print ("bonjour",jeu.j1.Nom,"!\nVous etes le joueur Jaune\n")
    elif (combienDeJoueur==2):
        print ("Il y aura deux autres jouers virtuels.")
        jeu.j1.Nom=input("J1 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j1.Nom,"!")
        jeu.j1.Humain = True
        jeu.j2.Nom=input("J2 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j2.Nom,"!")
        jeu.j2.Humain = True
    elif (combienDeJoueur==3):
        print ("Il y aura un autres joueurs virtuels.")
        jeu.j1.Nom=input("J1 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j1.Nom,"!")
        jeu.j1.Humain = True
        jeu.j2.Nom=input("J2 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j2.Nom,"!")
        jeu.j2.Humain = True
        jeu.j3.Nom= input("J3 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j3.Nom,"!")
        jeu.j3.Humain=True
    elif (combienDeJoueur==4):
        print ("Il n'y aura pas de joueurs virtuel")
        jeu.j1.Nom=input("J1 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j1.Nom,"!")
        jeu.j1.Humain = True
        jeu.j2.Nom=input("J2 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j2.Nom,"!")
        jeu.j2.Humain = True
        jeu.j3.Nom=input("J3 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j3.Nom,"!")
        jeu.j3.Humain = True
        jeu.j4.Nom=input("J4 Comment vous appellez-vous?\n")
        print ("bonjour",jeu.j4.Nom,"!")
        jeu.j4.Humain = True

    jeu.maxide = obtenirInt("Combien de faces le de a-t-il? La valeur possible est compris entre 6 et 12\n")
    print ("Le dé ira jusqu'a",jeu.maxide)
    while (jeu.maxide > 12 or jeu.maxide < 6):
        jeu.maxide = obtenirInt("NON! La valeur possible est compris entre 6 et 12\n")
        print ("Le dé ira jusqu'a",jeu.maxide)

if __name__ == '__main__': main()