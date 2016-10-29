#  -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:02:00 2016

@author: Philippe

Déclaration des constantes utilisées pour la prédiction
"""

from numpy import zeros
from datetime import timedelta, datetime

#   constantes generales non ajustables (liees a la structure du programme)

# donnees bibliotheque et buffer
N_ATTRIBUT = 7    # nombre d attributs pour les donnees et pour buffer
NON_FILTRE = 0    # valeur non filtrees
FILTRE = 1    # valeur filtrees
SEQUENCE = 2  # sequence(1 nuit 0-5, 2 matin 6-10, 3 midi 11-16, 4 soir 17-23)
DEB_NUIT = 0
NUIT = 1
DEB_MATIN = 6
MATIN = 2
DEB_MIDI = 11
MIDI = 3
DEB_SOIR = 17
SOIR = 4
TYPE_POINT = 3    # type de point (-1 mini, 1 maxi, 0 reste)
MIN_POINT = -1
MAX_POINT = 1
INTER_POINT = 0
HEURE_POINT = 4    # heure de la valeur
JOUR_POINT = 5    # jour de la valeur
MOIS_POINT = 6    # mois de la valeur
ANNEE_POINT = 7    # annee de la valeur
MIN_SEQ = 0    # mini de la sequence
MAX_SEQ = 1    # maxi de la sequence
NB_SEQ = 4    # nombre de sequences
# predicteur analogie
ANA_HEURE = 0    # heure du resultat
ANA_ECART_MC = 1    # ecart MC du resultat
# predicteur parametre
PARA_HEURE = 0    # heure du resultat
PARA_ECART_MC = 1    # ecart MC du resultat
# prediction
PRED_ECART = 0  # ecart prediction
PRED_RANG = 1    # rang prediction
# valeurs predites
VAL_ANNEE = 4
VAL_MOIS = 3
VAL_JOUR = 2
VAL_HEURE = 1
VAL_VALEUR = 0
DATE_INIT = datetime(1900, 1, 1, 0)
TIME_HEURE = timedelta(0, 3600)
MAXI = 10000000.0

#  constantes ajustable (modifie le fonctionnement du programme)

# bibliotheque : historique des donnees sur plusieurs annees
# FILE_BIBLIO = """D:/LocalData/a179227/python/analyse de données/prediction/\
# Biblio_2014-2015_export.csv"""
FILE_BIBLIO = """./Biblio_2014-2015_export.csv"""

N_LIGNE = 17520    # nombre de lignes du fichiers (donnees bibliotheque)
N2AIXA = 4  # colonne de la serie
N2AIXC = 5  # colonne de la serie
N2CINQ = 6  # colonne de la serie
N2PLOM = 7  # colonne de la serie
N2RABA = 8  # colonne de la serie
N2STLO = 9  # colonne de la serie
O3AIXA = 10  # colonne de la serie
O3AIXP = 11  # colonne de la serie
O3CINQ = 12  # colonne de la serie
PCAIXA = 13  # colonne de la serie
PCAIXC = 14  # colonne de la serie
PCCINQ = 15  # colonne de la serie
PCRABA = 16  # colonne de la serie
PCSTLO = 17  # colonne de la serie

# simulation : parametres de reglage
N_RESULT = 60    # nombre de donnees traitees (9000), 90, 900
N_DEPART = 26    # premiere ligne des donnees traitees, 26
TAILLE_BUFFER = 24  # taille du buffer pour les donnees acquises et predites
DEBUG_DONNEES = False  # export des donnees
DEBUG_BUFFER = False  # export des buffer
DEBUG_ANALOGIE = False  # export des donnees analogie
DEBUG_PARAMETRE = False  # export des donnees parametre
DEBUG_PREDICTION = False  # export des donnnees predites
DEBUG_PREDICTION1 = False  # export des donnees predites h+1
DEBUG_PREDICTION2 = False  # export des donnees predites h+2
DEBUG_PREDICTION3 = False  # export des donnees predites h+3
DEBUG_PREDICTION4 = False  # export des donnees predites h+4
DEBUG_PREDICTION5 = False  # export des donnees predites h+5
AFFICHE_HORIZON = 0    # horizon de prediction pour ana et para (0 a HORIZON-1)

# predicteur reference : parametres de reglage
REF_SCENARIO = 3    # nombre de predicteurs de reference
REF_PENTE = 1.    # pente du predicteurs de reference (par défaut valeur 1)

# predicteur analogie : parametres de reglage
ANA_PROFONDEUR = 8    # nombre d heures de comparaison
ANA_FILTRAGE = False    # utilisation des donnees recue filtrees pour ana
ANA_FILTRAGE_BIBLIO = False   # utilisation donnees biblio filtrees pour ana
ANA_SCENARIO = 8   # nombre de scenario de calcul d ecart traites

# predicteur parametre : parametres de reglage
PARA_PROFONDEUR = 3   # nombre de points de comparaison
PARA_HORIZON_POINT = 20   # horizon de recherche des points (< a TAILLE_BUFFER)
PARA_SENS = 1    # METTRE A -1 POUR LES SERIES O3 ET A 1 POUR LES AUTRES SERIES

# traitement et prediction : parametres de reglage
PRED_MOYEN = 0  # moyenne historique des rangs des prédicteurs (1 : h et h-1)
HORIZON = 5    # horizon de prediction (nombre d heures predites)
PRED_OPTION = 1   # 0 :coef direct, 1 :V_PREDIC, 2 :V_PREDIC + moins bons
V_PREDIC = 0.1    # vitesse d evolution de la prediction : etait (0,08)
V_PREDIC2 = 0.06    # vitesse d evolution de la prediction : etait (0,04)
V_PREDIC3 = 0.03    # vitesse d evolution de la prediction : etait (0,02)
V_MOYENNE = 0.3    # vitesse d evolution de la moyenne : etait 0.1
ACTIVATION_REF = True    # activation predicteur de reference
ACTIVATION_ANA = True    # activation predicteur analogie
ACTIVATION_PARAM = True    # activation predicteur parametre
PRED_RESULTAT = 5   # nombre de meilleurs candidats ana et param conserves
NB_PREDICTEURS = REF_SCENARIO + ANA_SCENARIO + PRED_RESULTAT  # total des pred


# initialisation des coefficients d ajustement des predicteurs

C_MEM_PREDICTION = zeros((NB_PREDICTEURS))
C_MEM_PREDICTION[0] = 0.15
C_MEM_PREDICTION[1] = 0.13
C_MEM_PREDICTION[2] = 0.1
C_MEM_PREDICTION[3] = 0.09
C_MEM_PREDICTION[4] = 0.08
C_MEM_PREDICTION[5] = 0.07
C_MEM_PREDICTION[6] = 0.06
C_MEM_PREDICTION[7] = 0.06
C_MEM_PREDICTION[8] = 0.05
C_MEM_PREDICTION[9] = 0.04
C_MEM_PREDICTION[10] = 0.04
C_MEM_PREDICTION[11] = 0.03
C_MEM_PREDICTION[12] = 0.03
C_MEM_PREDICTION[13] = 0.03
C_MEM_PREDICTION[14] = 0.02
C_MEM_PREDICTION[15] = 0.02

# memoire analogie
C_MEM_ANA = zeros((ANA_PROFONDEUR, ANA_SCENARIO))
C_MEM_ANA[0, 0] = 0.05
C_MEM_ANA[1, 0] = 0.05
C_MEM_ANA[2, 0] = 0.1
C_MEM_ANA[3, 0] = 0.1
C_MEM_ANA[4, 0] = 0.15
C_MEM_ANA[5, 0] = 0.15
C_MEM_ANA[6, 0] = 0.2  # 0,3 au lieu de 0,2
C_MEM_ANA[7, 0] = 0.2  # 0,1 au lieu de 0,2

C_MEM_ANA[0, 1] = 0.02
C_MEM_ANA[1, 1] = 0.03
C_MEM_ANA[2, 1] = 0.05
C_MEM_ANA[3, 1] = 0.1
C_MEM_ANA[4, 1] = 0.15
C_MEM_ANA[5, 1] = 0.15
C_MEM_ANA[6, 1] = 0.25  # 0,4 au lieu de 0,25
C_MEM_ANA[7, 1] = 0.25  # 0,1 au lieu de 0,25

C_MEM_ANA[0, 2] = 0.02
C_MEM_ANA[1, 2] = 0.03
C_MEM_ANA[2, 2] = 0.05
C_MEM_ANA[3, 2] = 0.07
C_MEM_ANA[4, 2] = 0.1
C_MEM_ANA[5, 2] = 0.15
C_MEM_ANA[6, 2] = 0.24
C_MEM_ANA[7, 2] = 0.34

C_MEM_ANA[0, 3] = 0.01
C_MEM_ANA[1, 3] = 0.02
C_MEM_ANA[2, 3] = 0.03
C_MEM_ANA[3, 3] = 0.05
C_MEM_ANA[4, 3] = 0.07
C_MEM_ANA[5, 3] = 0.1
C_MEM_ANA[6, 3] = 0.24
C_MEM_ANA[7, 3] = 0.48

C_MEM_ANA[0, 4] = 0.01
C_MEM_ANA[1, 4] = 0.01
C_MEM_ANA[2, 4] = 0.02
C_MEM_ANA[3, 4] = 0.02
C_MEM_ANA[4, 4] = 0.02
C_MEM_ANA[5, 4] = 0.05
C_MEM_ANA[6, 4] = 0.25
C_MEM_ANA[7, 4] = 0.62

C_MEM_ANA[0, 5] = 0.01
C_MEM_ANA[1, 5] = 0.01
C_MEM_ANA[2, 5] = 0.01
C_MEM_ANA[3, 5] = 0.01
C_MEM_ANA[4, 5] = 0.02
C_MEM_ANA[5, 5] = 0.02
C_MEM_ANA[6, 5] = 0.2
C_MEM_ANA[7, 5] = 0.72

C_MEM_ANA[0, 6] = 0.05
C_MEM_ANA[1, 6] = 0.05
C_MEM_ANA[2, 6] = 0.1
C_MEM_ANA[3, 6] = 0.1
C_MEM_ANA[4, 6] = 0.15
C_MEM_ANA[5, 6] = 0.15
C_MEM_ANA[6, 6] = 0.3
C_MEM_ANA[7, 6] = 0.1

C_MEM_ANA[0, 7] = 0.02
C_MEM_ANA[1, 7] = 0.03
C_MEM_ANA[2, 7] = 0.05
C_MEM_ANA[3, 7] = 0.1
C_MEM_ANA[4, 7] = 0.15
C_MEM_ANA[5, 7] = 0.25
C_MEM_ANA[6, 7] = 0.25
C_MEM_ANA[7, 7] = 0.15

# memoire parametre
C_MEM_PARAM = zeros((PARA_PROFONDEUR))
C_MEM_PARAM[0] = 0.3
C_MEM_PARAM[1] = 0.5
C_MEM_PARAM[2] = 0.2
