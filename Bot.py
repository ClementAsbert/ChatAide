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
        matiere = ("Bonjour","français","mathématiques","histoire","géographie")
        matiereScore = [0,0,0,0,0]
        rep = demande

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
        
        
        print(matiereScore)
        max1 = -1
        max2 = -1

        for a in matiereScore:
            if a > max1:
                max1 = a
            elif a > max2:
                max2 = a


        if max(matiereScore)==min(matiereScore) or max1<=max2+2:
            reponseFinal = "Je ne comprend pas"
        else:
            reponseFinal = matiere[matiereScore.index(max(matiereScore))]
            reponseFinal = self.choix(reponseFinal,cursor)
            print(reponseFinal)
        
        return reponseFinal


    def choix(self,matiere,cursor):
        cursor.execute("SELECT enonce FROM exercice WHERE idMatiere = "+"'"+matiere+"'"+";")
        enonce = cursor.fetchone()
        rsp = "%s" % enonce
        return rsp


