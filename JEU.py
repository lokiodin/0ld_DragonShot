#V5 ---> V4 + changement de sprite entre map + explications
#Jeu
#Le J1 est le perso qui doit finir le labyrinthe, variable utilisée pour lui: perso
#Le J2 est le perso qui doit tirer sur le J1, variable utilisée: dresseur

import pygame
from pygame.locals import *
from constantes import*



pygame.init()

#Ouverture de la fenetre pygame
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre + 30))

pygame.display.set_caption("DragonShot")



"""---------------------LOAD DES JOUEURS/OBJETS----------------------"""

#Load perso
perso = pygame.image.load("./images/dragon/dragonface.png").convert_alpha()
position_perso = perso.get_rect()

#Load image par defaut      Coordonnées par defaut : <rect(0,0,30,30)>
imgdef = pygame.image.load("./images/dragon/dragonface.png").convert_alpha()
position_imgdef = imgdef.get_rect()

#Load dresseur
dresseur  = pygame.image.load("./images/dresseur/dresseur 19_232.png")
position_dresseur = dresseur.get_rect()

#Load balle du dresseur
balle = pygame.image.load("./images/ballepokemon2.png")
position_balle = balle.get_rect()

#Load d'un coeur
coeur = pygame.image.load("./images/coeur.png")

"""---------------------FIN LOAD DES JOUEURS/OBJETS----------------------"""


#son
#voir constantes.py


""" -------------------------------DEF------------------------------------"""

#Definit la map apres win
def ni(position_perso, sprite_arrivee, position_dresseur, xpos_dresseur, lst_map, continuer_fin, continuer_acceuil, continuer_jeu, continuer_GA, choix, iindice):
    if position_perso[0] == sprite_arrivee[0] and position_perso[1] == sprite_arrivee[1]:
        if iindice < 3:
            sonteleport.play()
            choix = lst_map[iindice + 1]
            position_perso = position_perso.move(-sprite_arrivee[0], -sprite_arrivee[1])
            position_dresseur = position_dresseur.move(-300, -600)
            iindice += 1
            continuer_fin = 0
            continuer_jeu = 0
            continuer_acceuil = 0
        else:
            continuer_jeu = 0
            continuer_fin = 1
            continuer_GA = 0
    return continuer_fin, continuer_acceuil, continuer_jeu, continuer_GA, position_perso, position_dresseur, choix, iindice

#affiche les coeur
def coeur_affiche():
    xposvie = 450
    nbvie = len(lst_coeur)
    for qqc in range(nbvie):
        fenetre.blit(coeur, (xposvie + 30 * (qqc - 1), 0))
        pygame.display.flip()

#Calcul le nombre de point de vie restant et GAME OVER si 0 hp
def hp_cal(lst_coeur, continuer_jeu, continuer_GA):
    if len(lst_coeur) == 0:     #Si il reste 0 hp
        continuer_jeu = 0
        continuer_GA = 1
        continuer_fin = 0
    return continuer_jeu, continuer_GA

#Charge les images de la map1
def cmap1():
    arrivee = pygame.image.load("./images/map1/arrivee.png")
    depart = pygame.image.load("./images/map1/depart.png")
    mur = pygame.image.load("./images/map1/mur.png")
    cheminperso = pygame.image.load("./images/map1/cheminperso.png")
    chemindresseur = pygame.image.load("./images/map1/chemindresseur.png")
    explo_balle = pygame.image.load("./images/map1/explo.png")
    return arrivee, depart, mur, cheminperso, chemindresseur, explo_balle

#Charge les images de la map2
def cmap2():
    arrivee = pygame.image.load("./images/map2/arrivee.png")
    depart = pygame.image.load("./images/map2/depart.png")
    mur = pygame.image.load("./images/map2/mur.png")
    cheminperso = pygame.image.load("./images/map2/cheminperso.png")
    chemindresseur = pygame.image.load("./images/map2/chemindresseur.png")
    explo_balle = pygame.image.load("./images/map2/explo.png")
    return arrivee, depart, mur, cheminperso, chemindresseur, explo_balle

#Charge les images de la map3
def cmap3():
    arrivee = pygame.image.load("./images/map3/arrivee.png")
    depart = pygame.image.load("./images/map3/depart.png")
    mur = pygame.image.load("./images/map3/mur.png")
    cheminperso = pygame.image.load("./images/map3/cheminperso.png")
    chemindresseur = pygame.image.load("./images/map3/chemindresseur.png")
    explo_balle = pygame.image.load("./images/map3/explo.png")
    return arrivee, depart, mur, cheminperso, chemindresseur, explo_balle

#Charge les images de la map4
def cmap4():
    arrivee = pygame.image.load("./images/map4/arrivee.png")
    depart = pygame.image.load("./images/map4/depart.png")
    mur = pygame.image.load("./images/map4/mur.png")
    cheminperso = pygame.image.load("./images/map4/cheminperso.png")
    chemindresseur = pygame.image.load("./images/map4/chemindresseur.png")
    explo_balle = pygame.image.load("./images/map4/explo.png")
    return arrivee, depart, mur, cheminperso, chemindresseur, explo_balle

#Choix des sprites en fonction des niveaux
def choix_sprite_niveau(choix):
    if choix == lst_map[0]:
        arrivee, depart, mur, cheminperso, chemindresseur, explo_balle = cmap1()
    elif choix == lst_map[1]:
        arrivee, depart, mur, cheminperso, chemindresseur, explo_balle = cmap2()
    elif choix == lst_map[2]:
        arrivee, depart, mur, cheminperso, chemindresseur, explo_balle = cmap3()
    elif choix == lst_map[3]:
        arrivee, depart, mur, cheminperso, chemindresseur, explo_balle = cmap4()
    return arrivee, depart, mur, cheminperso, chemindresseur, explo_balle

#affiche le niveau
def affiche(choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle):
    structure = []              #structure du niveau
    with open(choix) as fic:
        iligne = 0
        for ligne in fic:
            icolonne = 0
            for sprite in ligne:
                x = icolonne * taille_sprite
                y = iligne * taille_sprite
                if sprite == 'd':
                    fenetre.blit(depart, (x, y))
                elif sprite == 'm':
                    fenetre.blit(mur, (x, y))
                elif sprite == '0':
                    fenetre.blit(cheminperso, (x,y))
                elif sprite == 'a':
                    sprite_arrivee = (x, y)
                    fenetre.blit(arrivee, (x, y))
                elif sprite == 'c':
                    fenetre.blit(chemindresseur, (x, y))
                icolonne += 1


            structure.append(ligne)
            iligne += 1
    return structure, sprite_arrivee

#Mouvement J1
def J1_mouv(direc, position_perso):
    if direc == 'droite':                       # Droite
        if structure[int(ligney)][int(colonnex) + 1] == 'a':
            position_perso = position_perso.move(30, 0)
            fenetre.blit(perso, position_perso)
        elif structure[int(ligney)][int(colonnex) + 1] != 'm':
            position_perso = position_perso.move(30, 0)
            fenetre.blit(perso, position_perso)
        #else:
         #   sontape_mur.play()
    elif direc == 'gauche':                     # Gauche
        if structure[int(ligney)][int(colonnex) - 1] == 'a':
            position_perso = position_perso.move(-30, 0)
            fenetre.blit(perso, position_perso)
        elif structure[int(ligney)][int(colonnex) - 1] != 'm':
            position_perso = position_perso.move(-30, 0)
            fenetre.blit(perso, position_perso)
        #else:
         #   sontape_mur.play()
    elif direc == 'bas':                        # Bas
        if structure[int(ligney) + 1][int(colonnex)] == 'a':
            position_perso = position_perso.move(0, 30)
            fenetre.blit(perso, position_perso)
        elif structure[int(ligney) + 1][int(colonnex)] != 'm':
            position_perso = position_perso.move(0, 30)
            fenetre.blit(perso, position_perso)
        #else:
         #   sontape_mur.play()
    elif direc == 'haut':                       # Haut
        if structure[int(ligney) - 1][int(colonnex)] == 'a':
            position_perso = position_perso.move(0, -30)
            fenetre.blit(perso, position_perso)
        elif structure[int(ligney) - 1][int(colonnex)] != 'm':
            position_perso = position_perso.move(0, -30)
            fenetre.blit(perso, position_perso)
        #else:
         #   sontape_mur.play()

    return position_perso

#Mouvement du J2
def J2_mouv(direc, position_dresseur, xpos_dresseur):
    if direc == 'droite':                       # Droite
        xpos_dresseur += 15
        position_dresseur = position_dresseur.move(15, 0)
    elif direc == 'gauche':                     # Gauche
        xpos_dresseur -= 15
        position_dresseur = position_dresseur.move(-15, 0)

    return position_dresseur, xpos_dresseur

#lancer la balle
def obus(position_balle, position_dresseur, speed_proj, continuer_jeu, continuer_GA, balle, lst_coeur):
    lan = 1
    sonlancer.play()
    pygame.time.delay(200)
    position_balle[0] = position_dresseur[0]
    position_balle[1] = position_dresseur[1]
    while lan != 0:
        if ((position_balle[0] == position_perso[0]) and (position_balle[1] == position_perso[1])): #si la balle touche le perso alors
            balle = pygame.image.load("./images/explo.png")                                         #la balle s'arrete
            fenetre.blit(balle, position_balle)
            pygame.display.flip()                   #et le J1 perd, la boucle jeu prend fin
            continuer_jeu, continuer_GA = hp_cal(lst_coeur, continuer_jeu, continuer_GA)
            lst_coeur.pop()                                        #perd 1 hp
            pygame.time.delay(20)
            print("Touché !!!!")
            balle = pygame.image.load("./images/ballepokemon2.png")
            lan = 0
        elif position_balle[1] == 0:            #la balle dépasse le cadre du jeu alors la balle disparait
           lan = 0
        elif ((position_balle[0] != position_perso[0]) and (position_balle[1] != position_perso[1])) or position_balle[1] > 0:
            structure, sprite_arrivee = affiche(choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle)                                           #Si la balle ne subit aucun evenement alors
            fenetre.blit(perso, position_perso)                                     #elle continue son mouvement
            fenetre.blit(dresseur, position_dresseur)
            position_balle = position_balle.move(0, -10)    #déplacer la balle
            fenetre.blit(balle, position_balle)     #dessiner une nouvelle balle
            pygame.display.update()                 #afficher le tout
            pygame.time.delay(speed_proj)


    return position_balle, position_dresseur, continuer_jeu, continuer_GA, balle, lst_coeur

#Mise à niveau de la map
def m_a_n(position_dresseur, position_perso, position_balle, choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle):
    pygame.mixer.music.play()           #Music play
    structure, sprite_arrivee = affiche(choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle)          #Affiche la map

    #Affichage des joueurs
    fenetre.blit(dresseur, position_dresseur)
    fenetre.blit(balle, position_balle)
    #Positionnement des joueurs
    position_perso = position_perso.move(30, 30)
    position_dresseur = position_dresseur.move(300, 600)

    pygame.display.flip()
    return position_dresseur, position_perso, structure, sprite_arrivee

"""------------------------------FINDEF-----------------------------------"""



#BOUCLE INFINIE
while continuer == 1:

    while continuer_acceuil == 1:       #Boucle d'acceuil
        #Load fond
        fond = pygame.image.load("./images/fond qui pete2.png").convert()
        fenetre.blit(fond, (0,0))

        #On met les coordonnées des joueurs à celle de defaut
        position_dresseur = position_imgdef
        position_perso = position_imgdef

        lst_coeur = [1, 1, 1, 1, 1] #On remet à la valeur par defaut pour les vies

        pygame.display.flip()
        continuer_acceuil = 1
        continuer_jeu = 0

        for event in pygame.event.get():
            if event.type == QUIT:          #Evenement = Quitter
                pygame.mixer.music.stop()   #On stoppe toutes les boucles
                continuer = 0
                continuer_acceuil = 0
                continuer_jeu = 0
                continuer_fin = 0
                continuer_GA = 0
            iindice = 0
            if event.type == KEYDOWN:       #Evenement = F1/F2/F3/F4 --> choix du niveau
                if event.key == K_F1:
                    continuer_acceuil = 0
                    continuer_jeu = 1
                    choix = lst_map[iindice]
                elif event.key == K_F2:
                    iindice = 1
                    continuer_acceuil = 0
                    continuer_jeu = 1
                    choix = lst_map[iindice]
                elif event.key == K_F3:
                    iindice = 2
                    continuer_acceuil = 0
                    continuer_jeu = 1
                    choix = lst_map[iindice]
                elif event.key == K_F4:
                    iindice = 3
                    continuer_acceuil = 0
                    continuer_jeu = 1
                    choix = lst_map[iindice]
                elif event.key == K_RETURN:
                    continuer_fin = 0
                    continuer_acceuil = 1
                    continuer_expl = 1



        while continuer_expl == 1:
            #Load fond
            fond = pygame.image.load("./images/explic.png").convert()
            fenetre.blit(fond, (0,0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:          #Evenement = Quitter
                    pygame.mixer.music.stop()   #On stoppe toutes les boucles
                    continuer = 0
                    continuer_acceuil = 0
                    continuer_jeu = 0
                    continuer_fin = 0
                    continuer_GA = 0
                    continuer_expl = 0
                iindice = 0
                if event.type == KEYDOWN:       #Evenement = F1/F2/F3/F4 --> choix du niveau
                    if event.key == K_F1:
                        iindice = 0
                        continuer_acceuil = 0
                        continuer_jeu = 1
                        continuer_expl = 0
                        choix = lst_map[iindice]
                    elif event.key == K_F2:
                        iindice = 1
                        continuer_acceuil = 0
                        continuer_jeu = 1
                        continuer_expl = 0
                        choix = lst_map[iindice]
                    elif event.key == K_F3:
                        iindice = 2
                        continuer_acceuil = 0
                        continuer_jeu = 1
                        continuer_expl = 0
                        choix = lst_map[iindice]
                    elif event.key == K_F4:
                        iindice = 3
                        continuer_acceuil = 0
                        continuer_jeu = 1
                        continuer_expl = 0
                        choix = lst_map[iindice]
                    elif event.key == K_RETURN:
                        iindice = 0
                        continuer_fin = 0
                        continuer_acceuil = 0
                        continuer_expl = 0
                        continuer_jeu = 1
                        choix = lst_map[iindice]




    if choix == lst_map[0] or choix == lst_map[1] or choix == lst_map[2] or choix == lst_map[3]:
        arrivee, depart, mur, cheminperso, chemindresseur, explo_balle = choix_sprite_niveau(choix)
        position_dresseur, position_perso, structure, sprite_arrivee = m_a_n(position_dresseur, position_perso, position_balle, choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle)
        continuer_fin = 1
        continuer_jeu = 1


    while continuer_jeu == 1:               #Boucle de jeu
        continuer_fin = 1
        for event in pygame.event.get():
        #Attente des événements
            if event.type == QUIT:          #Evenement = Quitter
                pygame.mixer.music.stop()
                continuer = 0
                continuer_acceuil = 0
                continuer_jeu = 0
                continuer_fin = 0
                continuer_GA = 0

            ligney = position_perso[1]/30
            colonnex = position_perso[0]/30

            if event.type == KEYDOWN:       #Evenement = Touches appuyées:
                if event.key == K_DOWN:                 #Bas
                    position_perso = J1_mouv('bas', position_perso)
                if event.key == K_UP:                   #J1 Haut
                    position_perso = J1_mouv('haut', position_perso)
                if event.key == K_RIGHT:                #J1 Droite
                    position_perso = J1_mouv('droite', position_perso)
                if event.key == K_LEFT:                 #J1 Gauche
                    position_perso = J1_mouv('gauche', position_perso)

                if event.key == K_d:                    #J2 DROITE
                    position_dresseur, xpos_dresseur = J2_mouv('droite', position_dresseur, xpos_dresseur)
                if event.key == K_a:                    #J2 GAUCHE
                    position_dresseur, xpos_dresseur = J2_mouv('gauche', position_dresseur, xpos_dresseur)
                if event.key == K_SPACE:                #Lancer une balle du J2
                        position_balle, position_dresseur, continuer_jeu, continuer_GA, balle, lst_coeur = obus(position_balle, position_dresseur, speed_proj, continuer_jeu, continuer_GA, balle, lst_coeur)
                #les vies
                if event.key == K_2:
                    lst_coeur.pop()
                if event.key == K_5:
                    lst_coeur.append(1)

        continuer_fin, continuer_acceuil, continuer_jeu, continuer_GA, position_perso, position_dresseur, choix, iindice = ni(position_perso, sprite_arrivee, position_dresseur, xpos_dresseur, lst_map, continuer_fin, continuer_acceuil, continuer_jeu, continuer_GA, choix, iindice)
        coeur_affiche()
        continuer_jeu, continuer_GA = hp_cal(lst_coeur, continuer_jeu, continuer_GA)

        fenetre.blit(fond, (0,0))
        affiche(choix, arrivee, depart, mur, cheminperso, chemindresseur, explo_balle)
        fenetre.blit(perso, position_perso)
        fenetre.blit(dresseur, position_dresseur)
    	#Rafraichissement
        pygame.display.flip()

    if continuer_GA == 1:
        pygame.mixer.music.stop()
        sonGA.play()

    while continuer_GA == 1:
        for event in pygame.event.get():
            if event.type == QUIT:          #Evenement = Quitter
                pygame.mixer.music.stop()
                continuer = 0               #Mise à 0 des boucles
                continuer_acceuil = 0
                continuer_jeu = 0
                continuer_fin = 0
                continuer_GA = 0
                choix = ''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    lst_coeur = [1, 1, 1, 1, 1]
                    continuer_fin = 0
                    continuer_GA = 0
                    continuer_acceuil = 1
                    continuer_jeu = 1
        #Load fond
        fond = pygame.image.load("./images/GameOver.png").convert()
        fenetre.blit(fond, (0,0))
        pygame.display.flip()

    while continuer_fin == 1:               #Boucle de fin
        for event in pygame.event.get():
            if event.type == QUIT:          #Evenement = Quitter
                pygame.mixer.music.stop()
                continuer = 0               #Mise à 0 des boucles
                continuer_acceuil = 0
                continuer_jeu = 0
                continuer_fin = 0
                continuer_GA = 0
                choix = ''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    lst_coeur = [1, 1, 1, 1, 1]
                    continuer_fin = 0
                    continuer_acceuil = 1
                    continuer_jeu = 1
        #Load fond
        fond = pygame.image.load("./images/fin.png").convert()
        fenetre.blit(fond, (0,0))

        pygame.display.flip()

