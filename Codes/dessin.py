# dessin de jeu Azémard-Bertin

################################################################################

# modules importés

from turtle import*
from math import*

#===============================================================================#


# fonctions de dessin en pixels

def dessinPixel(l,c):
    hideturtle()
    pensize (1)
    tracer(0)
    down()
    begin_fill()
    color(c)
    i=0
    while i<4:
        forward(l-1)
        left(90)
        i=i+1
    end_fill()
    up()
    


def paletteCouleurs(c):
    palette=["transparent","white","black","red","green","blue","cyan","yellow","orange","brown","purple","grey","dim gray","lightgrey","dodgerblue"]
    couleur=palette[c]
    return couleur


def dessin(taillePixel,matrice,positionX,positionY,W=1):

    taillePixels=taillePixel*W
    positionX=positionX*W
    positionY=positionY*W
    up()
    tracer(0)
    goto(positionX,positionY)
    for i in range(len(matrice)):
        for n in range(len(matrice[i])):
            goto(positionX+(n*taillePixels),positionY+(-i*taillePixels))

            if (paletteCouleurs(matrice[i][n])!="transparent"):
                dessinPixel(taillePixels,paletteCouleurs(matrice[i][n]))
    update()

      

#==============================================================================#


# Quilles et décors


#________________________________________________________________________________#

# Décors:

#---------------------------------------------------------------#

# étoile noire (avec fonction dessin)


étoilenoire=[[0,0,0,0,2,2,2,2,2,2,2,0,0,0,0],
             [0,0,0,2,11,11,11,11,11,11,11,2,0,0,0],
             [0,0,2,11,12,12,12,11,11,11,0,11,2,0,0],
             [0,2,11,12,12,12,12,12,11,11,11,11,11,2,0],
             [2,11,11,12,12,3,12,12,11,11,11,0,0,11,2],
             [2,11,11,12,12,12,12,12,11,11,0,11,11,11,2],
             [2,11,11,11,12,12,12,11,11,11,11,11,0,11,2],
             [2,11,11,11,11,11,11,11,11,11,11,0,11,11,0],
             [2,12,12,12,12,12,12,12,12,12,12,12,12,12,2],
             [2,11,11,11,11,11,11,11,11,11,11,11,0,0,2],
             [2,11,11,11,11,11,11,11,11,11,0,11,11,11,2],
             [0,2,11,11,11,11,11,11,11,11,11,11,11,2,0],
             [0,0,2,11,11,11,11,11,11,11,11,11,2,0,0],
             [0,0,0,2,11,11,11,11,11,11,11,2,0,0,0],
             [0,0,0,0,2,2,2,2,2,2,2,0,0,0,0]]


            #dessin(15,étoilenoire,0,0)


# Lutin R2D2 (avec fonction dessin)

R2D2=[[0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,2,2,13,14,14,13,2,2,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,2,14,13,14,1,2,14,13,14,2,0,0,0,0,0,0],
       [0,0,0,0,0,2,14,13,13,14,2,2,14,13,13,14,2,0,0,0,0,0],
       [0,0,0,0,0,2,13,13,13,14,14,14,14,13,13,13,2,0,0,0,0,0],
       [0,0,0,0,2,13,14,14,13,13,13,13,13,13,13,13,13,2,0,0,0,0],
       [0,0,0,0,2,13,13,13,13,14,13,14,14,14,13,14,13,2,0,0,0,0],
       [0,0,0,0,2,13,14,14,13,14,13,14,3,14,13,14,13,2,0,0,0,0],
       [0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0],
       [0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,0,0],
       [0,2,1,1,2,13,13,13,1,14,14,14,14,1,13,13,13,2,1,1,2,0],
       [0,2,1,1,2,13,1,13,1,1,1,1,1,1,13,1,13,2,1,1,2,0],
       [0,2,2,2,2,13,1,13,1,14,14,14,14,1,13,1,13,2,2,2,2,0],
       [0,0,2,1,2,13,1,13,1,1,1,1,1,1,13,1,13,2,1,2,0,0],
       [0,0,2,1,2,13,1,13,1,14,13,13,14,1,13,1,13,2,1,2,0,0],
       [0,0,2,1,2,13,1,13,1,14,13,13,14,1,13,1,13,2,1,2,0,0],
       [0,0,2,1,2,13,1,13,1,1,1,1,1,1,13,1,13,2,1,2,0,0],
       [0,0,2,1,2,13,13,13,1,14,14,14,14,1,13,13,13,2,1,2,0,0],
       [0,0,2,1,2,1,1,13,1,14,13,2,14,1,13,1,1,2,1,2,0,0],
       [0,0,2,2,2,1,1,13,1,14,2,13,14,1,13,1,1,2,2,2,0,0],
       [0,2,1,13,2,1,1,13,1,14,14,14,14,1,13,1,1,2,13,1,2,0],
       [0,2,1,13,2,2,2,2,2,2,2,2,2,2,2,2,2,2,13,1,2,0],
       [2,1,1,1,2,0,0,0,2,1,13,13,1 ,2,0,0,0,2,1,1,1,2],
       [2,1,1,1,2,0,0,2,1,13,1,1,13,1,2,0,0,2,1,1,1,2],
       [2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2]]


        #dessin(10,R2D2,0,0)


    

#---------------------------------------------------------------------------------#

# planète

def dessinePolygone(nbcotes,longueur,positionX=0,positionY=0,couleur="black"):
    up()
    tracer(0)
    hideturtle()
    goto(positionX,positionY)
    down()
    color(couleur)
    begin_fill()
    for i in range(nbcotes):
        forward(longueur)
        left(360/nbcotes)
    end_fill()
    up()
    update()


def dessineCercle(rayon,positionX,positionY,couleur):
    goto(positionX,positionY)
    down()
    l=(rayon*2*3.14159)/50
    dessinePolygone(50,l,positionX,positionY-rayon,couleur)
    up()





def planète(rayon,R,positionX,positionY,couleurSphère,couleurAnneau):
    
    pas=radians(360/50)
    k=3.8

    up()
    tracer(0)
    pensize(5)
    goto(positionX+R,positionY)
    down()
    color(couleurAnneau)
    
    for i in range(1,25):
        goto(int(R*cos(i*pas)+positionX),int(R*sin(i*pas)/k+positionY))
        
    up()
    dessineCercle(rayon,positionX,positionY,couleurSphère)
    goto(positionX-R,positionY)
    color(couleurAnneau)
    down()
    
    for i in range(25,50):
         goto(int(R*cos(i*pas)+positionX),int(R*sin(i*pas)/k+positionY))
    update()



# étoiles:

def étoile(x,y,taille,couleur,W):
        up()
        goto ((x-(1.6*taille))*W,(y-(0.4*taille))*W)
        color (couleur)
        begin_fill ()
        for i in range(10):
           forward(taille*W)
           right(108)
           forward(taille*W)
           left(144)
        end_fill ()
        update() 

    

#_________________________________________________________________________________#

#Quilles:

# quilles vaisseaux

def vaisseau(x,y,taille,W=1):
    #hideturtle()
    #tracer(0)
    t=taille*W
    x=x*W
    y=y*W
    seth(0)

    up()
    goto(x,y)
    down()
    width(8*t)
    forward(50*t)
    left(90)
    up()
    goto((50*t)+x,(25*t)+y)
    down()  
    width(1*t)
    color('red')
    begin_fill()
    circle(25*t)
    end_fill()
    color('black')
    width(8*t)
    right(90)
    forward(20*t)
    width(3*t)
    begin_fill()
    right(90)
    forward(100*t)
    left(90)
    forward(20*t)
    left(90)
    forward(200*t)
    left(90)
    forward(20*t)
    left(90)
    forward(100*t)
    end_fill()
    up()
    goto(x,(25*t)+y)
    down()
    right(90)
    width(8*t)
    forward(20*t)
    width(3*t)
    begin_fill()
    right(90)
    forward(100*t)
    left(90)
    forward(20*t)
    left(90)
    forward(200*t)
    left(90)
    forward(20*t)
    left(90)
    forward(100*t)
    end_fill()
    up()
    goto(x,y)
    down()
    width(8*t)
    forward(50*t)
    right(90)
    forward(50*t)
    right(90)
    forward(50*t)
    seth(0)
    pensize (1)
    up()
    #update()

    #vaisseau(0,0,1)



# quilles couchées: vaisseau détruit  (avec fonction dessin)

vaisseau_explosé=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                 [0,0,2,2,0,0,0,0,0,0,0,3,0,0,2,0,0],
                 [0,0,2,2,0,0,3,3,3,3,3,3,0,0,2,0,0],
                 [0,0,2,2,0,0,8,8,0,0,0,3,3,8,2,0,0],
                 [0,0,2,2,0,0,2,2,2,2,2,3,8,2,2,0,0],
                 [0,0,2,2,0,0,2,3,3,8,3,2,2,2,0,0,0],
                 [0,0,2,2,0,0,2,3,8,8,8,8,2,2,0,0,0],
                 [0,0,2,2,2,2,2,8,8,8,3,2,8,2,0,0,0],
                 [0,0,2,2,0,0,2,8,3,8,2,2,3,2,0,0,0],
                 [0,0,2,2,0,0,2,2,2,2,2,3,3,8,8,0,0],
                 [0,0,2,2,0,0,8,3,0,9,0,8,8,2,3,0,0],
                 [0,0,2,2,0,8,0,3,0,9,9,8,0,2,3,0,0],
                 [0,0,2,2,0,0,0,3,3,3,8,9,9,2,3,0,0],
                 [0,0,2,2,0,0,0,3,3,3,9,9,9,2,3,0,0],
                 [0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0]]



                  
                    #dessin(10,vaisseau_explosé,0,0)



# rectangle (fond qui recouvre une quille)

def effaceVaisseau(x,y,taille,W=1):
    up()
    hideturtle()
    tracer(0)

    x=x*W
    y=y*W
    taille=taille*W
    
    goto(x-(45*taille),y-(80*taille))
    seth(0)

    down()
    color("dark blue")
    begin_fill()
    
    for i in range (2):
        forward(140*taille)
        left(90)
        forward(210*taille)
        left(90)

    end_fill()
    up()
    





#__________________________________________________________________________________________________________#

# Décors intérieurs (vaisseau interne)

#écran de jeu

def dessineEcran(vitre,W=1):
    #setup(1600,800)
    bgcolor("grey")
    up()
    hideturtle()
    tracer(0)
    begin_fill()
    color("dark blue")
    pensize(4)
    pencolor("black")


    goto(vitre[0][0]*W,vitre[0][1]*W)
    down()

    for i in range(1,len(vitre)):
        goto(vitre[i][0]*W,vitre[i][1]*W)
        
    end_fill()
    up()
    update()





def Ecran(W=1):

    vitreCentre=[[-350,-200],[350,-200],[550,0],[550,50],[350,250],[-350,250],[-550,50],[-550,0],[-350,-200]]
    vitreBasDroit=[[400,-200],[550,-350],[700,-350],[750,-300],[750,0],[600,0],[400,-200]]
    vitreHautDroit=[[600,50],[750,50],[750,300],[700,350],[600,350],[400,250],[600,50]]
    vitreBasGauche=[[-400,-200],[-550,-350],[-700,-350],[-750,-300],[-750,0],[-600,0],[-400,-200]]
    vitreHautGauche=[[-600,50],[-750,50],[-750,300],[-700,350],[-600,350],[-400,250],[-600,50]]
    vitreHaut=[[-375,275],[375,275],[525,350],[-525,350],[-375,275]]

    cinqVitres=[vitreCentre,vitreBasDroit,vitreHautDroit,vitreBasGauche,vitreHautGauche,vitreHaut]

    for i in range(len(cinqVitres)):
        dessineEcran(cinqVitres[i],W)
 




# écran de texte (tableau de bord):

def ecranTexte(texte,W=1):
    up()
    tracer(0)

    ecran=[[-350,-300],[10,-300],[10,-240],[-350,-240],[-350,-300]]
    
    
    pencolor("gray95")
    pensize(3)
    fillcolor("cyan")
    begin_fill()

    goto(ecran[0][0]*W,ecran[0][1]*W)
    down()

    for i in range(1,len(ecran)):
        goto(ecran[i][0]*W,ecran[i][1]*W)
    
    end_fill()
    up()

    color("black")
    goto(-340*W,-275*W)
    write(texte,align="left",font=("Courier New",int(12*W),"bold"))
    update()



# boutons (avec fonction dessin)

tableau_de_bord_A=[[0,2,2,2,2,2,2,2,2,2,2,2,2],
                [0,2,14,14,14,14,14,14,14,14,14,14,2],
                [0,2,14,8,14,14,5,14,14,14,4,14,2],
                [0,2,14,14,14,14,5,14,9,14,14,14,2],
                [0,2,14,3,14,14,5,14,14,14,12,14,2],
                [0,2,14,14,14,14,14,14,14,14,14,14,2],
                [0,2,2,2,2,2,2,2,2,2,2,2,2]]


#-----------------------------------------------------------#

# Ecran de jeu

def ecranDeJeu(W=1):

    Ecran(W)
    ecranTexte("",W)
    dessin(10,tableau_de_bord_A,200,-240,W)
    étoile(200,150,6,"white",W)
    étoile(-400,310,10,"white",W)
    étoile(-500,70,5,"white",W)
    étoile(-50,-150,12,"white",W)
    étoile(600,-100,12,"Yellow",W)
    étoile(-700,250,8,"white",W)
    dessin(10,R2D2,-680,-130,W)
    dessin(5,étoilenoire,650,200,W)
    planète(10*W,30*W,600*W,300*W,"orange","yellow")
    planète(20*W,50*W,-680*W,-50*W,"red","green")
    




































