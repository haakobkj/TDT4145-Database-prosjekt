--CREATE DATABASE KaffeDB;

CREATE TABLE Bruker (
	BrukerID INTEGER NOT NULL,
	Epost VARCHAR(320) NOT NULL,
	Passord VARCHAR(30),
	Navn VARCHAR(30),
	CONSTRAINT Bruker_PK PRIMARY KEY (BrukerID)
);

 CREATE TABLE Kaffesmaking (
	KaffesmakingID INTEGER NOT NULL, 
	Smaksnotater VARCHAR(255), 
	AntallPoeng INTEGER, 
	Smaksdato VARCHAR(30), 
	BrukerID INTEGER NOT NULL, 
	KaffeID INTEGER,
	CONSTRAINT Kaffesmaking_PK PRIMARY KEY (KaffesmakingID),
	CONSTRAINT Kaffesmaking_FK1 FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
		ON UPDATE CASCADE
		ON DELETE NO ACTION,
	CONSTRAINT Kaffesmaking_FK2 FOREIGN KEY (KaffeID) REFERENCES Kaffe (KaffeID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE Kaffe (
	KaffeID INTEGER NOT NULL,
	Navn VARCHAR(30),
	Kilopris INTEGER ,
	Beskrivelse VARCHAR(255),
	Brenningsgrad VARCHAR(30),
	Dato VARCHAR(30),
	KaffebrenneriID INTEGER ,
	KaffepartiID INTEGER ,
	CONSTRAINT Kaffe_PK PRIMARY KEY (KaffeID),
	CONSTRAINT Kaffe_FK1 FOREIGN KEY (KaffeBrenneriID) REFERENCES KaffeBrenneri (KaffeBrenneriID)
		ON UPDATE CASCADE
		ON DELETE NO ACTION,
	CONSTRAINT Kaffe_FK2 FOREIGN KEY (KaffepartiID) REFERENCES Kaffe (KaffepartiID)
		ON UPDATE CASCADE
		ON DELETE NO ACTION,
    CONSTRAINT Unik_kaffe UNIQUE (Navn, KaffebrenneriID, Dato)
);


CREATE TABLE Kaffebrenneri (
	KaffebrenneriID INTEGER NOT NULL,
	Navn VARCHAR(30) UNIQUE,
	CONSTRAINT Kafferbrenneri_PK PRIMARY KEY(KaffebrenneriID)
);


CREATE TABLE Gaard (
	GaardsID INTEGER NOT NULL,
	Navn VARCHAR(30), 
	Region VARCHAR(30),
	HøydeOverHavet INTEGER,
	CONSTRAINT Gaard_PK PRIMARY KEY (GaardsID),
	CONSTRAINT Gaard_FK FOREIGN KEY (Region) REFERENCES RegionILand (Region)
		ON UPDATE CASCADE
		ON DELETE NO ACTION
);

CREATE TABLE RegionILand (
	Region VARCHAR(30) NOT NULL,
	Land VARCHAR(30) NOT NULL,
	CONSTRAINT RegionILand_PK PRIMARY KEY (Region, Land)
);


	
CREATE TABLE Kaffeparti ( 
	KaffepartiID INTEGER NOT NULL,
	Innhoestingsaar INTEGER,
	Pris INTEGER,
	ForedlingsmetodeID INTEGER,
	GaardsID INTEGER,
	CONSTRAINT Kaffeparti_PK PRIMARY KEY (KaffepartiID),
	CONSTRAINT Kaffeparti_FK1 FOREIGN KEY (ForedlingsmetodeID) REFERENCES Foredlingsmetode (ForedlingsmetodeID)
		ON UPDATE CASCADE
		ON DELETE NO ACTION,
	CONSTRAINT Kaffeparti_FK2 FOREIGN KEY (GaardsID) REFERENCES Gaard (GaardsID)
		ON UPDATE CASCADE
		ON DELETE NO ACTION
);

CREATE TABLE Kaffeboenne (
	KaffeboenneID INTEGER NOT NULL,
	Navn VARCHAR(30) NOT NULL,
	Art VARCHAR(30),
	CONSTRAINT KaffeBoenne_PK PRIMARY KEY (KaffeboenneID)
);

CREATE TABLE Foredlingsmetode (
	ForedlingsmetodeID INTEGER NOT NULL,
	Navn VARCHAR(30),
	Beskrivelse VARCHAR(255),
	CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (ForedlingsmetodeID)
);


CREATE TABLE DelAv (
	KaffepartiID INTEGER NOT NULL,
	KaffeboenneID INTEGER NOT NULL,
	CONSTRAINT DelAv_PK PRIMARY KEY (KaffepartiID, KaffeboenneID),
	CONSTRAINT DelAv_FK1 FOREIGN KEY (KaffepartiID) REFERENCES Kaffeparti (KaffepartiID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT DelAv_FK2 FOREIGN KEY (KaffeboenneID) REFERENCES Kaffeboenne (KaffeboenneID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE DyrkesPaa (
	GaardsID INTEGER NOT NULL,
	KaffeboenneID VARCHAR(30) NOT NULL,
	CONSTRAINT DyrkesPaa_PK PRIMARY KEY (GaardsID, KaffeboenneID)
	CONSTRAINT DyrkesPaa_FK1 FOREIGN KEY (GaardsID) REFERENCES Gaard (GaardsID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT DyrkesPaa_FK2 FOREIGN KEY (KaffeboenneID) REFERENCES Kaffeboenne (KaffeboenneID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

--Innsetting av data i databasen
INSERT INTO Bruker VALUES (1, "test@gmail.com", "test", "Test testesen");
INSERT INTO Bruker VALUES (2, "ola@gmail.com", "1234", "Ola Normann");
INSERT INTO Bruker VALUES (3, "kari@gmail.com", "1234", "Kari Jensen");
INSERT INTO Bruker VALUES (4, "mohammed@gmail.com", "1234", "Mohammed Olsen");
INSERT INTO Bruker VALUES (5, "jens@gmail.com", "1234", "Jens Hansen");

INSERT INTO Kaffebrenneri VALUES (1, "Friele");
INSERT INTO Kaffebrenneri VALUES (2, "Ali");
INSERT INTO Kaffebrenneri VALUES (3, "Coop");
INSERT INTO Kaffebrenneri VALUES (4, "Kjeldsberg");
INSERT INTO Kaffebrenneri VALUES (5, "Evergood");
INSERT INTO Kaffebrenneri VALUES (6, "Jacobsen & Svart");


INSERT INTO Foredlingsmetode VALUES (1, "Bærtørket", "Bærtørket"); --Fra brukerhistorie 1
INSERT INTO Foredlingsmetode VALUES (2, "Vasket", "Vasket for hånd");
INSERT INTO Foredlingsmetode VALUES (3, "Renset", "Renset for hånd");

INSERT INTO Gaard VALUES (1, "Nombre de Dios", "Santa Ana", 1500); --Fra brukerhistorie 1
INSERT INTO Gaard VALUES (2, "Coffefarm", "Kabuga", 1200);
INSERT INTO Gaard VALUES (3, "Coffee 213", "Kabarando", 1100);
INSERT INTO Gaard VALUES (4, "El Farmito", "Medellin", 1495);
INSERT INTO Gaard VALUES (5, "El Farm", "Bogota", 2640);

INSERT INTO RegionILand VALUES ("Santa Ana", "El Salvador"); --Fra brukerhistorie 1
INSERT INTO RegionILand VALUES ("Kabuga", "Rwanda");
INSERT INTO RegionILand VALUES ("Kabarando", "Rwanda");
INSERT INTO RegionILand VALUES ("Medellin", "Colombia");
INSERT INTO RegionILand VALUES ("Bogota", "Colombia");

INSERT INTO Kaffeparti VALUES (1, 2021, 8, 1, 1); --Fra brukerhistorie 1
INSERT INTO Kaffeparti VALUES (2, 2022, 10, 2, 2);
INSERT INTO Kaffeparti VALUES (3, 2022, 6, 3, 3);
INSERT INTO Kaffeparti VALUES (4, 2022, 4, 2, 4);
INSERT INTO Kaffeparti VALUES (5, 2022, 3, 3, 5);

INSERT INTO Kaffeboenne VALUES (1, "Bourbon", "c. arabica"); --Fra brukerhistorie 1
INSERT INTO Kaffeboenne VALUES (2, "Mocha Java", "c. arabica");

INSERT INTO DelAv VALUES (1, 1); --Fra brukerhistorie 1
INSERT INTO DelAv VALUES (2, 2);
INSERT INTO DelAv VALUES (3, 1);
INSERT INTO DelAv VALUES (4, 2);
INSERT INTO DelAv VALUES (5, 1);

INSERT INTO DyrkesPaa VALUES (1, 1);
INSERT INTO DyrkesPaa VALUES (2, 1);
INSERT INTO DyrkesPaa VALUES (3, 1);
INSERT INTO DyrkesPaa VALUES (4, 1);
INSERT INTO DyrkesPaa VALUES (5, 1);
INSERT INTO DyrkesPaa VALUES (1, 2);
INSERT INTO DyrkesPaa VALUES (2, 2);
INSERT INTO DyrkesPaa VALUES (3, 2);

INSERT INTO Kaffe VALUES (1, "Frokostkaffe", 150, "Fyldig og aromatisk", "Medium brent", "22/11/2021", 1, 1);
INSERT INTO Kaffe VALUES (2, "Morgenkaffe", 120, "Kurerer gruff", "Medium brent","11/03/2022", 2, 2);
INSERT INTO Kaffe VALUES (3, "Påskekaffe", 280, "Floral", "Lysbrent", "12/02/2022", 3, 3);
INSERT INTO Kaffe VALUES (4, "Ettermiddagskaffe", 200, "Fyldig og aromatisk", "Mørkbrent", "11/01/2022", 4, 4);
INSERT INTO Kaffe VALUES (5, "Filterkaffe", 170, "Floral", "Medium", "14/02/2022", 5, 5);
INSERT INTO Kaffe VALUES (6, "Vinterkaffe 2022", 600, "En velsmakende og kompleks kaffe for mørketiden", "Lysbrent", "20/01/2022",6, 1); --fra brukerhistorie 1

INSERT INTO Kaffesmaking VALUES (1, "Floral", 7, "22/03/2021", 2, 2);
INSERT INTO Kaffesmaking VALUES (2, "Floral", 8, "22/03/2022", 2, 3);
INSERT INTO Kaffesmaking VALUES (3, "Floral", 7, "22/03/2022", 2, 3);
INSERT INTO Kaffesmaking VALUES (4, "Floral", 7, "22/03/2022", 2, 5);

INSERT INTO Kaffesmaking VALUES (5, "Digg", 8, "22/03/2021", 3, 1);
INSERT INTO Kaffesmaking VALUES (6, "Bitter", 5, "22/03/2021", 3, 3);
INSERT INTO Kaffesmaking VALUES (7, "Fantastisk", 9, "22/03/2022", 3, 4);

INSERT INTO Kaffesmaking VALUES (8, "Helt grei", 4, "22/03/2022", 4, 2);
INSERT INTO Kaffesmaking VALUES (9, "Veldig god", 7, "22/03/2022", 4, 5);
INSERT INTO Kaffesmaking VALUES (10, "Floral", 10, "22/03/2022", 4, 6);

INSERT INTO Kaffesmaking VALUES (11, "Fantastisk", 10, "22/03/2022", 5, 6);



