use chatbot;
update aide SET indice = 'Si on donne quelque chose en plus de ce qu\'on a déjà il faut additionner ce qu\'on a au départ avec ce qu\'on nous donne. Par exemple si on a 5 pommes et qu’on nous donne 10 pommes on fait 5+10=15, on a 15 pommes.' where idAide = 2;
update aide SET indice = 'Rappel COD COI : Pour trouver le COD il faut se poser la question « qui ? » ou « quoi ? » par exemple : Paul fait du vélo.  Qui fais du vélo ? Pour le COI il faut ce poser la question « à qui ? », « à quoi ? » par exemple : la chemise a carreaux appartient a caroline. A qui appartient la chemise a carreaux ? ' where idAide = 3;
update aide SET indice = 'Faites bien attention à regarder horizontalement, verticalement, diagonalement et a l\'envers.' where idAide = 5;
update aide SET indice = 'Rappelez vous bien de la syntaxe d\'une coordonnée, il ce trouve entre parenthèse, par exemple (z,8).' where idAide = 6;
update aide SET indice = 'Regardez bien la ponctuation cela pourrait vous aider.' where idAide = 7;

update exercice SET classe = 'CE1' where idEx = 27;

INSERT INTO exercice VALUES
(28,"4-2=","2",1,"CP",NULL),
(29,"10+11=","21",1,"CP",NULL),
(30,"Ecris quatre milliards trois cent cinquante-sept millions cent trente-cinq mille trois cent vingt-deux.","4 357 135 322",1,"CM1",NULL),
(31,"Combien y a-t il d'unités entières dans 9/3 ?","3",1,"CM1",NULL),
(32,"Ecris 3015/10 sous la forme d'un nombre décimal.","3015,5",1,"CM2",NULL),
(33,"Complète le phrase avec a ou à : Il n'en ... pas parlé.","a",2,"CM2",NULL),
(34,"Conjugue le verbe \"partager\" au passé composé à la première personne du pluriel (nous).","nous avons partagé",2,"CM2",NULL),
(35,"Complète la phrase  : La petite fille ... son père achètent des glaces.","et",2,"CM1",NULL);

INSERT INTO aide VALUES
(8,"Pour les opérations quand il y a un signe \"-\" il faut soustraire donc prendre la valeur de gauche moins la valeur de droite, lorsqu\'il y a le signe \"+\" il faut additionner les deux valeurs de l'opération.",1),
(9,"Attention à bien mettre les espaces.",1),
(10,"Essayer de conjuguer le mot à placer, si vous pouvez le conjuguer c'est donc un verbe et vous pouvez donc deviner quel est le bon mot à remplir.",2);

INSERT INTO aideexo VALUES
(28,8),
(29,8),
(30,9),
(33,10),
(35,10);