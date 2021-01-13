# -*- coding: utf-8 -*-
from Image import App

class Bot():
    """Classe du Bot"""
    def __init__(self):
        """Constructeur"""
        self.exoEnCours = None
        self.reponse = ""
        self.attenteReponse = False
        self.exosFini = []
        self.__name = "Bot"


    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom du bot 
        """
        return self.__name



    def respond(self,demande,cursor,user):
        
        rep = " "+demande #On met un espace au début du message pour un meilleur filtrage des gros mots
        matiereTrouve = self.scanMatiere(rep)
        grosMots = self.grosmot(rep,cursor)


        """Vérifie qu'il n'y ai pas de gros mots"""
        if grosMots:
            return "Surveille ton langage ! "
        
        
        """Cas où le bot est en attente d'une réponse"""
        if self.attenteReponse: 
            if self.reponse in demande:
                self.attenteReponse = False
                self.exosFini.append(self.exoEnCours)
                self.exoEnCours = None
                return "Bravo tu as réussi l'exercice "
            elif matiereTrouve!=None: #Cas ou l'utilisateur demande un autre exercice
                reponseFinal = self.enonce(matiereTrouve,cursor,user)
            else:
                return "Essaye encore :/ "
        else:
            
            """Si le Bot n'attend pas de réponse"""
            if(matiereTrouve!=None):    #Si le scan détecte une matiere dans la réponse alors lui assigne un énoncé
                reponseFinal = self.enonce(matiereTrouve,cursor,user)
            elif((matiereTrouve!=None) and ('bonjour' in demande)):
                reponseFinal = 'Bonjour, ' + reponseFinal
            elif((matiereTrouve==None) and ('bonjour' in demande)):
                reponseFinal = "Bonjour :)"
            else:
                reponseFinal = "Je ne comprends pas"

       
        return reponseFinal
            



    """Attribut un énoncé de la base de données à une matière donnée et retourne l'énoncé"""
    def enonce(self,matiere,cursor,user):
        if (matiere == "histoire") or (matiere == "géographie"):
            return "Pas d'exercices dans cette matière :( "
        
        if matiere=="image":
            self.SendImage()
            return "Voici votre exercice en image"


        """Recherche d'exercice dans la BDD"""
        cursor.execute("SELECT enonce,idEx,reponse FROM exercice NATURAL JOIN matiere WHERE nom = "+"'"+matiere+"'"+" AND classe= "+"'"+user.niveau+"'"+" ;") #AND idEx NOT IN "+"'".join(self.exoFini)+"'"+" 
        enonce = cursor.fetchone()
        rsp = "%s" % enonce[0]
        self.reponse = "%s" % enonce[2]
        self.exoEnCours = "%d" % enonce[1]
        while (self.exoEnCours in self.exosFini):
            enonce = cursor.fetchone()
            if(enonce==None):
                return "Tu as fini tout les exercices de cette matière"
            else:
                rsp = "%s" % enonce[0]
                self.reponse = "%s" % enonce[2]
                self.exoEnCours = "%d" % enonce[1]
        


        """Met le bot en attente de la Réponse"""
        self.attenteReponse = True
        
        return rsp


    def scanMatiere(self,rep):
        
        matiere = ("image","français","mathématiques","histoire","géographie")
        matiereScore = [0,0,0,0,0]
        
        deb=0
        fin=2
        taille=len(rep)
        ok=True
        while ok==True:
            extr = rep[deb:fin]
            ok = False
            for s in matiere:
                if (s.find(extr)>=0 and fin<taille):
                    if len(extr)>1:
                        matiereScore[matiere.index(s)]=matiereScore[matiere.index(s)]+1
                    ok = True
            fin=fin+1
            if (ok==False and deb<=taille-1):
                deb+=1
                fin=deb+1
                ok=True
        
        
        
        max1 = -1
        max2 = -1

        for a in matiereScore:
            if a > max1:
                max1 = a
            elif a > max2:
                max2 = a
        
        """Réponse final du scan"""
        if (max(matiereScore)==min(matiereScore) or max1<=max2+3): #Si aucune matiere est détecté
            return None
        else:
            return matiere[matiereScore.index(max(matiereScore))]

        



    """Vérifie si il y a un gros mot dans le texte donné"""
    def grosmot(self,str,cursor):
        cursor.execute("SELECT mot FROM grotmot;")
        grosmot = cursor.fetchall()
        for mot in grosmot:
            gromo = " "+mot[0]
            if gromo in str:
                return True
        return False

    """Envoie d'une image"""
    def SendImage(self):
        self.image = App("img/ImageMaths.jpg")




