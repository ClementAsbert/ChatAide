# -*- coding: utf-8 -*-
from Util import util


class Utilisateur():
    
    
    """Classe de l'utilisateur"""
    def __init__(self,nom,niveau):
        
        """Constructeur"""
        self.niveau=niveau
        self.__name=nom        


    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom de l'utilisateur
        """
        return self.__name





