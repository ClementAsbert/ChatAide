# -*- coding: utf-8 -*-
from Image import App

class Bot():
    """Classe du Bot"""
    def __init__(self):
        """Constructeur"""
        self.exoEnCours = 0
        self.reponse = ""
        self.attenteReponse = False
        self.exoFini = []
        self.__name = "Bot"


    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom du bot 
        """
        return self.__name

    def respond(self,demande,cursor,user):
        matiere = ("français","mathématiques","histoire","géographie")
        matiereScore = [0,0,0,0]
        rep = " "+demande



        """Vérifie qu'il n'y ai pas de gros mots"""
        if self.grosmot(rep,cursor):
            return "Surveille ton langage ! "
        
        if self.attenteReponse:
            if self.reponse in demande:
                self.attenteReponse = False
                self.exoFini.append(self.exoEnCours)
                self.exoEnCours = 0
                return "Bravo tu as réussi l'exercice "
            else:
                return "Essaye encore :/ "

        """Detecte la matiere souhaité"""
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

        """Vérifie si l'utilitsateur salut le bot"""
        if (max(matiereScore)==min(matiereScore) or max1<=max2+2) and ('bonjour' in demande)==True:
            return "Bonjour :) "
        elif max(matiereScore)==min(matiereScore) or max1<=max2+2:
            return "Je ne comprend pas"
        else:
            

            reponseFinal = matiere[matiereScore.index(max(matiereScore))]
            reponseFinal = self.enonce(reponseFinal,cursor,user)
            
            """Cas où l'utilisateur dit bonjour et demande un énoncé"""
            if 'bonjour' in demande:
                reponseFinal = 'Bonjour, ' + reponseFinal
        return reponseFinal
            


    def enonce(self,matiere,cursor,user):
        if matiere == "mathématiques":
            matiere = "mathematique"
        if matiere == "français":
            matiere = "francais"
        
        """Attribution de la réponse au bot"""
        cursor.execute("SELECT reponse FROM exercice NATURAL JOIN matiere WHERE nom = "+"'"+matiere+"'"+" AND classe= "+"'"+user.niveau+"'"+" ;") 
        reponse = cursor.fetchone()
        self.reponse = "%s" % reponse

        """lecture de l'enonce"""
        cursor.execute("SELECT enonce,idEx FROM exercice NATURAL JOIN matiere WHERE nom = "+"'"+matiere+"'"+" AND classe= "+"'"+user.niveau+"'"+"  ;") 
        enonce = cursor.fetchone()
        rsp = "%s" % enonce[0]
        self.exoEnCours = "%d" % enonce[1]
        
        

        """Met le bot en attente de la Réponse"""
        self.attenteReponse = True

        return rsp


    def grosmot(self,str,cursor):
        cursor.execute("SELECT mot FROM grotmot;")
        grosmot = cursor.fetchall()
        for mot in grosmot:
            gromo = " "+mot[0]
            if gromo in str:
                return True
        return False


    def SendImage(self):
        self.image = App("img/ImageMaths.jpg")




