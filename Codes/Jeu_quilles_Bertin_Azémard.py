#fonctions du projet Azémard-Bertin

######################################################################################################################################################################################################"

# modules importés:

from random import*
from turtle import*
from dessin import*
from time import*

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#fonctions textuelles

# 1: convertir une liste de liste en une chaine de .|.| (pour la fonction afficheQuilles)

def transformationEnChaîne(q,n):                    # on rentre 2 variables: q= une liste de liste de la forme [[a,b][c,d]...] ; et n est le nombre total de quilles
    début=1
    chaîne=""
    if len(q)==0:                                   # si la taille de la chaine de quille est 0
        chaîne="."*n                                # alors afficher que des points
    else:
        for i in range (len(q)):                    # pour i (un compteur) qui prend toutes les valeurs de la liste de liste q (ex: si i=2 alors i représente la deuxième liste de l'ensemble des listes indiquées)
            chaîne=chaîne+"."*(q[i][0]-début)       #-> pour afficher les points
            début=q[i][1]+1 
            chaîne=chaîne+"|"*(q[i][1]-q[i][0]+1)   # -> pour afficher les batons
        chaîne=chaîne+"."*(n-q[len(q)-1][1])        # -> pour afficher les derniers points de l'ensemble
    return chaîne                                   # renvoyer la chaine de caractère de forme ...||...|||..



# 2: fonction qui affiche les quilles debouts et couchées

def afficheQuilles(q,n):
    print("Voici les quilles, il y a ",len(q),"groupe(s) de quilles")   # on indique le nombre de quilles dans la partie
    print(transformationEnChaîne(q,n))                                  # on affiche la chaine de ...|||...||.




# 3: fonction pour faire jouer l'ordinateur au hasard

def ordiJoue(q):                              # q est la liste de liste (ex: [[3,5],[8,10]] )
    i=randint(1,len(q))                       # choisir une des listes au hasard (dans l'exemple il y a 2 éléments, donc on choisit au hasard entre 1 et 2)
    p=choice(["G","M","D"])                   # choisir au hasard une lettre
    reponse=str(i)+":"+p                      # créer une chaine de caractère de type: i:p  (ce qui correspond à "une liste : une lettre")
    return reponse                            # renvoyer la chaine


# 4: fonction pour faire jouer le joueur

def joueurJoue(q):
    
    i=int(input("Quel groupe ? :" ))                          # demander une des listes parmis les listes proposées
    while (not(0<i<=len(q))):                                 # tant que la liste indiquée par le joueur n'est pas comprise dans les listes proposées
        i=int(input("Erreur ! Quel groupe ? : "))             # alors redemander une liste
        
    p=input("Ou tirer? (G,M,D) : ")                           # demander où tirer (on choisit une lettre)
    while (not (p in ["G","M","D"])):                         # tant que le caractère indiqué n'est pas G ou M ou D
        p=input("Erreur ! Ou tirer ? (G,M,D) ")               # alors on redemande une lettre
        
    reponse=str(i)+":"+p                                      # on créer la chaine de caractère qui correspond au choix de jeu du joueur
    return reponse                                            # renvoyer la chaine
    


# 5: fonction pour extraire le numero de la ligne et le convertir en nombre entier

def ligne(c):
    nombreExtrait=int(c[0:len(c)-2])                        # on convertit le numero de liste choisit par le joueur sous forme de chaine de caractère en un entier
    return nombreExtrait                                    # renvoyer l'entier


# 6: fonction pour extraire le choix (G,M,D)

def choix(c):
    choixExtrait=c[-1]                                      # on indique dans choixExtrait la lettre choisit par le joueur
    return choixExtrait                                     # on renvoit la lettre


# 7: procédure principale "jouer"

def jouer(c,q):
    if (q[ligne(c)-1][0])==(q[ligne(c)-1][1]):              # si le 1er nombre d'une liste = le 2e nombre de la même liste (ex: [4,4] )
        del q[ligne(c)-1]                                   # alors on supprime la liste (en effet il ne reste qu'une quille dans la liste, donc cette liste disparait au prochain tour)

    elif choix(c)=="M":                                     # si on joue au milieu
        jouerMilieu(c,q)

    else:                                                   # dans les autres cas
        jouerCote(c,q)
        



# 7a: procédure secondaire "jouerCote" (gauche/droite)

def jouerCote(c,q):
    if choix(c)=="G":                                     # si on joue à gauche
        q[ligne(c)-1][0]+=1                               # alors le premier membre de la liste choisie est augmenté de 1 (ex: [3,5] devient [4,5] )
    elif choix(c)=="D":                                   # si on joue à droite
        q[ligne(c)-1][1]-=1                               # alors le 2e membre de la liste est baissé de 1  (ex: [3,5] devient [3,4] )


# 7b: procédure secondaire "jouerMilieu"

def jouerMilieu(c,q):
    if (q[ligne(c)-1][0]+1)==(q[ligne(c)-1][1]):            # si le 1er membre de la liste choisie, augmenté de 1 = le 2e membre
        del q[ligne(c)-1]                                   # alors on supprime la liste (en effet il y a 2 quilles dans la liste)

    elif (q[ligne(c)-1][0]+2)==(q[ligne(c)-1][1]):          # si il y a 3 quilles dans la liste
        q[ligne(c)-1][0]+=2                                 # alors on augmente le premier membre de la liste de 2 (ex: [3,5] devient [5,5] )

    else:                                                   # dans les autres cas: il faut transformer une liste en deux nouvelles listes (ex: [4,9] devient [4,5] et [8,9] )
        milieu=int((q[ligne(c)-1][0]+q[ligne(c)-1][1])/2)   # milieu = l'entier de ( la moyenne du 1er membre + le 2e membre)
        listeGauche=[q[ligne(c)-1][0],milieu-1]             # listeGauche = [1e membre de la liste initiale, moyenne - 1]  
        listeDroite=[milieu+2,q[ligne(c)-1][1]]             # listeDroite = [moyenne +2 , 2e membre de la liste initiale]  -> ici on à retirer la quille du milieu (moyenne) et la quille à sa droite (on impose que la quille qui tombe est toujours celle de droite)
        del q[ligne(c)-1]                                   # supprimer la liste initiale
        q.insert(ligne(c)-1,listeGauche)                    # on insère la nouvelle liste de gauche
        q.insert(ligne(c),listeDroite)                      # on insère la nouvelle liste de droite après la liste de gauche


#========================================================================================#

# fonctions textuelles modifiées pour l'affichage du décors grâce aux fonctions de dessin(dessin) 

def graphQuilles(q,n,W):
    chaîne=transformationEnChaîne(q,n)
    for i in range(len(chaîne)):
        y=25
        x=-500+(((500-(-500))*(i))/(n-1))

        
        if chaîne[i]=="|":
            vaisseau(x,y,0.2,W)

        else:
            effaceVaisseau(x,y,0.2,W)
            dessin(2,vaisseau_explosé,x-(50*0.2),y+(100*0.2),W)





def graphJoueurJoue(q):
    
    i=int(numinput("Pilote rebelle","Quel chasseur ? :" ))                       
    while (not(0<i<=len(q))):                                
        i=int(numinput("Pilote rebelle","Erreur ! Quel chasseur ? : "))      
        
    p=textinput("Pilote rebelle","Ou tirer? (G,M,D) : ")                       
    while (not (p in ["G","M","D"])):                       
        p=textinput("Pilote rebelle","Erreur ! Ou tirer ? (G,M,D) ")
        
    reponse=str(i)+":"+p                    
    return reponse              
    


#===============================================================================#

# adaptation de l'écran

def adaptationEcran(q,n,W):
    grandissementHorizontal=(window_width())/1600
    grandissementVertical=(window_height())/800
    grandissement=min(grandissementHorizontal,grandissementVertical)

    if grandissement!=W:
        W=grandissement
        clear()
        ecranDeJeu(W)
        graphQuilles(q,n,W)
    return W




#===============================================================================#

#Animations de jeu




def boum(x,y,W=1):
    def étoileBoum (x,y,taille,couleur,W):
        tortueBoum.up()
        tortueBoum. goto ((x-(1.6*taille))*W,(y-(0.4*taille))*W)
        tortueBoum.color (couleur)
        tortueBoum. begin_fill ()
        for i in range(10):
           tortueBoum. forward(taille*W)
           tortueBoum. right(108)
           tortueBoum. forward(taille*W)
           tortueBoum.left(144)
        tortueBoum.end_fill ()
        update() 
   
    tortueBoum=Turtle()
    tortueBoum.hideturtle()
    étoileBoum (x,y,20,"white",W)
    sleep(0.1)
    étoileBoum (x,y,40,"yellow",W)
    sleep(0.1)
    étoileBoum (x,y,65,"orange",W)
    sleep(0.1)
    tortueBoum.clear()





def abscissesVaisseauxdétruits(chaîneActuelle,chaînePrécédente,choix):
    x=0
    if choix[2]=="M":
        x= (500/(len(chaîneActuelle)-1))
    for i in range(len(chaîneActuelle)):
        if chaîneActuelle[i]!=chaînePrécédente[i]:
            x=-500+(((500-(-500))*(i))/(len(chaîneActuelle)-1))+x
            break
    
    return x








def laser(débutX,débutY,finalX,finalY,couleur,W=1):

    tortueLaser=Turtle()
    
    tortueLaser.hideturtle()
    tortueLaser.up()
    
    tortueLaser.goto(débutX*W,débutY*W)

    tortueLaser.down()
    tracer(1)
    tortueLaser.pensize(4)

    bgcolor(couleur)

   
    tortueLaser.color(couleur)
    tortueLaser.speed(8)
    tortueLaser.goto(finalX*W,finalY*W)
   
    tracer (0)
    boum(finalX,finalY,W)
    bgcolor("grey")
    tortueLaser.clear()

   
   



################################################################################################################################################################################################################################

# 8: Programme de JEUX (mofifié avec les fonctions de dessin)

agr=1

setup(1600,800)
tracer (0)
ecranDeJeu(agr)
nb_Quilles=randint(8,18)                                                      # on choisit un nombre de quille au hasard (on impose ici que le nombre est compris entre 8 minimum et 18 maximum)
quilles=[[1,nb_Quilles]]                                                        # on créer la première liste de liste de la forme [[1, nombre de quilles au hasard]]  (ici il n'y à qu'une seule liste)


situationPrécédenteDesQuilles=transformationEnChaîne(quilles,nb_Quilles)



ecranTexte("Début de jeux",agr)



sleep(1)
agr=adaptationEcran(quilles,nb_Quilles,agr)
ecranTexte("Il y a "+str(nb_Quilles)+" chasseurs dans la partie",agr)           # on indique le nombre de quilles dans la partie
           
                               # on affiche les quilles
graphQuilles(quilles,nb_Quilles,agr)
update()

while (len(quilles)>0):                                                         # tant que le nombre d'éléments dans la liste "quilles">0   <=> tant qu'il reste des quilles en jeux  <=> tant qu'il n'y a pas de gagnant

    agr=adaptationEcran(quilles,nb_Quilles,agr)

    choixJoueur=graphJoueurJoue(quilles)                                             # le joueur joue
    ecranTexte("Vous jouez "+choixJoueur,agr)
    sleep(1)
    agr=adaptationEcran(quilles,nb_Quilles,agr)
    
    jouer(choixJoueur,quilles)                                                  # la fonction "jouer" applique le choix du joueur

    situationDesQuilles=transformationEnChaîne(quilles,nb_Quilles)
    laser(300,-200,abscissesVaisseauxdétruits(situationDesQuilles,situationPrécédenteDesQuilles,choixJoueur),25,"green",agr)
    situationPrécédenteDesQuilles=transformationEnChaîne(quilles,nb_Quilles)

    
    graphQuilles(quilles,nb_Quilles,agr)
    
    if len(quilles)==0:                                                         # s'il n'y a plus de quille après le jeu du joueur
        ecranTexte("Bravo ! Vous avez gagné",agr)                                                # alors le joueur gagne
        
    else:
        sleep (1)
        agr=adaptationEcran(quilles,nb_Quilles,agr)
        choixOrdi=ordiJoue(quilles)                                             # l'ordinateur joue
        ecranTexte("R2D2 joue "+str(choixOrdi),agr) # on affiche ce que joue l'ordinateur
        jouer(choixOrdi,quilles)                                                # la fonction "jouer" applique le choix de jeu de l'ordinateur
        sleep(2)
        agr=adaptationEcran(quilles,nb_Quilles,agr)
        situationDesQuilles=transformationEnChaîne(quilles,nb_Quilles)
        laser(-300,-200,abscissesVaisseauxdétruits(situationDesQuilles,situationPrécédenteDesQuilles,choixOrdi),25,"blue",agr)
        situationPrécédenteDesQuilles=transformationEnChaîne(quilles,nb_Quilles)
        ecranTexte(" ",agr) #on efface le message de l'ordi
        sleep (1)
        agr=adaptationEcran(quilles,nb_Quilles,agr) 

                                    # on affiche les quilles restantes
        graphQuilles(quilles,nb_Quilles,agr)
        
        if len(quilles)==0:                                                     # s'il n'y a plus de quilles après le jeu de l'ordinateur
           ecranTexte("Perdu ! R2D2 a gagné !",agr)




