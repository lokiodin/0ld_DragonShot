# Créé par Lokiodin, le 24/03/2016 en Python 3.2


import pygame
from pygame.locals import *

pygame.init()

#Constantes

    #Var
nombre_sprite_cote = 20
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite


    #Constantes de la boucle du jeu entier
choix = ''
continuer = 1
continuer_acceuil = 1
continuer_jeu = 0
continuer_fin = 0
continuer_GA = 0
continuer_expl = 0

    #Liste
lst_map = ['./map/n1.txt', './map/n22.txt', './map/n3.txt', './map/n4.txt']

lst_coeur = [1, 1, 1, 1, 1]


sprite_arrivee = (0, 0)
xpos_dresseur = 0
speed_proj = 2 #Plus ce nombre est petit plus le projectile iras vite
                #Limite de lag : speed_proj <= 50
    #Son
pygame.mixer.music.load("./son/10 - Kanar _ Bolt - Sortir du Sol.wav")
sontape_mur = pygame.mixer.Sound("./son/Tape un mur.wav")
sonwin = pygame.mixer.Sound("./son/Win.wav")
sonlancer = pygame.mixer.Sound("./son/son lancer.wav")
sonteleport = pygame.mixer.Sound("./son/son teleportation.wav")
sonGA = pygame.mixer.Sound("./son/son GA.wav")