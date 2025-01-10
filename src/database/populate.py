import sqlite3

# Donnees pour les produits
PRODUITS = [
    {
        "id": 1,
        "nom": "Miel de lavande maritime",
        "description_etiquettes": "Miel de lavande maritime de la Côte d’Azur, recolte entre juin et août.",
        "quantite": 500,
        "photo_etiquettes": "miel_lavande.jpg",
        "id_contenant": 1,
        "photo": "miel_lavande_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-06-01",
    },
    {
        "id": 2,
        "nom": "Miel de sarrasin",
        "description_etiquettes": "Miel de sarrasin recolte entre août et septembre en Bretagne, France et Pays-Bas.",
        "quantite": 500,
        "photo_etiquettes": "miel_sarrasin.jpg",
        "id_contenant": 1,
        "photo": "miel_sarrasin_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-08-01",
    },
    {
        "id": 3,
        "nom": "Confiture de pêche de vigne",
        "description_etiquettes": "Confiture artisanale de pêche de vigne, France et Espagne, août-septembre.",
        "quantite": 800,
        "photo_etiquettes": "confiture_peche.jpg",
        "id_contenant": 2,
        "photo": "confiture_peche_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-08-01",
    },
    {
        "id": 4,
        "nom": "Confiture de rhubarbe",
        "description_etiquettes": "Confiture de rhubarbe recoltee entre avril et juin en Belgique et aux Pays-Bas.",
        "quantite": 800,
        "photo_etiquettes": "confiture_rhubarbe.jpg",
        "id_contenant": 2,
        "photo": "confiture_rhubarbe_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-04-01",
    },
    {
        "id": 5,
        "nom": "Miel de jujubier",
        "description_etiquettes": "Miel de jujubier recolte entre septembre et decembre au Yemen et en Inde.",
        "quantite": 500,
        "photo_etiquettes": "miel_jujubier.jpg",
        "id_contenant": 1,
        "photo": "miel_jujubier_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-09-01",
    },
    {
        "id": 6,
        "nom": "Miel de the",
        "description_etiquettes": "Miel de the recolte entre mai et juillet en Chine et Japon.",
        "quantite": 500,
        "photo_etiquettes": "miel_the.jpg",
        "id_contenant": 1,
        "photo": "miel_the_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-05-01",
    },
    {
        "id": 7,
        "nom": "Confiture de fruit du dragon et mangue",
        "description_etiquettes": "Confiture realisee avec des fruits du dragon recoltes entre juin et octobre et des mangues recoltees entre mars et juin au Vietnam et en Thaïlande.",
        "quantite": 1000,
        "photo_etiquettes": "confiture_fruit_mangue.jpg",
        "id_contenant": 3,
        "photo": "confiture_fruit_mangue_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-03-01",
    },
    {
        "id": 8,
        "nom": "Miel d’eucalyptus",
        "description_etiquettes": "Miel d’eucalyptus recolte entre septembre et novembre en Afrique du Sud, et entre janvier et mars au Maroc.",
        "quantite": 500,
        "photo_etiquettes": "miel_eucalyptus.jpg",
        "id_contenant": 1,
        "photo": "miel_eucalyptus_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-09-01",
    },
    {
        "id": 9,
        "nom": "Confiture de goyave",
        "description_etiquettes": "Confiture realisee avec des goyaves recoltees entre septembre et decembre au Kenya, et entre fevrier et avril en Afrique du Sud.",
        "quantite": 1000,
        "photo_etiquettes": "confiture_goyave.jpg",
        "id_contenant": 3,
        "photo": "confiture_goyave_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2023-09-01",
    },
    {
        "id": 10,
        "nom": "Confiture de dattes",
        "description_etiquettes": "Confiture realisee avec des dattes recoltees entre août et novembre en Tunisie et egypte.",
        "quantite": 1000,
        "photo_etiquettes": "confiture_dattes.jpg",
        "id_contenant": 3,
        "photo": "confiture_dattes_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": "2024-08-01",
    }
]

# Donnees pour les coûts
DETAILS_COUTS = [
    {
        "id": 1,
        "id_produit": 1,  # Correspond au premier produit dans `PRODUCTS`
        "cout_prod": 12.50,  # Coût total de production
        "cout_matieres_premieres": 10.50,  # Coût des matières premières
        "prix_de_vente": 18.00,  # Prix de vente final
        "cout_marketing": 2.00,  # Coût du marketing
    },
    {
        "id": 2,
        "id_produit": 2,
        "cout_prod": 13.20,
        "cout_matieres_premieres": 11.20,
        "prix_de_vente": 19.00,
        "cout_marketing": 2.50,
    },
    {
        "id": 3,
        "id_produit": 3,
        "cout_prod": 9.50,
        "cout_matieres_premieres": 7.50,
        "prix_de_vente": 14.00,
        "cout_marketing": 1.50,
    },
    {
        "id": 4,
        "id_produit": 4,
        "cout_prod": 8.80,
        "cout_matieres_premieres": 6.80,
        "prix_de_vente": 13.00,
        "cout_marketing": 1.20,
    },
    {
        "id": 5,
        "id_produit": 5,
        "cout_prod": 15.50,
        "cout_matieres_premieres": 13.50,
        "prix_de_vente": 22.00,
        "cout_marketing": 3.00,
    },
    {
        "id": 6,
        "id_produit": 6,
        "cout_prod": 11.10,
        "cout_matieres_premieres": 9.10,
        "prix_de_vente": 16.00,
        "cout_marketing": 2.00,
    },
    {
        "id": 7,
        "id_produit": 7,
        "cout_prod": 13.60,
        "cout_matieres_premieres": 11.60,
        "prix_de_vente": 20.00,
        "cout_marketing": 2.50,
    },
    {
        "id": 8,
        "id_produit": 8,
        "cout_prod": 12.20,
        "cout_matieres_premieres": 10.20,
        "prix_de_vente": 18.50,
        "cout_marketing": 2.30,
    },
    {
        "id": 9,
        "id_produit": 9,
        "cout_prod": 14.40,
        "cout_matieres_premieres": 12.40,
        "prix_de_vente": 21.00,
        "cout_marketing": 2.70,
    },
    {
        "id": 10,
        "id_produit": 10,
        "cout_prod": 10.80,
        "cout_matieres_premieres": 8.80,
        "prix_de_vente": 15.00,
        "cout_marketing": 1.80,
    },
]

# Donnees pour les ingredients
INGREDIENTS = [
    {"id": 1, "nom": "Miel de lavande maritime"},
    {"id": 2, "nom": "Miel de sarrasin"},
    {"id": 3, "nom": "Pêche de vigne"},
    {"id": 4, "nom": "Rhubarbe"},
    {"id": 5, "nom": "Miel de jujubier"},
    {"id": 6, "nom": "Miel de the"},
    {"id": 7, "nom": "Fruit du dragon"},
    {"id": 8, "nom": "Mangue"},
    {"id": 9, "nom": "Miel d’eucalyptus"},
    {"id": 10, "nom": "Goyave"},
    {"id": 11, "nom": "Datte"},
    {"id": 12, "nom": "Sucre"},
    {"id": 13, "nom": "Arôme de the"},
    {"id": 14, "nom": "Jus de citron"},
    {"id": 15, "nom": "Pectine"},
]

# Composition des produits : chaque entree represente un produit avec ses ingredients et quantites
COMPOSITION_PRODUIT = [
    # Miel de lavande maritime
    {"id": 1, "id_produit": 1, "quantite": 500, "id_ingredient": 1},  # Miel de lavande maritime

    # Miel de sarrasin
    {"id": 2, "id_produit": 2, "quantite": 500, "id_ingredient": 2},  # Miel de sarrasin

    # Confiture de pêche de vigne
    {"id": 3, "id_produit": 3, "quantite": 800, "id_ingredient": 3},  # Pêche de vigne
    {"id": 4, "id_produit": 3, "quantite": 300, "id_ingredient": 12}, # Sucre
    {"id": 5, "id_produit": 3, "quantite": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 6, "id_produit": 3, "quantite": 10, "id_ingredient": 15},  # Pectine

    # Confiture de rhubarbe
    {"id": 7, "id_produit": 4, "quantite": 800, "id_ingredient": 4},  # Rhubarbe
    {"id": 8, "id_produit": 4, "quantite": 300, "id_ingredient": 12}, # Sucre
    {"id": 9, "id_produit": 4, "quantite": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 10, "id_produit": 4, "quantite": 10, "id_ingredient": 15}, # Pectine

    # Miel de jujubier
    {"id": 11, "id_produit": 5, "quantite": 500, "id_ingredient": 5}, # Miel de jujubier

    # Miel de the
    {"id": 12, "id_produit": 6, "quantite": 500, "id_ingredient": 6},  # Miel de the
    {"id": 13, "id_produit": 6, "quantite": 10, "id_ingredient": 13},  # Arôme de the

    # Confiture de fruit du dragon et mangue
    {"id": 14, "id_produit": 7, "quantite": 500, "id_ingredient": 7},  # Fruit du dragon
    {"id": 15, "id_produit": 7, "quantite": 500, "id_ingredient": 8},  # Mangue
    {"id": 16, "id_produit": 7, "quantite": 300, "id_ingredient": 12}, # Sucre
    {"id": 17, "id_produit": 7, "quantite": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 18, "id_produit": 7, "quantite": 10, "id_ingredient": 15},  # Pectine

    # Miel d’eucalyptus
    {"id": 19, "id_produit": 8, "quantite": 500, "id_ingredient": 9},  # Miel d’eucalyptus

    # Confiture de goyave
    {"id": 20, "id_produit": 9, "quantite": 1000, "id_ingredient": 10}, # Goyave
    {"id": 21, "id_produit": 9, "quantite": 300, "id_ingredient": 12},  # Sucre
    {"id": 22, "id_produit": 9, "quantite": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 23, "id_produit": 9, "quantite": 10, "id_ingredient": 15},  # Pectine

    # Confiture de dattes
    {"id": 24, "id_produit": 10, "quantite": 1000, "id_ingredient": 11}, # Dattes
    {"id": 25, "id_produit": 10, "quantite": 300, "id_ingredient": 12},  # Sucre
    {"id": 26, "id_produit": 10, "quantite": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 27, "id_produit": 10, "quantite": 10, "id_ingredient": 15},  # Pectine
]

FOURNISSEURS_DISTRIBUTEURS = [
    {"id": 1, "nom": "Fournisseur Lavande Maritime", "localisation": "Côte d’Azur, France", "contact": "contact@lavandemaritime.fournisseur.com", "type": True},
    {"id": 2, "nom": "Fournisseur Sarrasin Bretagne", "localisation": "Bretagne, France", "contact": "contact@sarrasinbretagne.fournisseur.com", "type": True},
    {"id": 3, "nom": "Fournisseur Rhubarbe Belgique", "localisation": "Belgique", "contact": "contact@rhubarbebelgique.fournisseur.com", "type": True},
    {"id": 4, "nom": "Fournisseur Sarrasin Pays-Bas", "localisation": "Pays-Bas", "contact": "contact@sarrasinpaysbas.fournisseur.com", "type": True},
    {"id": 5, "nom": "Fournisseur Sidr Yemen", "localisation": "Yemen", "contact": "contact@sidryemen.fournisseur.com", "type": True},
    {"id": 6, "nom": "Fournisseur Pitaya Vietnam", "localisation": "Vietnam, Zones proches de Ho Chi Minh", "contact": "contact@pitayavietnam.fournisseur.com", "type": True},
    {"id": 7, "nom": "Fournisseur Miel de The Chine", "localisation": "Chine, Zhejiang", "contact": "contact@mieldethechine.fournisseur.com", "type": True},
    {"id": 8, "nom": "Fournisseur Miel de The Japon", "localisation": "Japon, Zhejiang", "contact": "contact@mieldethejapon.fournisseur.com", "type": True},
    {"id": 9, "nom": "Fournisseur Dattes Tunisie", "localisation": "Tozeur, Tunisie", "contact": "contact@dattestunisie.fournisseur.com", "type": True},
    {"id": 10, "nom": "Fournisseur Goyave Kenya", "localisation": "Regions côtières, Kenya", "contact": "contact@goyavekenya.fournisseur.com", "type": True},
    {"id": 11, "nom": "Fournisseur Eucalyptus Afrique du Sud", "localisation": "Provinces du Cap, Afrique du Sud", "contact": "contact@eucalyptusafriquedusud.fournisseur.com", "type": True},
    {"id": 12, "nom": "Distributeur Bangkok Thaïlande", "localisation": "Bangkok, Thaïlande", "contact": "contact@distributeurbangkok.com", "type": False},
    {"id": 13, "nom": "Distributeur Ho Chi Minh Vietnam", "localisation": "Ho Chi Minh Ville, Vietnam", "contact": "contact@distributeurhochiminh.com", "type": False},
    {"id": 14, "nom": "Distributeur Dakar Senegal", "localisation": "Dakar, Senegal", "contact": "contact@distributeurdakar.com", "type": False},
    {"id": 15, "nom": "Distributeur Mombasa Kenya", "localisation": "Mombasa, Kenya", "contact": "contact@distributeurmombasa.com", "type": False},
    {"id": 16, "nom": "Distributeur Paris Bruxelles", "localisation": "Paris, France / Bruxelles, Belgique", "contact": "contact@distributeurparisbruxelles.com", "type": False}
]

MARCHANDISES = [
        {
            "id": 1,
            "date_contractualisation": "2024-06-01",
            "date_livraison": "2024-06-15",
            "id_ingredient": 1,  # Miel de lavande maritime
            "quantite_kg": 100,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 2,
            "date_contractualisation": "2024-08-01",
            "date_livraison": "2024-08-20",
            "id_ingredient": 2,  # Miel de sarrasin
            "quantite_kg": 150,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 3,
            "date_contractualisation": "2024-08-01",
            "date_livraison": "2024-08-25",
            "id_ingredient": 3,  # Pêche de vigne
            "quantite_kg": 200,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 4,
            "date_contractualisation": "2024-04-01",
            "date_livraison": "2024-04-15",
            "id_ingredient": 4,  # Rhubarbe
            "quantite_kg": 250,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 5,
            "date_contractualisation": "2024-09-01",
            "date_livraison": "2024-09-15",
            "id_ingredient": 5,  # Miel de jujubier
            "quantite_kg": 100,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 6,
            "date_contractualisation": "2024-05-01",
            "date_livraison": "2024-05-20",
            "id_ingredient": 6,  # Miel de the
            "quantite_kg": 80,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 7,
            "date_contractualisation": "2024-03-01",
            "date_livraison": "2024-03-15",
            "id_ingredient": 7,  # Fruit du dragon
            "quantite_kg": 300,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 8,
            "date_contractualisation": "2024-03-01",
            "date_livraison": "2024-03-15",
            "id_ingredient": 8,  # Mangue
            "quantite_kg": 300,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 9,
            "date_contractualisation": "2024-09-01",
            "date_livraison": "2024-09-20",
            "id_ingredient": 9,  # Miel d’eucalyptus
            "quantite_kg": 120,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 10,
            "date_contractualisation": "2023-09-01",
            "date_livraison": "2023-09-15",
            "id_ingredient": 10,  # Goyave
            "quantite_kg": 150,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 11,
            "date_contractualisation": "2024-08-01",
            "date_livraison": "2024-08-30",
            "id_ingredient": 11,  # Datte
            "quantite_kg": 200,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 12,
            "date_contractualisation": "2024-08-01",
            "date_livraison": "2024-08-30",
            "id_ingredient": 12,  # Sucre
            "quantite_kg": 500,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 13,
            "date_contractualisation": "2024-04-01",
            "date_livraison": "2024-04-15",
            "id_ingredient": 13,  # Arôme de the
            "quantite_kg": 50,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 14,
            "date_contractualisation": "2024-04-01",
            "date_livraison": "2024-04-15",
            "id_ingredient": 14,  # Jus de citron
            "quantite_kg": 30,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 15,
            "date_contractualisation": "2024-04-01",
            "date_livraison": "2024-04-15",
            "id_ingredient": 15,  # Pectine
            "quantite_kg": 20,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        }
    ]

USINES_ENTREPOTS = [
    {"id": 1, "localisation": "Côte d’Azur, France", "contact": "contact@lavandemaritime.usine.com", "type": True},
    {"id": 2, "localisation": "Bretagne, France", "contact": "contact@sarrasinbretagne.usine.com", "type": True},
    {"id": 3, "localisation": "Belgique", "contact": "contact@rhubarbebelgique.usine.com", "type": True},
    {"id": 4, "localisation": "Pays-Bas", "contact": "contact@sarrasinpaysbas.usine.com", "type": True},
    {"id": 5, "localisation": "Yemen", "contact": "contact@sidryemen.usine.com", "type": True},
    {"id": 6, "localisation": "Vietnam, Zones proches de Ho Chi Minh", "contact": "contact@pitayavietnam.usine.com", "type": True},
    {"id": 7, "localisation": "Chine, Zhejiang", "contact": "contact@mieldethechine.usine.com", "type": True},
    {"id": 8, "localisation": "Japon, Zhejiang", "contact": "contact@mieldethejapon.usine.com", "type": True},
    {"id": 9, "localisation": "Tozeur, Tunisie", "contact": "contact@dattestunisie.usine.com", "type": True},
    {"id": 10, "localisation": "Regions côtières, Kenya", "contact": "contact@goyavekenya.usine.com", "type": True},
    {"id": 11, "localisation": "Provinces du Cap, Afrique du Sud", "contact": "contact@eucalyptusafriquedusud.usine.com", "type": True},

    {"id": 12, "localisation": "Bangkok, Thaïlande", "contact": "contact@bangkok.usine.com", "type": False},
    {"id": 13, "localisation": "Ho Chi Minh Ville, Vietnam", "contact": "contact@hochiminh.usine.com", "type": False},
    {"id": 14, "localisation": "Dakar, Senegal", "contact": "contact@dakar.usine.com", "type": False},
    {"id": 15, "localisation": "Mombasa, Kenya", "contact": "contact@mombasa.usine.com", "type": False},
    {"id": 16, "localisation": "Paris, France / Bruxelles, Belgique", "contact": "contact@parisbruxelles.usine.com", "type": False}
]

PROCESS_DATA = [
    # Miel de lavande maritime
    {"id_usine": 1, "id_process_type": 5, "date": "2024-06-01", "id": 1, "id_marchandise": 1, "id_ingredient": 1},  # maturation
    {"id_usine": 1, "id_process_type": 3, "date": "2024-06-10", "id": 2, "id_marchandise": 1, "id_ingredient": 1},  # Emballage
    {"id_usine": 16, "id_process_type": 4, "date": "2024-06-12", "id": 3, "id_marchandise": 1, "id_ingredient": 1},  # Conservation

    # Miel de sarrasin
    {"id_usine": 2, "id_process_type": 5, "date": "2024-06-01", "id": 4, "id_marchandise": 2, "id_ingredient": 2},  # maturation
    {"id_usine": 2, "id_process_type": 3, "date": "2024-06-15", "id": 5, "id_marchandise": 2, "id_ingredient": 2},  # Emballage
    {"id_usine": 16, "id_process_type": 4, "date": "2024-06-17", "id": 6, "id_marchandise": 2, "id_ingredient": 2},  # Conservation

    # Confiture de pêche de vigne
    {"id_usine": 2, "id_process_type": 1, "date": "2024-08-18", "id": 7, "id_marchandise": 3, "id_ingredient": 3},  # cuisson
    {"id_usine": 2, "id_process_type": 2, "date": "2024-08-20", "id": 8, "id_marchandise": 3, "id_ingredient": 3},  # Melange
    {"id_usine": 2, "id_process_type": 2, "date": "2024-08-20", "id": 9, "id_marchandise": 12, "id_ingredient": 12},  # Melange sucre
    {"id_usine": 2, "id_process_type": 2, "date": "2024-08-20", "id": 10, "id_marchandise": 14, "id_ingredient": 14},  # Melange citron
    {"id_usine": 2, "id_process_type": 2, "date": "2024-08-20", "id": 11, "id_marchandise": 15, "id_ingredient": 15},  # Melange peptine
    {"id_usine": 2, "id_process_type": 3, "date": "2024-08-22", "id": 12, "id_marchandise": 3, "id_ingredient": 3}, # Emballage
    {"id_usine": 16, "id_process_type": 4, "date": "2024-08-30", "id": 13, "id_marchandise": 3, "id_ingredient": 3},  # Conservation


    # Confiture de rhubarbe
    {"id_usine": 3, "id_process_type": 1, "date": "2024-04-18", "id": 14, "id_marchandise": 4, "id_ingredient": 4},  # cuisson
    {"id_usine": 3, "id_process_type": 2, "date": "2024-04-20", "id": 15, "id_marchandise": 4, "id_ingredient": 4},  # Melange
    {"id_usine": 3, "id_process_type": 2, "date": "2024-04-20", "id": 16, "id_marchandise": 12, "id_ingredient": 12},  # Melange sucre
    {"id_usine": 3, "id_process_type": 2, "date": "2024-04-20", "id": 17, "id_marchandise": 15, "id_ingredient": 15},  # Melange pectine
    {"id_usine": 3, "id_process_type": 2, "date": "2024-04-20", "id": 18, "id_marchandise": 14, "id_ingredient": 14},  # Melange citron
    {"id_usine": 3, "id_process_type": 3, "date": "2024-04-22", "id": 19, "id_marchandise": 4, "id_ingredient": 4},  # Emballage
    {"id_usine": 16, "id_process_type": 4, "date": "2024-04-30", "id": 20, "id_marchandise": 4, "id_ingredient": 4},  # Conservation

    # Miel de jujubier
    {"id_usine": 5, "id_process_type": 5, "date": "2024-09-01", "id": 21, "id_marchandise": 5, "id_ingredient": 5},  # maturation
    {"id_usine": 5, "id_process_type": 3, "date": "2024-09-10", "id": 22, "id_marchandise": 5, "id_ingredient": 5},  # Emballage
    {"id_usine": 12, "id_process_type": 4, "date": "2024-09-11", "id": 23, "id_marchandise": 5, "id_ingredient": 5},  # Conservation

    # Miel de the
    {"id_usine": 7, "id_process_type": 5, "date": "2024-05-01", "id": 24, "id_marchandise": 6, "id_ingredient": 6},  # maturation
    {"id_usine": 7, "id_process_type": 2, "date": "2024-05-15", "id": 25, "id_marchandise": 6, "id_ingredient": 6},  # Melange
    {"id_usine": 7, "id_process_type": 2, "date": "2024-05-15", "id": 26, "id_marchandise": 13, "id_ingredient": 13},  # Melange arôme de the
    {"id_usine": 7, "id_process_type": 3, "date": "2024-05-17", "id": 27, "id_marchandise": 6, "id_ingredient": 6},  # emballage
    {"id_usine": 12, "id_process_type": 4, "date": "2024-05-18", "id": 28, "id_marchandise": 6, "id_ingredient": 6},  # conservation
    
    # Confiture de fruit du dragon et mangue
    {"id_usine": 6, "id_process_type": 1, "date": "2024-03-01", "id": 29, "id_marchandise": 7, "id_ingredient": 7},  # cuisson
    {"id_usine": 6, "id_process_type": 1, "date": "2024-03-01", "id": 30, "id_marchandise": 8, "id_ingredient": 8},  # cuisson
    {"id_usine": 6, "id_process_type": 2, "date": "2024-03-03", "id": 31, "id_marchandise": 12, "id_ingredient": 12},  # Melange sucre
    {"id_usine": 6, "id_process_type": 2, "date": "2024-03-03", "id": 32, "id_marchandise": 15, "id_ingredient": 15},  # Melange pectine
    {"id_usine": 6, "id_process_type": 2, "date": "2024-03-03", "id": 33, "id_marchandise": 14, "id_ingredient": 14},  # Melange citron
    {"id_usine": 6, "id_process_type": 2, "date": "2024-03-03", "id": 34, "id_marchandise": 7, "id_ingredient": 7},  # Melange fruit du dragon
    {"id_usine": 6, "id_process_type": 2, "date": "2024-03-03", "id": 35, "id_marchandise": 8, "id_ingredient": 8},  # Melange mangue
    {"id_usine": 6, "id_process_type": 3, "date": "2024-03-05", "id": 36, "id_marchandise": 7, "id_ingredient": 7},  # Emballage
    {"id_usine": 12, "id_process_type": 4, "date": "2024-03-15", "id": 37, "id_marchandise": 7, "id_ingredient": 7},  # Conservation


    # Miel d’eucalyptus
    {"id_usine": 11, "id_process_type": 5, "date": "2024-09-01", "id": 38, "id_marchandise": 9, "id_ingredient": 9},  # maturation
    {"id_usine": 11, "id_process_type": 3, "date": "2024-09-20", "id": 39, "id_marchandise": 9, "id_ingredient": 9},  # Emballage
    {"id_usine": 15, "id_process_type": 4, "date": "2024-09-30", "id": 40, "id_marchandise": 9, "id_ingredient": 9},  # Conservation

    # Confiture de goyave
    {"id_usine": 10, "id_process_type": 1, "date": "2023-09-01", "id": 41, "id_marchandise": 10, "id_ingredient": 10},  # cuisson
    {"id_usine": 10, "id_process_type": 2, "date": "2024-09-03", "id": 42, "id_marchandise": 12, "id_ingredient": 12},  # Melange sucre
    {"id_usine": 10, "id_process_type": 2, "date": "2024-09-03", "id": 43, "id_marchandise": 15, "id_ingredient": 15},  # Melange pectine
    {"id_usine": 10, "id_process_type": 2, "date": "2024-09-03", "id": 44, "id_marchandise": 14, "id_ingredient": 14},  # Melange citron
    {"id_usine": 10, "id_process_type": 2, "date": "2023-09-03", "id": 45, "id_marchandise": 10, "id_ingredient": 10},  # Melange
    {"id_usine": 10, "id_process_type": 3, "date": "2024-09-05", "id": 46, "id_marchandise": 10, "id_ingredient": 10},  # Emballage
    {"id_usine": 12, "id_process_type": 4, "date": "2024-09-15", "id": 47, "id_marchandise": 10, "id_ingredient": 10},  # Conservation

    # Confiture de dattes
    {"id_usine": 9, "id_process_type": 1, "date": "2024-08-01", "id": 48, "id_marchandise": 11, "id_ingredient": 11},  # cuisson
    {"id_usine": 9, "id_process_type": 2, "date": "2024-08-03", "id": 49, "id_marchandise": 12, "id_ingredient": 12},  # Melange sucre
    {"id_usine": 9, "id_process_type": 2, "date": "2024-08-03", "id": 50, "id_marchandise": 15, "id_ingredient": 15},  # Melange pectine
    {"id_usine": 9, "id_process_type": 2, "date": "2024-08-03", "id": 51, "id_marchandise": 14, "id_ingredient": 14},  # Melange citron
    {"id_usine": 9, "id_process_type": 2, "date": "2023-08-03", "id": 52, "id_marchandise": 11, "id_ingredient": 11},  # Melange
    {"id_usine": 9, "id_process_type": 3, "date": "2024-08-05", "id": 53, "id_marchandise": 11, "id_ingredient": 11},  # Emballage
    {"id_usine": 14, "id_process_type": 4, "date": "2024-08-30", "id": 54, "id_marchandise": 11, "id_ingredient": 11},  # Conservation


]

PROCESS_TYPES = [
    {"id": 1, "nom": "Cuisson"},
    {"id": 2, "nom": "Melange"},
    {"id": 3, "nom": "Emballage"},
    {"id": 4, "nom": "Conservation"},
    {"id":5, "nom": "Maturation"},
]

LOTS = [
    {
        "id": 1,
        "date_de_prod": "2024-06-01",
        "date_de_peremption": "2025-06-01" ,  # 1 an de duree de conservation
        "id_produit": 1,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 2,
        "date_de_prod": "2024-08-01",
        "date_de_peremption": "2025-08-01" ,
        "id_produit": 2,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 3,
        "date_de_prod": "2024-08-01",
        "date_de_peremption": "2025-08-01" ,
        "id_produit": 3,
        "quantite": 800,
        "statut": True,
        "retour": False
    },
    {
        "id": 4,
        "date_de_prod": "2024-04-01",
        "date_de_peremption": "2025-04-01" ,
        "id_produit": 4,
        "quantite": 800,
        "statut": True,
        "retour": False
    },
    {
        "id": 5,
        "date_de_prod": "2024-09-01",
        "date_de_peremption": "2025-09-01" ,
        "id_produit": 5,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 6,
        "date_de_prod": "2024-05-01",
        "date_de_peremption": "2025-05-01" ,
        "id_produit": 6,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 7,
        "date_de_prod": "2024-03-01",
        "date_de_peremption": "2025-03-01" ,
        "id_produit": 7,
        "quantite": 1000,
        "statut": True,
        "retour": False
    },
    {
        "id": 8,
        "date_de_prod": "2024-09-01",
        "date_de_peremption": "2025-09-01" ,
        "id_produit": 8,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 9,
        "date_de_prod": "2023-09-01",
        "date_de_peremption": "2024-09-01" ,
        "id_produit": 9,
        "quantite": 1000,
        "statut": True,
        "retour": False
    },
    {
        "id": 10,
        "date_de_prod": "2024-08-01",
        "date_de_peremption": "2025-08-01" ,
        "id_produit": 10,
        "quantite": 1000,
        "statut": True,
        "retour": False
    }
]

STOCK = [
    {
        "id": 1,
        "id_entrepot": 1,
        "id_lot": 1,
        "date_arrivee": "2024-06-05"
    },
    {
        "id": 2,
        "id_entrepot": 2,
        "id_lot": 2,
        "date_arrivee": "2024-08-10"
    },
    {
        "id": 3,
        "id_entrepot": 3,
        "id_lot": 3,
        "date_arrivee": "2024-08-15"
    },
    {
        "id": 4,
        "id_entrepot": 4,
        "id_lot": 4,
        "date_arrivee": "2024-04-05"
    },
    {
        "id": 5,
        "id_entrepot": 5,
        "id_lot": 5,
        "date_arrivee": "2024-09-02"
    },
    {
        "id": 6,
        "id_entrepot": 6,
        "id_lot": 6,
        "date_arrivee": "2024-05-10"
    },
    {
        "id": 7,
        "id_entrepot": 7,
        "id_lot": 7,
        "date_arrivee": "2024-03-05"
    },
    {
        "id": 8,
        "id_entrepot": 8,
        "id_lot": 8,
        "date_arrivee": "2024-09-15"
    },
    {
        "id": 9,
        "id_entrepot": 9,
        "id_lot": 9,
        "date_arrivee": "2023-09-10"
    },
    {
        "id": 10,
        "id_entrepot": 10,
        "id_lot": 10,
        "date_arrivee": "2024-08-20"
    }
]

HISTORIQUE_PROCESS = [
    # Miel de lavande maritime
    {"id_lot": 1, "id_process": 1},
    {"id_lot": 1, "id_process": 2},
    {"id_lot": 1, "id_process": 3},

    # Miel de sarrasin
    {"id_lot": 2, "id_process": 4},
    {"id_lot": 2, "id_process": 5},
    {"id_lot": 2, "id_process": 6},

    # Confiture de pêche de vigne
    {"id_lot": 3, "id_process": 7},
    {"id_lot": 3, "id_process": 8},
    {"id_lot": 3, "id_process": 9},
    {"id_lot": 3, "id_process": 10},
    {"id_lot": 3, "id_process": 11},
    {"id_lot": 3, "id_process": 12},
    {"id_lot": 3, "id_process": 13},

    # Confiture de rhubarbe
    {"id_lot": 4, "id_process": 14},
    {"id_lot": 4, "id_process": 15},
    {"id_lot": 4, "id_process": 16},
    {"id_lot": 4, "id_process": 17},
    {"id_lot": 4, "id_process": 18},
    {"id_lot": 4, "id_process": 19},
    {"id_lot": 4, "id_process": 20},

    # Miel de jujubier
    {"id_lot": 5, "id_process": 21},
    {"id_lot": 5, "id_process": 22},
    {"id_lot": 5, "id_process": 23},

    # Miel de thé
    {"id_lot": 6, "id_process": 24},
    {"id_lot": 6, "id_process": 25},
    {"id_lot": 6, "id_process": 26},
    {"id_lot": 6, "id_process": 27},
    {"id_lot": 6, "id_process": 28},

    # Confiture de fruit du dragon et mangue
    {"id_lot": 7, "id_process": 29},
    {"id_lot": 7, "id_process": 30},
    {"id_lot": 7, "id_process": 31},
    {"id_lot": 7, "id_process": 32},
    {"id_lot": 7, "id_process": 33},
    {"id_lot": 7, "id_process": 34},
    {"id_lot": 7, "id_process": 35},
    {"id_lot": 7, "id_process": 36},
    {"id_lot": 7, "id_process": 37},

    # Miel d’eucalyptus
    {"id_lot": 8, "id_process": 38},
    {"id_lot": 8, "id_process": 39},
    {"id_lot": 8, "id_process": 40},

    # Confiture de goyave
    {"id_lot": 9, "id_process": 41},
    {"id_lot": 9, "id_process": 42},
    {"id_lot": 9, "id_process": 43},
    {"id_lot": 9, "id_process": 44},
    {"id_lot": 9, "id_process": 45},
    {"id_lot": 9, "id_process": 46},
    {"id_lot": 9, "id_process": 47},

    # Confiture de dattes
    {"id_lot": 10, "id_process": 48},
    {"id_lot": 10, "id_process": 49},
    {"id_lot": 10, "id_process": 50},
    {"id_lot": 10, "id_process": 51},
    {"id_lot": 10, "id_process": 52},
    {"id_lot": 10, "id_process": 53},
    {"id_lot": 10, "id_process": 54}
]


DISTRIBUTIONS = [
    # Distribution pour Miel de lavande maritime
    {"id": 1, "id_entrepot": 1, "id_lot": 1, "id_distributeur": 1, "date_contractualisation": "2024-06-01", "date_livraison": "2024-06-15"},
    {"id": 2, "id_entrepot": 2, "id_lot": 1, "id_distributeur": 2, "date_contractualisation": "2024-06-02", "date_livraison": "2024-06-16"},

    # Distribution pour Miel de sarrasin
    {"id": 3, "id_entrepot": 1, "id_lot": 2, "id_distributeur": 1, "date_contractualisation": "2024-08-01", "date_livraison": "2024-08-10"},
    {"id": 4, "id_entrepot": 2, "id_lot": 2, "id_distributeur": 3, "date_contractualisation": "2024-08-02", "date_livraison": "2024-08-12"},

    # Distribution pour Confiture de pêche de vigne
    {"id": 5, "id_entrepot": 3, "id_lot": 3, "id_distributeur": 4, "date_contractualisation": "2024-08-15", "date_livraison": "2024-08-20"},
    {"id": 6, "id_entrepot": 4, "id_lot": 3, "id_distributeur": 5, "date_contractualisation": "2024-08-16", "date_livraison": "2024-08-25"},

    # Distribution pour Confiture de rhubarbe
    {"id": 7, "id_entrepot": 3, "id_lot": 4, "id_distributeur": 6, "date_contractualisation": "2024-04-01", "date_livraison": "2024-04-10"},
    {"id": 8, "id_entrepot": 4, "id_lot": 4, "id_distributeur": 7, "date_contractualisation": "2024-04-02", "date_livraison": "2024-04-12"},

    # Distribution pour Miel de jujubier
    {"id": 9, "id_entrepot": 5, "id_lot": 5, "id_distributeur": 8, "date_contractualisation": "2024-09-01", "date_livraison": "2024-09-05"},

    # Distribution pour Miel de the
    {"id": 10, "id_entrepot": 6, "id_lot": 6, "id_distributeur": 9, "date_contractualisation": "2024-05-01", "date_livraison": "2024-05-10"},

    # Distribution pour Confiture de fruit du dragon
    {"id": 11, "id_entrepot": 7, "id_lot": 7, "id_distributeur": 10, "date_contractualisation": "2024-03-01", "date_livraison": "2024-03-10"},

    # Distribution pour Confiture de mangue
    {"id": 12, "id_entrepot": 8, "id_lot": 8, "id_distributeur": 11, "date_contractualisation": "2024-09-01", "date_livraison": "2024-09-05"},

    # Distribution pour Miel d’eucalyptus
    {"id": 13, "id_entrepot": 9, "id_lot": 9, "id_distributeur": 12, "date_contractualisation": "2023-09-01", "date_livraison": "2023-09-10"},

    # Distribution pour Confiture de goyave
    {"id": 14, "id_entrepot": 10, "id_lot": 10, "id_distributeur": 13, "date_contractualisation": "2024-08-01", "date_livraison": "2024-08-10"},
]


def populate_products(execute_query):
    for product in PRODUITS:
        query = """
        INSERT INTO Product_info (nom, description_etiquettes, quantite, photo_etiquettes, id_contenant, photo, version, date_mise_en_prod)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = [
        
            product["nom"],
            product["description_etiquettes"],
            product["quantite"],
            product["photo_etiquettes"],
            product["id_contenant"],
            product["photo"],
            product["version"],
            product["date_mise_en_prod"]
    
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting products: {e}")

def populate_costs(execute_query):
    for cost in DETAILS_COUTS:
        query = """
        INSERT INTO Details_Couts (cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing)
        VALUES (?, ?, ?, ?, ?)
        """
        params = [

            cost["cout_prod"],
            cost["cout_matieres_premieres"],
            cost["prix_de_vente"],
            cost["id_produit"],
            cost["cout_marketing"]

        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting costs: {e}")

def populate_ingredients(execute_query):
    for ingredient in INGREDIENTS:
        query = "INSERT INTO Ingredients (nom) VALUES (?)"
        params = [ingredient["nom"]]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting ingredients: {e}")

def populate_compositions(execute_query):
    for composition in COMPOSITION_PRODUIT:
        query = """
        INSERT INTO Composition_produit (id_produit, quantite, id_ingredient)
        VALUES (?, ?, ?)
        """
        params = [
            
            composition["id_produit"],
            composition["quantite"],
            composition["id_ingredient"]
        
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting compositions: {e}")

def populate_fournisseurs_distributeurs(execute_query):
    for fournisseur in FOURNISSEURS_DISTRIBUTEURS:
        query = """
        INSERT INTO `Fournisseurs_Distributeurs` (id, nom, localisation, contact, type)
        VALUES (?, ?, ?, ?, ?)
        """
        params = [
            fournisseur["id"],
            fournisseur["nom"],
            fournisseur["localisation"],
            fournisseur["contact"],
            fournisseur["type"],
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting fournisseur_distributeur {fournisseur['nom']}: {e}")

def populate_marchandises(execute_query):
    for marchandise in MARCHANDISES :
        query = """
        INSERT INTO Marchandises (id, date_contractualisation, date_livraison, id_ingredient, quantite_kg, id_usine_livraison, id_fournisseur)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = [
            
            marchandise["id"],
            marchandise["date_contractualisation"],
            marchandise["date_livraison"],
            marchandise["id_ingredient"],
            marchandise["quantite_kg"],
            marchandise["id_usine_livraison"],
            marchandise["id_fournisseur"]
        
        ]
        
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting marchandises: {e}")

def populate_usines_entrepots(execute_query):
    for usine in USINES_ENTREPOTS:
        query = """
        INSERT INTO Usines_entrepots (id, localisation, contact, type)
        VALUES (?, ?, ?, ?)
        """
        params = [
            usine["id"],
            usine["localisation"],
            usine["contact"],
            usine["type"]
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting usine/entrepôt {usine['localisation']}: {e}")

def populate_process(execute_query):
    # Insertion des types de processus
    for process_type in PROCESS_TYPES:
        query = """
        INSERT INTO Process_Types (id, nom)
        VALUES (?, ?)
        """
        params = [
            process_type["id"],
            process_type["nom"]
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting process type {process_type['nom']}: {e}")

    # Insertion des donnees de process
    for process in PROCESS_DATA:
        query = """
        INSERT INTO Process (id_usine, id_process_type, date, id, id_marchandise, id_ingredient)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            process["id_usine"],
            process["id_process_type"],
            process["date"],
            process["id"],
            process["id_marchandise"],
            process["id_ingredient"]
        )
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting process data for marchandise ID {process['id_marchandise']}: {e}")

def populate_lots(execute_query):
    for lot in LOTS:
        query = """
        INSERT INTO Lots (id, date_de_prod, date_de_peremption, id_produit, quantite, statut, retour)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = [
            
            lot["id"],
            lot["date_de_prod"],
            lot["date_de_peremption"],
            lot["id_produit"],
            lot["quantite"],
            lot["statut"],
            lot["retour"]
        
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting lots: {e}")

def populate_stock(execute_query):
    for stock in STOCK:
        query = """
        INSERT INTO Stock (id, id_entrepot, id_lot, date_arrivee)
        VALUES (?, ?, ?, ?)
        """
        params = [
            stock["id"],
            stock["id_entrepot"],
            stock["id_lot"],
            stock["date_arrivee"] 
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting stock: {e}")

def populate_historique_process(execute_query):
    for historique in HISTORIQUE_PROCESS:
        query = """
        INSERT INTO Historique_process (id_lot, id_process)
        VALUES (?, ?)
        """
        params = [
            historique["id_lot"], historique["id_process"]
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting historique process: {e}")

def populate_distributions(execute_query):
    for distribution in DISTRIBUTIONS:
        query = """
        INSERT INTO Distributions (id, id_entrepot, id_lot, id_distributeur, date_contractualisation, date_livraison)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = [
            distribution["id"], 
            distribution["id_entrepot"], 
            distribution["id_lot"], 
            distribution["id_distributeur"], 
            distribution["date_contractualisation"], 
            distribution["date_livraison"]
        ]
        try:
            execute_query(query, params)
        except Exception as e:
            print(f"Error inserting distributions: {e}")


