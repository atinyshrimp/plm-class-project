CREATE TABLE IF NOT EXISTS `Product_info` (
	`id` integer primary key NOT NULL UNIQUE,
	`nom` TEXT NOT NULL,
	`description_étiquettes` TEXT NOT NULL,
	`quantité` REAL NOT NULL,
	`photo_étiquettes` TEXT NOT NULL,
	`id_contenant` INTEGER NOT NULL,
	`photo` TEXT NOT NULL,
	`version` INTEGER NOT NULL,
	`date_mise_en_prod` REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS `Details_Couts` (
	`id` integer primary key NOT NULL UNIQUE,
	`cout_prod` REAL NOT NULL,
	`cout_matieres_premieres` REAL NOT NULL,
	`prix_de_vente` REAL NOT NULL,
	`id_produit` INTEGER NOT NULL,
	`cout_marketing` INTEGER NOT NULL,
FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`)
);
CREATE TABLE IF NOT EXISTS `Ingredients` (
	`id` integer primary key NOT NULL UNIQUE,
	`nom` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Composition_produit` (
	`id` integer primary key NOT NULL UNIQUE,
	`id_produit` INTEGER NOT NULL,
	`quantité` REAL NOT NULL,
	`id_ingredient` INTEGER NOT NULL,
FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`),
FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`)
);
CREATE TABLE IF NOT EXISTS `Fournisseurs/Distributeurs` (
	`id` integer primary key NOT NULL UNIQUE,
	`nom` TEXT NOT NULL,
	`localisation` TEXT NOT NULL,
	`contact` TEXT NOT NULL,
	`type` BOOLEAN NOT NULL
);
CREATE TABLE IF NOT EXISTS `Marchandises` (
	`id` integer primary key NOT NULL UNIQUE,
	`date_contractualisation` REAL NOT NULL,
	`date_livraison` REAL NOT NULL,
	`id_ingredient` INTEGER NOT NULL,
	`quantité_kg` REAL NOT NULL,
	`id_usine_livraison` INTEGER NOT NULL,
	`id_fournisseur` INTEGER NOT NULL,
FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`),
FOREIGN KEY(`id_usine_livraison`) REFERENCES `Usines_entrepots`(`id`),
FOREIGN KEY(`id_fournisseur`) REFERENCES `Fournisseurs/Distributeurs`(`id`)
);
CREATE TABLE IF NOT EXISTS `Usines_entrepots` (
	`id` integer primary key NOT NULL UNIQUE,
	`localisation` TEXT NOT NULL,
	`contact` TEXT NOT NULL,
	`type` BOOLEAN NOT NULL
);
CREATE TABLE IF NOT EXISTS `Process` (
	`id_usine` INTEGER NOT NULL,
	`id_process_type` INTEGER NOT NULL,
	`date` REAL NOT NULL,
	`id` INTEGER NOT NULL,
	`id_marchandise` INTEGER,
	`id_ingredient` INTEGER NOT NULL,
FOREIGN KEY(`id_usine`) REFERENCES `Usines/entrepots`(`id`),
FOREIGN KEY(`id_process_type`) REFERENCES `Process_type`(`id`),
FOREIGN KEY(`id_marchandise`) REFERENCES `Marchandises`(`id`),
FOREIGN KEY(`id_ingredient`) REFERENCES `Ingredients`(`id`)
);
CREATE TABLE IF NOT EXISTS `Process_type` (
	`id` integer primary key NOT NULL UNIQUE,
	`name` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Lots` (
	`id` integer primary key NOT NULL UNIQUE,
	`date_de_prod` REAL,
	`date_de_peremption` REAL,
	`id_produit` INTEGER NOT NULL,
	`quantite` INTEGER NOT NULL,
	`statut` BOOLEAN NOT NULL,
	`retour` BOOLEAN,
FOREIGN KEY(`id_produit`) REFERENCES `Product_info`(`id`)
);
CREATE TABLE IF NOT EXISTS `Stock` (
	`id` integer primary key NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`date_arrivee` REAL NOT NULL,
FOREIGN KEY(`id_entrepot`) REFERENCES `Usines/entrepots`(`id`),
FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`)
);
CREATE TABLE IF NOT EXISTS `Historique_process` (
	`id_lot` INTEGER NOT NULL,
	`id_process` INTEGER NOT NULL,
FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
FOREIGN KEY(`id_process`) REFERENCES `Process`(`id`)
);
CREATE TABLE IF NOT EXISTS `Distributions` (
	`id` integer primary key NOT NULL UNIQUE,
	`id_entrepot` INTEGER NOT NULL,
	`id_lot` INTEGER NOT NULL,
	`id_distributeur` INTEGER NOT NULL,
	`date_contractualisation` REAL NOT NULL,
	`date_livraison` REAL NOT NULL,
FOREIGN KEY(`id_entrepot`) REFERENCES `Usines/entrepots`(`id`),
FOREIGN KEY(`id_lot`) REFERENCES `Lots`(`id`),
FOREIGN KEY(`id_distributeur`) REFERENCES `Fournisseurs/Distributeurs`(`id`)
);