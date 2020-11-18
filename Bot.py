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