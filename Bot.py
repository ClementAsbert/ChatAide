# -*- coding: utf-8 -*-

class Bot():
    """Classe du Bot"""
    def __init__(self):
        """Constructeur"""

        self.__name = "Bot"


    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom du bot 
        """
        return self.__name

    def respond(self,demande,cursor):
        matiere = ("français","mathématiques","histoire","géographie")
        matiereScore = [0,0,0,0]
        rep = " "+demande

        if self.grosmot(rep,cursor):
            return "Surveille ton langage ! "


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
        
        
        #print(matiereScore)
        max1 = -1
        max2 = -1

        for a in matiereScore:
            if a > max1:
                max1 = a
            elif a > max2:
                max2 = a

        print('bonjour' in demande);
        if (max(matiereScore)==min(matiereScore) or max1<=max2+2) and ('bonjour' in demande)==True:
            return "Bonjour :) "
        elif max(matiereScore)==min(matiereScore) or max1<=max2+2:
            return "Je ne comprend pas"
        else:
            

            reponseFinal = matiere[matiereScore.index(max(matiereScore))]
            #print (reponseFinal)
            reponseFinal = self.choix(reponseFinal,cursor)
            #print(reponseFinal)
            if 'bonjour' in demande:
                reponseFinal = 'Bonjour, ' + reponseFinal
        return reponseFinal


    def choix(self,matiere,cursor):
        if matiere == "mathématiques":
            matiere = "mathematique"
        if matiere == "français":
            matiere = "francais"
        cursor.execute("SELECT enonce FROM exercice NATURAL JOIN matiere WHERE nom = "+"'"+matiere+"'"+";") 
        enonce = cursor.fetchone()
        rsp = "%s" % enonce
        return rsp


    def grosmot(self,str,cursor):
        cursor.execute("SELECT mot FROM grotmot;")
        grosmot = cursor.fetchall()
        for mot in grosmot:
            gromo = " "+mot[0]
            if gromo in str:
                return True
        return False




