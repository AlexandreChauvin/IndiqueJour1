#Import nécessaire et en relation avec l'univers du temps.
import math
import sys
from datetime import datetime

#Cette méthode permet la séparation de la date par des /
def SeparationDate(date):
    maListe = []
    maListe = date.split("/")
    return maListe

#Cette méthode permet d'ajouter en fonction du mois de la date
def AjoutMois(date):
    maListe = SeparationDate(date)
    mois = maListe[1]
    if mois == "1" or mois == "01" or mois == "10":
        MRetour = 0
    elif mois == "2" or mois == "02" or mois == "3" or mois == "03" or mois == "11":
        MRetour = 3
    elif mois == "4" or mois == "04" or mois == "7" or mois == "07":
        MRetour = "6"
    elif mois == "5" or mois == "05":
        MRetour = 1
    elif mois == "6" or mois == "06":
        MRetour = 4
    elif mois == "08" or mois == "8":
        MRetour = 2
    else:
        MRetour = 5
    return  MRetour

#Cette méthode permet de vérifier si la date est correcte
def VerifDate(date):
    date_format = '%d/%m/%Y'
    my_date = date
    try:
        valid_date = datetime.strptime(my_date, date_format)
    except ValueError:
        print('%s la saisit de la date est incorrecte. ' % my_date)
        return 0


#Cette méthode nous permettra de savoir si l'année est Bissextile
def Bissextile(date):
    maListe = SeparationDate(date)
    anneeDate = maListe[2]
    annee = 2016
    if int(anneeDate) < 2016:
        while int(anneeDate) < annee:
            annee = annee - 4
    elif int(anneeDate) > 2016:
        while int(anneeDate) > annee:
            annee = annee + 4
    if int(anneeDate) == annee:
        return True
    else:
        return False



#Cette méthode donne le jour de la semaine
def JourSemaine(reste):
    reste = reste % 7
    if add == 0:
        resultat = "Dimanche"
    elif add == 1:
        resultat = "Lundi"
    elif add == 2:
        resultat = "Mardi"
    elif add == 3:
        resultat = "Mercredi"
    elif add == 4:
        resultat = "Jeudi"
    elif add == 5:
        resultat = "Vendredi"
    else:
        resultat = "Samedi"
    return resultat

#Cette méthode permet d'ajouter la date de l'annee en fonction du siécle dans lequel on se trouve
def Siecle(date):
    maListe = SeparationDate(date)
    siecle = maListe[2][0:2]
    addAnnee = 0
    if siecle == "16" or siecle == "20":
        addAnnee = 6
    elif siecle == "17" or siecle == "21":
        addAnnee = 4
    elif siecle == "18":
        addAnnee = 2
    else:
        addAnnee = 0
    return addAnnee

#L'utilisateur doit entrer sa date sous le même format indiquer sinon elle sera invalide
date = input("Veuillez saisir une date sous le même format qu'ici : jj/mm/aaaa : ")
if VerifDate(date) == 0:
    sys.exit()
else:
#Cette condition permet de retourner les deux derniers chiffre de l'année
    longueur = len(date)
    longueurDepart = longueur - 2
    annee = date[longueurDepart:]

#Puis on divise par 4 afin de garder la partie entière
    add = int(annee) + int(annee) / 4
    add = math.floor(add)

#Enfin on ajoute la journée du mois correspondant
    maListe = SeparationDate(date)
    lenghtJour = len(maListe[0])
    if lenghtJour == 2:
        jour = date[0:2]
    else:
        jour = date[0:1]
    add = add + int(jour)

#Sinon on ajoute le numéro correspondant au mois
    MRetour = AjoutMois(date)
    add = add + MRetour

#Cette condition permet de tester si l'année est Bissextile
    if maListe[1] == "1" or maListe[1] == "01" or maListe[1] == "2" or maListe[1] == "02":
        verification = "vrai"
    else:
        verification = "faux"
    if Bissextile(date) == True and verification == "vrai":
        add = add - 1

    addAnnee = Siecle(date)
    add = add + addAnnee
    resultat = JourSemaine(add)
#Affiche le jour correspondant à la date saisit par l'utilisateur
    print("La jour correspondant à la date que avez saisit est le", resultat)