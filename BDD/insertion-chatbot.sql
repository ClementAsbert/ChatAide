SET SQL_SAFE_UPDATES = 0;
delete from exercice;
delete from aide;
delete from matiere;

INSERT INTO matiere VALUES
(1, "mathematique"),
(2, "francais");

INSERT INTO exercice VALUES
(1,"conjuguez la phrase suivante avec le verbe 'aller' : Je ... à l'école.","vais",2,"CE2"),
(2,"Ecrviez le mot suivant au féminin -> directeur : ","directrice",2,"CM2"),
(3,"pierre à 2 bonbons, on lui donne 3 bonbons en plus. Combien a-t'il de bonbons ?", "5", 1,"CP"),
(4,"Une personne prend l'avion à 14 heures. Elle laisse sa voiture sur un parking, place n°185. Elle la reprendra 8 jours après. Une journée sur le parking coûte 7 € . Quelle somme a payé la personne en reprenant sa voiture ?","56",1,"CE2"),
(5,"Valentine collectionne les timbres depuis 5 ans. Elle possède 237 timbres français et 79 timbres étrangers. Elle a 29 timbres anglais, 18 allemands, 4 suisses, 23 italiens et 5 belges. Combien de timbres Valentine possède-t-elle?","316",1,"CE2"),
(6,"Une personne emmène sa voiture au garage pour la révision des 20000 km. Le soir, vers 18h00, le mécanicien lui donne la facture suivante : Huile : 13 € Filtre à air : 5 € Nettoyage du carburateur : 10€ Essuie-glaces : 4 € Quel est le montant de la facture ?","32",1,"CE2"),
(7,"Calcul mental : 4x25=","100",1,"CM2"),
(9,"Calcul mental : 12x5=","60",1,"CM2"),
(10,"Pour aller chez max, Paul a 600 m à faire En partant de chez Max, il doit faire 250 m de plus pour se rendre chez Alan. Quelle distance sépare la maison de Paul et celle d’Alan ?","850",1,"CM1"),
(11,"Trouvez dans la phrase suivante s’il y a un COD ou un COI : Je conduis la voiture.","cod",2,"CM1"),
(12,"Trouvez dans la phrase suivante s’il y a un COD ou un COI : Maman fait les gâteaux.","cod",2,"CM1"),
(13,"Trouvez dans la phrase suivante s’il y a un COD ou un COI : Pascal parle à son frère.","coi",2,"CM1"),
(14,"Trouvez dans la phrase suivante s’il y a un COD ou un CII : Sébastien se souvient de sa leçon.","coi",2,"CM1");

  
  
INSERT INTO aide VALUES
(1,"Rappel de conjugaison, pour le premier groupe, je -> e, tu -> es, il/elle/on -> e, nous -> ons, vous -> ez, ils/elles -> ent Pour le deuxieme  groupe, je -> is, tu -> is, il/elle/on -> it, nous -> issons, vous -> issez, ils/elles -> issent Et pour le troisième  groupe, je -> s, tu -> s, il/elle/on -> t, nous -> ons, vous -> ez, ils/elles -> ent",2),
(2,"Si on donne quelque chose en plus de ce qu'on a deja il faut additioner ce qu'on a au depart avec ce qu'on nous donne. Par exemple si on a 5 pommes et qu’on nous donne 10 pommes on fait 5+10=15, on a 15 pommes",1),
(3,"Rappel COD COI : Pour trouver le COD il faut se poser la question « qui ? » ou « quoi ? » par exemple : Paul fait du velo.  Qui fais du velo ? Pour le COI il faut ce poser la question « à qui ? », « à quoi ? » par exemple : la chemise a carreaux appartient a caroline. A qui appartient la chemise a carreaux ? ",2);
