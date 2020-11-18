# -*- coding: utf-8 -*-


class Utilisateur():
    """Classe de l'utilisateur"""
    def __init__(self):
        """Constructeur"""

        self.__name = "Utilisateur"



    @property
    def name(self):
        """Getter de l'attribut privé __name
        
        Return :
            String : retourne le nom de l'utilisateur
        """
        return self.__name
    
    
