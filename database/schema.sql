-- INIT database
-- 1. Création des tables avec clés étrangères incluses

CREATE TABLE IF NOT EXISTS `Product_info` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`nom` TEXT NOT NULL,
	`description_étiquettes` TEXT NOT NULL,
	`quantité` REAL NOT NULL,
	`photo_étiquettes` TEXT NOT NULL,
	`id_contenant` INTEGER NOT NULL,
	`photo` TEXT NOT NULL,
	`version` INTEGER NOT NULL,
	`date_mise_en_prod` DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS `Details_Couts` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`cout_prod` REAL NOT NULL,
	`cout_matieres_premieres` REAL NOT NULL,
	`prix_de_vente` REAL NOT NULL,
	`id_produit` INTEGER NOT NULL,
	`cout_marketing` INTEGER NOT NULL,
	FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`)
);

CREATE TABLE IF NOT EXISTS `Ingredients` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`nom` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Composition_produit` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_produit` INTEGER NOT NULL,
	`quantité` REAL NOT NULL,
	`id_ingredient` INTEGER NOT NULL,
	FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`),
	FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`)
);

CREATE TABLE IF NOT EXISTS `Fournisseurs_Distributeurs` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`nom` TEXT NOT NULL,
	`localisation` TEXT NOT NULL,
	`contact` TEXT NOT NULL,
	`type` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Usines_entrepots` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`localisation` TEXT NOT NULL,
	`contact` TEXT NOT NULL,
	`type` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Marchandises` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`date_contractualisation` DATE NOT NULL,
	`date_livraison` DATE NOT NULL,
	`id_ingredient` INTEGER NOT NULL,
	`quantité_kg` REAL NOT NULL,
	`id_usine_livraison` INTEGER NOT NULL,
	`id_fournisseur` INTEGER NOT NULL,
	FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`),
	FOREIGN KEY(`id_usine_livraison`) REFERENCES `Usines_entrepots`(`id`),
	FOREIGN KEY(`id_fournisseur`) REFERENCES `Fournisseurs_Distributeurs`(`id`)
);

CREATE TABLE IF NOT EXISTS `Process_type` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`name` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Process` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_usine` INTEGER NOT NULL,
	`id_process_type` INTEGER NOT NULL,
	`date` DATE NOT NULL,
	`id_marchandise` INTEGER,
	`id_ingredient` INTEGER NOT NULL,
	FOREIGN KEY(`id_usine`) REFERENCES `Usines_entrepots`(`id`),
	FOREIGN KEY(`id_process_type`) REFERENCES `Process_type`(`id`),
	FOREIGN KEY(`id_marchandise`) REFERENCES `Marchandises`(`id`),
	FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`)
);

CREATE TABLE IF NOT EXISTS `Stock` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`date_arrivee` DATE NOT NULL,
	FOREIGN KEY(`id_entrepot`) REFERENCES `Usines_entrepots`(`id`),
	FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`)
);

CREATE TABLE IF NOT EXISTS `Lots` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`date_de_prod` DATE,
	`date_de_peremption` DATE,
	`id_produit` INTEGER NOT NULL,
	`quantité` INTEGER NOT NULL,
	`statut` INTEGER NOT NULL,
	`retour` INTEGER,
	FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`)
);

CREATE TABLE IF NOT EXISTS `Historique_process` (
	`id_lot` INTEGER NOT NULL,
	`id_process` INTEGER NOT NULL,
	FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
	FOREIGN KEY(`id_process`) REFERENCES `Process`(`id`)
);

CREATE TABLE IF NOT EXISTS `Distributions` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`id_distributeur` INTEGER NOT NULL,
	`date_contractualisation` DATE NOT NULL,
	`date_livraison` DATE NOT NULL,
	FOREIGN KEY(`id_entrepot`) REFERENCES `Usines_entrepots`(`id`),
	FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
	FOREIGN KEY(`id_distributeur`) REFERENCES `Fournisseurs_Distributeurs`(`id`)
);




-- Insertion des données dans Product_info
INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES
(1, 'Shampooing Naturel', 'Shampooing à base de plantes', 500, 'shampooing_label.png', 1, 'shampooing.png', 1, '2023-05-10'),
(2, 'Savon Bio', 'Savon fait à la main', 300, 'savon_label.png', 2, 'savon.png', 1, '2023-07-15');

-- Insertion des données dans Details_Couts
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES
(1, 2.50, 1.20, 5.00, 1, 0.50),
(2, 1.50, 0.80, 3.00, 2, 0.30);

-- Insertion des données dans Ingredients
INSERT INTO Ingredients (id, nom) VALUES
(1, 'Huile essentielle'),
(2, 'Aloe Vera'),
(3, 'Beurre de karité');

-- Insertion des données dans Composition_produit
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES
(1, 1, 100, 1),
(2, 1, 200, 2),
(3, 2, 150, 3);

-- Insertion des données dans Fournisseurs_Distributeurs
INSERT INTO Fournisseurs_Distributeurs (id, nom, localisation, contact, type) VALUES
(1, 'Fournisseur Naturel', 'Paris', 'contact@naturel.com', 1),
(2, 'Distributeur Bio', 'Lyon', 'contact@bio.com', 2);

-- Insertion des données dans Usines_entrepots
INSERT INTO Usines_entrepots (id, localisation, contact, type) VALUES
(1, 'Usine Marseille', 'contact@usine.com', 1),
(2, 'Entrepôt Lille', 'contact@entrepot.com', 2);

-- Insertion des données dans Marchandises
INSERT INTO Marchandises (id, date_contractualisation, date_livraison, id_ingredient, quantité_kg, id_usine_livraison, id_fournisseur) VALUES
(1, '2023-04-01', '2023-04-15', 1, 50, 1, 1),
(2, '2023-06-10', '2023-06-20', 2, 30, 1, 1);

-- Insertion des données dans Process_type
INSERT INTO Process_type (id, name) VALUES
(1, 'Mélange'),
(2, 'Conditionnement');

-- Insertion des données dans Process
INSERT INTO Process (id, id_usine, id_process_type, date, id_marchandise, id_ingredient) VALUES
(1, 1, 1, '2023-05-01', 1, 1),
(2, 1, 2, '2023-05-02', 2, 2);

-- Insertion des données dans Lots
INSERT INTO Lots (id, date_de_prod, date_de_peremption, id_produit, quantité, statut, retour) VALUES
(1, '2023-05-10', '2024-05-10', 1, 100, 1, 0),
(2, '2023-07-15', '2024-07-15', 2, 50, 1, 0);

-- Insertion des données dans Stock
INSERT INTO Stock (id, id_entrepot, id_lot, date_arrivee) VALUES
(1, 2, 1, '2023-05-20'),
(2, 2, 2, '2023-07-18');

-- Insertion des données dans Historique_process
INSERT INTO Historique_process (id_lot, id_process) VALUES
(1, 1),
(2, 2);

-- Insertion des données dans Distributions
INSERT INTO Distributions (id, id_entrepot, id_lot, id_distributeur, date_contractualisation, date_livraison) VALUES
(1, 2, 1, 2, '2023-05-22', '2023-05-25'),
(2, 2, 2, 2, '2023-07-20', '2023-07-25');

-- QUERY database
SELECT * FROM Product_info;
