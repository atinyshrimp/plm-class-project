-- INIT database
-- 1. Création des tables sans clés étrangères
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
	`cout_marketing` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Ingredients` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`nom` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Composition_produit` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_produit` INTEGER NOT NULL,
	`quantité` REAL NOT NULL,
	`id_ingredient` INTEGER NOT NULL
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
	`id_fournisseur` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Process_type` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`name` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Process` (
	`id_usine` INTEGER NOT NULL,
	`id_process_type` INTEGER NOT NULL,
	`date` DATE NOT NULL,
	`id` INTEGER NOT NULL PRIMARY KEY,
	`id_marchandise` INTEGER,
	`id_ingredient` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Stock` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`date_arrivee` DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS `Lots` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`date_de_prod` DATE,
	`date_de_peremption` DATE,
	`id_produit` INTEGER NOT NULL,
	`quantité` INTEGER NOT NULL,
	`statut` INTEGER NOT NULL,
	`retour` INTEGER
);

CREATE TABLE IF NOT EXISTS `Historique_process` (
	`id_lot` INTEGER NOT NULL,
	`id_process` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Distributions` (
	`id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`id_distributeur` INTEGER NOT NULL,
	`date_contractualisation` DATE NOT NULL,
	`date_livraison` DATE NOT NULL
);

-- 2. Ajout des clés étrangères (FOREIGN KEY) après la création des tables

-- Foreign Key pour `Details_Couts`
ALTER TABLE `Details_Couts`
ADD FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`);

-- Foreign Key pour `Composition_produit`
ALTER TABLE `Composition_produit`
ADD FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`),
ADD FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`);

-- Foreign Key pour `Marchandises`
ALTER TABLE `Marchandises`
ADD FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`),
ADD FOREIGN KEY(`id_usine_livraison`) REFERENCES `Usines_entrepots`(`id`),
ADD FOREIGN KEY(`id_fournisseur`) REFERENCES `Fournisseurs_Distributeurs`(`id`);

-- Foreign Key pour `Process`
ALTER TABLE `Process`
ADD FOREIGN KEY(`id_usine`) REFERENCES `Usines_entrepots`(`id`),
ADD FOREIGN KEY(`id_process_type`) REFERENCES `Process_type`(`id`),
ADD FOREIGN KEY(`id_marchandise`) REFERENCES `Marchandises`(`id`),
ADD FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`);

-- Foreign Key pour `Stock`
ALTER TABLE `Stock`
ADD FOREIGN KEY(`id_entrepot`) REFERENCES `Usines_entrepots`(`id`),
ADD FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`);

-- Foreign Key pour `Lots`
ALTER TABLE `Lots`
ADD FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`);

-- Foreign Key pour `Historique_process`
ALTER TABLE `Historique_process`
ADD FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
ADD FOREIGN KEY(`id_process`) REFERENCES `Process`(`id`);

-- Foreign Key pour `Distributions`
ALTER TABLE `Distributions`
ADD FOREIGN KEY(`id_entrepot`) REFERENCES `Usines_entrepots`(`id`),
ADD FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
ADD FOREIGN KEY(`id_distributeur`) REFERENCES `Fournisseurs_Distributeurs`(`id`);



-- INSERT DATA
-- (Data remains unchanged)




INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES (1, 'Product 1', 'Description for product 1', 45.97, 'photo_1_label.png', 5, 'photo_1.png', 8, '2024-11-29T17:26:57.980471');
INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES (2, 'Product 2', 'Description for product 2', 87.00, 'photo_2_label.png', 4, 'photo_2.png', 7, '2024-11-29T17:26:57.980490');
INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES (3, 'Product 3', 'Description for product 3', 24.39, 'photo_3_label.png', 5, 'photo_3.png', 3, '2024-11-29T17:26:57.980501');
INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES (4, 'Product 4', 'Description for product 4', 17.44, 'photo_4_label.png', 1, 'photo_4.png', 10, '2024-11-29T17:26:57.980516');
INSERT INTO Product_info (id, nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod) VALUES (5, 'Product 5', 'Description for product 5', 55.60, 'photo_5_label.png', 1, 'photo_5.png', 9, '2024-11-29T17:26:57.980525');
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES (1, 32.60, 16.32, 81.85, 1, 1744);
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES (2, 16.96, 11.30, 53.22, 2, 3928);
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES (3, 17.34, 6.29, 88.30, 3, 4620);
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES (4, 15.17, 12.43, 79.95, 4, 4402);
INSERT INTO Details_Couts (id, cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing) VALUES (5, 42.60, 19.62, 68.00, 5, 1164);
INSERT INTO Ingredients (id, nom) VALUES (1, 'Ingredient 1');
INSERT INTO Ingredients (id, nom) VALUES (2, 'Ingredient 2');
INSERT INTO Ingredients (id, nom) VALUES (3, 'Ingredient 3');
INSERT INTO Ingredients (id, nom) VALUES (4, 'Ingredient 4');
INSERT INTO Ingredients (id, nom) VALUES (5, 'Ingredient 5');
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES (1, 5, 6.44, 3);
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES (2, 2, 1.81, 3);
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES (3, 3, 8.51, 3);
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES (4, 3, 7.18, 1);
INSERT INTO Composition_produit (id, id_produit, quantité, id_ingredient) VALUES (5, 1, 2.26, 1);

-- QUERY database
SELECT * FROM Product_info;
