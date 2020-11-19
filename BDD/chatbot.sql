CREATE SCHEMA CHATBOT;
USE CHATBOT;
CREATE TABLE matiere(
    idMatiere INTEGER PRIMARY KEY,
    nom VARCHAR(27)
    );

CREATE TABLE exercice(
    idEx INTEGER PRIMARY KEY,
    enonce TEXT,
    reponse TEXT,
    idMatiere INTEGER,
    classe varchar(3),
    CONSTRAINT fk_matiere_ex FOREIGN KEY (idMatiere) REFERENCES matiere(idMatiere)
    );

CREATE TABLE aide (
    idAide INTEGER PRIMARY KEY,
    indice TEXT,
    idMatiere INTEGER,
    CONSTRAINT fk_matiere_aide FOREIGN KEY (idMatiere) REFERENCES matiere(idMatiere)
    );


