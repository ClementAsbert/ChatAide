# -*- coding: utf-8 -*-
from Util import util


class Utilisateur():
    
    
    """Classe de l'utilisateur"""
    def __init__(self):
        
        """Constructeur"""
        self.util = util()
        print(self.util.niveau)
        self.niveau=self.util.niveau
        self.__name=self.util.nom        


    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom de l'utilisateur
        """
        return self.__name





