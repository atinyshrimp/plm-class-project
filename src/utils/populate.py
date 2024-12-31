from database import create_connection, execute_query

# Données pour les produits
PRODUITS = [
    {
        "id": 1,
        "nom": "Miel de lavande maritime",
        "description_étiquettes": "Miel de lavande maritime de la Côte d’Azur, récolté entre juin et août.",
        "quantité": 500,
        "photo_étiquettes": "miel_lavande.jpg",
        "id_contenant": 1,
        "photo": "miel_lavande_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240601.0,
    },
    {
        "id": 2,
        "nom": "Miel de sarrasin",
        "description_étiquettes": "Miel de sarrasin récolté entre août et septembre en Bretagne, France et Pays-Bas.",
        "quantité": 500,
        "photo_étiquettes": "miel_sarrasin.jpg",
        "id_contenant": 1,
        "photo": "miel_sarrasin_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240801.0,
    },
    {
        "id": 3,
        "nom": "Confiture de pêche de vigne",
        "description_étiquettes": "Confiture artisanale de pêche de vigne, France et Espagne, août-septembre.",
        "quantité": 800,
        "photo_étiquettes": "confiture_peche.jpg",
        "id_contenant": 2,
        "photo": "confiture_peche_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240801.0,
    },
    {
        "id": 4,
        "nom": "Confiture de rhubarbe",
        "description_étiquettes": "Confiture de rhubarbe récoltée entre avril et juin en Belgique et aux Pays-Bas.",
        "quantité": 800,
        "photo_étiquettes": "confiture_rhubarbe.jpg",
        "id_contenant": 2,
        "photo": "confiture_rhubarbe_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240401.0,
    },
    {
        "id": 5,
        "nom": "Miel de jujubier",
        "description_étiquettes": "Miel de jujubier récolté entre septembre et décembre au Yémen et en Inde.",
        "quantité": 500,
        "photo_étiquettes": "miel_jujubier.jpg",
        "id_contenant": 1,
        "photo": "miel_jujubier_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240901.0,
    },
    {
        "id": 6,
        "nom": "Miel de thé",
        "description_étiquettes": "Miel de thé récolté entre mai et juillet en Chine et Japon.",
        "quantité": 500,
        "photo_étiquettes": "miel_the.jpg",
        "id_contenant": 1,
        "photo": "miel_the_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240501.0,
    },
    {
        "id": 7,
        "nom": "Confiture de fruit du dragon et mangue",
        "description_étiquettes": "Confiture réalisée avec des fruits du dragon récoltés entre juin et octobre et des mangues récoltées entre mars et juin au Vietnam et en Thaïlande.",
        "quantité": 1000,
        "photo_étiquettes": "confiture_fruit_mangue.jpg",
        "id_contenant": 3,
        "photo": "confiture_fruit_mangue_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240301.0,
    },
    {
        "id": 8,
        "nom": "Miel d’eucalyptus",
        "description_étiquettes": "Miel d’eucalyptus récolté entre septembre et novembre en Afrique du Sud, et entre janvier et mars au Maroc.",
        "quantité": 500,
        "photo_étiquettes": "miel_eucalyptus.jpg",
        "id_contenant": 1,
        "photo": "miel_eucalyptus_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240901.0,
    },
    {
        "id": 9,
        "nom": "Confiture de goyave",
        "description_étiquettes": "Confiture réalisée avec des goyaves récoltées entre septembre et décembre au Kenya, et entre février et avril en Afrique du Sud.",
        "quantité": 1000,
        "photo_étiquettes": "confiture_goyave.jpg",
        "id_contenant": 3,
        "photo": "confiture_goyave_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20230901.0,
    },
    {
        "id": 10,
        "nom": "Confiture de dattes",
        "description_étiquettes": "Confiture réalisée avec des dattes récoltées entre août et novembre en Tunisie et Égypte.",
        "quantité": 1000,
        "photo_étiquettes": "confiture_dattes.jpg",
        "id_contenant": 3,
        "photo": "confiture_dattes_bocal.jpg",
        "version": 1,
        "date_mise_en_prod": 20240801.0,
    }
]

# Données pour les coûts
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

# Données pour les ingrédients
INGREDIENTS = [
    {"id": 1, "nom": "Miel de lavande maritime"},
    {"id": 2, "nom": "Miel de sarrasin"},
    {"id": 3, "nom": "Pêche de vigne"},
    {"id": 4, "nom": "Rhubarbe"},
    {"id": 5, "nom": "Miel de jujubier"},
    {"id": 6, "nom": "Miel de thé"},
    {"id": 7, "nom": "Fruit du dragon"},
    {"id": 8, "nom": "Mangue"},
    {"id": 9, "nom": "Miel d’eucalyptus"},
    {"id": 10, "nom": "Goyave"},
    {"id": 11, "nom": "Datte"},
    {"id": 12, "nom": "Sucre"},
    {"id": 13, "nom": "Arôme de thé"},
    {"id": 14, "nom": "Jus de citron"},
    {"id": 15, "nom": "Pectine"},
]

# Composition des produits : chaque entrée représente un produit avec ses ingrédients et quantités
COMPOSITION_PRODUIT = [
    # Miel de lavande maritime
    {"id": 1, "id_produit": 1, "quantité": 500, "id_ingredient": 1},  # Miel de lavande maritime

    # Miel de sarrasin
    {"id": 2, "id_produit": 2, "quantité": 500, "id_ingredient": 2},  # Miel de sarrasin

    # Confiture de pêche de vigne
    {"id": 3, "id_produit": 3, "quantité": 800, "id_ingredient": 3},  # Pêche de vigne
    {"id": 4, "id_produit": 3, "quantité": 300, "id_ingredient": 12}, # Sucre
    {"id": 5, "id_produit": 3, "quantité": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 6, "id_produit": 3, "quantité": 10, "id_ingredient": 15},  # Pectine

    # Confiture de rhubarbe
    {"id": 7, "id_produit": 4, "quantité": 800, "id_ingredient": 4},  # Rhubarbe
    {"id": 8, "id_produit": 4, "quantité": 300, "id_ingredient": 12}, # Sucre
    {"id": 9, "id_produit": 4, "quantité": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 10, "id_produit": 4, "quantité": 10, "id_ingredient": 15}, # Pectine

    # Miel de jujubier
    {"id": 11, "id_produit": 5, "quantité": 500, "id_ingredient": 5}, # Miel de jujubier

    # Miel de thé
    {"id": 12, "id_produit": 6, "quantité": 500, "id_ingredient": 6},  # Miel de thé
    {"id": 13, "id_produit": 6, "quantité": 10, "id_ingredient": 13},  # Arôme de thé

    # Confiture de fruit du dragon et mangue
    {"id": 14, "id_produit": 7, "quantité": 500, "id_ingredient": 7},  # Fruit du dragon
    {"id": 15, "id_produit": 7, "quantité": 500, "id_ingredient": 8},  # Mangue
    {"id": 16, "id_produit": 7, "quantité": 300, "id_ingredient": 12}, # Sucre
    {"id": 17, "id_produit": 7, "quantité": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 18, "id_produit": 7, "quantité": 10, "id_ingredient": 15},  # Pectine

    # Miel d’eucalyptus
    {"id": 19, "id_produit": 8, "quantité": 500, "id_ingredient": 9},  # Miel d’eucalyptus

    # Confiture de goyave
    {"id": 20, "id_produit": 9, "quantité": 1000, "id_ingredient": 10}, # Goyave
    {"id": 21, "id_produit": 9, "quantité": 300, "id_ingredient": 12},  # Sucre
    {"id": 22, "id_produit": 9, "quantité": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 23, "id_produit": 9, "quantité": 10, "id_ingredient": 15},  # Pectine

    # Confiture de dattes
    {"id": 24, "id_produit": 10, "quantité": 1000, "id_ingredient": 11}, # Dattes
    {"id": 25, "id_produit": 10, "quantité": 300, "id_ingredient": 12},  # Sucre
    {"id": 26, "id_produit": 10, "quantité": 50, "id_ingredient": 14},  # Jus de citron
    {"id": 27, "id_produit": 10, "quantité": 10, "id_ingredient": 15},  # Pectine
]

FOURNISSEURS_DISTRIBUTEURS = [
    {"id": 1, "nom": "Fournisseur Lavande Maritime", "localisation": "Côte d’Azur, France", "contact": "contact@lavandemaritime.fournisseur.com", "type": True},
    {"id": 2, "nom": "Fournisseur Sarrasin Bretagne", "localisation": "Bretagne, France", "contact": "contact@sarrasinbretagne.fournisseur.com", "type": True},
    {"id": 3, "nom": "Fournisseur Rhubarbe Belgique", "localisation": "Belgique", "contact": "contact@rhubarbebelgique.fournisseur.com", "type": True},
    {"id": 4, "nom": "Fournisseur Sarrasin Pays-Bas", "localisation": "Pays-Bas", "contact": "contact@sarrasinpaysbas.fournisseur.com", "type": True},
    {"id": 5, "nom": "Fournisseur Sidr Yémen", "localisation": "Yémen", "contact": "contact@sidryemen.fournisseur.com", "type": True},
    {"id": 6, "nom": "Fournisseur Pitaya Vietnam", "localisation": "Vietnam, Zones proches de Ho Chi Minh", "contact": "contact@pitayavietnam.fournisseur.com", "type": True},
    {"id": 7, "nom": "Fournisseur Miel de Thé Chine", "localisation": "Chine, Zhejiang", "contact": "contact@mieldethechine.fournisseur.com", "type": True},
    {"id": 8, "nom": "Fournisseur Miel de Thé Japon", "localisation": "Japon, Zhejiang", "contact": "contact@mieldethejapon.fournisseur.com", "type": True},
    {"id": 9, "nom": "Fournisseur Dattes Tunisie", "localisation": "Tozeur, Tunisie", "contact": "contact@dattestunisie.fournisseur.com", "type": True},
    {"id": 10, "nom": "Fournisseur Goyave Kenya", "localisation": "Régions côtières, Kenya", "contact": "contact@goyavekenya.fournisseur.com", "type": True},
    {"id": 11, "nom": "Fournisseur Eucalyptus Afrique du Sud", "localisation": "Provinces du Cap, Afrique du Sud", "contact": "contact@eucalyptusafriquedusud.fournisseur.com", "type": True},
    {"id": 12, "nom": "Distributeur Bangkok Thaïlande", "localisation": "Bangkok, Thaïlande", "contact": "contact@distributeurbangkok.com", "type": False},
    {"id": 13, "nom": "Distributeur Ho Chi Minh Vietnam", "localisation": "Ho Chi Minh Ville, Vietnam", "contact": "contact@distributeurhochiminh.com", "type": False},
    {"id": 14, "nom": "Distributeur Dakar Sénégal", "localisation": "Dakar, Sénégal", "contact": "contact@distributeurdakar.com", "type": False},
    {"id": 15, "nom": "Distributeur Mombasa Kenya", "localisation": "Mombasa, Kenya", "contact": "contact@distributeurmombasa.com", "type": False},
    {"id": 16, "nom": "Distributeur Paris Bruxelles", "localisation": "Paris, France / Bruxelles, Belgique", "contact": "contact@distributeurparisbruxelles.com", "type": False}
]

MARCHANDISES = [
        {
            "id": 1,
            "date_contractualisation": 20240601.0,
            "date_livraison": 20240615.0,
            "id_ingredient": 1,  # Miel de lavande maritime
            "quantité_kg": 100,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 2,
            "date_contractualisation": 20240801.0,
            "date_livraison": 20240820.0,
            "id_ingredient": 2,  # Miel de sarrasin
            "quantité_kg": 150,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 3,
            "date_contractualisation": 20240801.0,
            "date_livraison": 20240825.0,
            "id_ingredient": 3,  # Pêche de vigne
            "quantité_kg": 200,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 4,
            "date_contractualisation": 20240401.0,
            "date_livraison": 20240415.0,
            "id_ingredient": 4,  # Rhubarbe
            "quantité_kg": 250,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 5,
            "date_contractualisation": 20240901.0,
            "date_livraison": 20240915.0,
            "id_ingredient": 5,  # Miel de jujubier
            "quantité_kg": 100,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 6,
            "date_contractualisation": 20240501.0,
            "date_livraison": 20240520.0,
            "id_ingredient": 6,  # Miel de thé
            "quantité_kg": 80,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 7,
            "date_contractualisation": 20240301.0,
            "date_livraison": 20240315.0,
            "id_ingredient": 7,  # Fruit du dragon
            "quantité_kg": 300,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 8,
            "date_contractualisation": 20240301.0,
            "date_livraison": 20240315.0,
            "id_ingredient": 8,  # Mangue
            "quantité_kg": 300,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 9,
            "date_contractualisation": 20240901.0,
            "date_livraison": 20240920.0,
            "id_ingredient": 9,  # Miel d’eucalyptus
            "quantité_kg": 120,
            "id_usine_livraison": 1,
            "id_fournisseur": 1
        },
        {
            "id": 10,
            "date_contractualisation": 20230901.0,
            "date_livraison": 20230915.0,
            "id_ingredient": 10,  # Goyave
            "quantité_kg": 150,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 11,
            "date_contractualisation": 20240801.0,
            "date_livraison": 20240830.0,
            "id_ingredient": 11,  # Datte
            "quantité_kg": 200,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 12,
            "date_contractualisation": 20240801.0,
            "date_livraison": 20240830.0,
            "id_ingredient": 12,  # Sucre
            "quantité_kg": 500,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 13,
            "date_contractualisation": 20240401.0,
            "date_livraison": 20240415.0,
            "id_ingredient": 13,  # Arôme de thé
            "quantité_kg": 50,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 14,
            "date_contractualisation": 20240401.0,
            "date_livraison": 20240415.0,
            "id_ingredient": 14,  # Jus de citron
            "quantité_kg": 30,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        },
        {
            "id": 15,
            "date_contractualisation": 20240401.0,
            "date_livraison": 20240415.0,
            "id_ingredient": 15,  # Pectine
            "quantité_kg": 20,
            "id_usine_livraison": 2,
            "id_fournisseur": 2
        }
    ]

USINES_ENTREPOTS = [
    {"id": 1, "localisation": "Côte d’Azur, France", "contact": "contact@lavandemaritime.usine.com", "type": True},
    {"id": 2, "localisation": "Bretagne, France", "contact": "contact@sarrasinbretagne.usine.com", "type": True},
    {"id": 3, "localisation": "Belgique", "contact": "contact@rhubarbebelgique.usine.com", "type": True},
    {"id": 4, "localisation": "Pays-Bas", "contact": "contact@sarrasinpaysbas.usine.com", "type": True},
    {"id": 5, "localisation": "Yémen", "contact": "contact@sidryemen.usine.com", "type": True},
    {"id": 6, "localisation": "Vietnam, Zones proches de Ho Chi Minh", "contact": "contact@pitayavietnam.usine.com", "type": True},
    {"id": 7, "localisation": "Chine, Zhejiang", "contact": "contact@mieldethechine.usine.com", "type": True},
    {"id": 8, "localisation": "Japon, Zhejiang", "contact": "contact@mieldethejapon.usine.com", "type": True},
    {"id": 9, "localisation": "Tozeur, Tunisie", "contact": "contact@dattestunisie.usine.com", "type": True},
    {"id": 10, "localisation": "Régions côtières, Kenya", "contact": "contact@goyavekenya.usine.com", "type": True},
    {"id": 11, "localisation": "Provinces du Cap, Afrique du Sud", "contact": "contact@eucalyptusafriquedusud.usine.com", "type": True},
    {"id": 12, "localisation": "Bangkok, Thaïlande", "contact": "contact@bangkok.usine.com", "type": False},
    {"id": 13, "localisation": "Ho Chi Minh Ville, Vietnam", "contact": "contact@hochiminh.usine.com", "type": False},
    {"id": 14, "localisation": "Dakar, Sénégal", "contact": "contact@dakar.usine.com", "type": False},
    {"id": 15, "localisation": "Mombasa, Kenya", "contact": "contact@mombasa.usine.com", "type": False},
    {"id": 16, "localisation": "Paris, France / Bruxelles, Belgique", "contact": "contact@parisbruxelles.usine.com", "type": False}
]

PROCESS_DATA = [
    # Miel de lavande maritime
    {"id_usine": 1, "id_process_type": 1, "date": 20240601.0, "id": 1, "id_marchandise": 1, "id_ingredient": 1},  # Extraction
    {"id_usine": 1, "id_process_type": 3, "date": 20240610.0, "id": 2, "id_marchandise": 1, "id_ingredient": 1},  # Emballage

    # Miel de sarrasin
    {"id_usine": 2, "id_process_type": 1, "date": 20240801.0, "id": 3, "id_marchandise": 2, "id_ingredient": 2},  # Extraction
    {"id_usine": 2, "id_process_type": 3, "date": 20240815.0, "id": 4, "id_marchandise": 2, "id_ingredient": 2},  # Emballage

    # Confiture de pêche de vigne
    {"id_usine": 2, "id_process_type": 1, "date": 20240801.0, "id": 5, "id_marchandise": 3, "id_ingredient": 3},  # Extraction
    {"id_usine": 2, "id_process_type": 2, "date": 20240820.0, "id": 6, "id_marchandise": 3, "id_ingredient": 3},  # Mélange
    {"id_usine": 2, "id_process_type": 3, "date": 20240825.0, "id": 7, "id_marchandise": 3, "id_ingredient": 12}, # Emballage

    # Confiture de rhubarbe
    {"id_usine": 3, "id_process_type": 1, "date": 20240401.0, "id": 8, "id_marchandise": 4, "id_ingredient": 4},  # Extraction
    {"id_usine": 3, "id_process_type": 3, "date": 20240410.0, "id": 9, "id_marchandise": 4, "id_ingredient": 4},  # Emballage

    # Miel de jujubier
    {"id_usine": 1, "id_process_type": 1, "date": 20240901.0, "id": 10, "id_marchandise": 5, "id_ingredient": 5},  # Extraction
    {"id_usine": 1, "id_process_type": 3, "date": 20240910.0, "id": 11, "id_marchandise": 5, "id_ingredient": 5},  # Emballage

    # Miel de thé
    {"id_usine": 7, "id_process_type": 1, "date": 20240501.0, "id": 12, "id_marchandise": 6, "id_ingredient": 6},  # Extraction
    {"id_usine": 7, "id_process_type": 2, "date": 20240515.0, "id": 13, "id_marchandise": 6, "id_ingredient": 6},  # Mélange

    # Confiture de fruit du dragon
    {"id_usine": 6, "id_process_type": 1, "date": 20240301.0, "id": 14, "id_marchandise": 7, "id_ingredient": 7},  # Extraction
    {"id_usine": 6, "id_process_type": 4, "date": 20240315.0, "id": 15, "id_marchandise": 7, "id_ingredient": 7},  # Conservation

    # Confiture de mangue
    {"id_usine": 6, "id_process_type": 1, "date": 20240301.0, "id": 16, "id_marchandise": 8, "id_ingredient": 8},  # Extraction
    {"id_usine": 6, "id_process_type": 4, "date": 20240315.0, "id": 17, "id_marchandise": 8, "id_ingredient": 8},  # Conservation

    # Miel d’eucalyptus
    {"id_usine": 11, "id_process_type": 1, "date": 20240901.0, "id": 18, "id_marchandise": 9, "id_ingredient": 9},  # Extraction
    {"id_usine": 11, "id_process_type": 3, "date": 20240920.0, "id": 19, "id_marchandise": 9, "id_ingredient": 9},  # Emballage

    # Confiture de goyave
    {"id_usine": 10, "id_process_type": 1, "date": 20230901.0, "id": 20, "id_marchandise": 10, "id_ingredient": 10},  # Extraction
    {"id_usine": 10, "id_process_type": 2, "date": 20230915.0, "id": 21, "id_marchandise": 10, "id_ingredient": 10},  # Mélange

    # Confiture de dattes
    {"id_usine": 9, "id_process_type": 1, "date": 20240801.0, "id": 22, "id_marchandise": 11, "id_ingredient": 11},  # Extraction
    {"id_usine": 9, "id_process_type": 4, "date": 20240830.0, "id": 23, "id_marchandise": 11, "id_ingredient": 11},  # Conservation

    # Sucre
    {"id_usine": 2, "id_process_type": 4, "date": 20240801.0, "id": 24, "id_marchandise": 12, "id_ingredient": 12},  # Conservation

    # Arôme de thé
    {"id_usine": 7, "id_process_type": 3, "date": 20240401.0, "id": 25, "id_marchandise": 13, "id_ingredient": 13},  # Emballage

    # Jus de citron
    {"id_usine": 2, "id_process_type": 4, "date": 20240401.0, "id": 26, "id_marchandise": 14, "id_ingredient": 14},  # Conservation

    # Pectine
    {"id_usine": 2, "id_process_type": 4, "date": 20240401.0, "id": 27, "id_marchandise": 15, "id_ingredient": 15},  # Conservation
]

PROCESS_TYPES = [
    {"id": 1, "nom": "Extraction"},
    {"id": 2, "nom": "Mélange"},
    {"id": 3, "nom": "Emballage"},
    {"id": 4, "nom": "Conservation"},
]

LOTS = [
    {
        "id": 1,
        "date_de_prod": 20240601.0,
        "date_de_peremption": 20240601.0 + 365,  # 1 an de durée de conservation
        "id_produit": 1,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 2,
        "date_de_prod": 20240801.0,
        "date_de_peremption": 20240801.0 + 365,
        "id_produit": 2,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 3,
        "date_de_prod": 20240801.0,
        "date_de_peremption": 20240801.0 + 365,
        "id_produit": 3,
        "quantite": 800,
        "statut": True,
        "retour": False
    },
    {
        "id": 4,
        "date_de_prod": 20240401.0,
        "date_de_peremption": 20240401.0 + 365,
        "id_produit": 4,
        "quantite": 800,
        "statut": True,
        "retour": False
    },
    {
        "id": 5,
        "date_de_prod": 20240901.0,
        "date_de_peremption": 20240901.0 + 365,
        "id_produit": 5,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 6,
        "date_de_prod": 20240501.0,
        "date_de_peremption": 20240501.0 + 365,
        "id_produit": 6,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 7,
        "date_de_prod": 20240301.0,
        "date_de_peremption": 20240301.0 + 365,
        "id_produit": 7,
        "quantite": 1000,
        "statut": True,
        "retour": False
    },
    {
        "id": 8,
        "date_de_prod": 20240901.0,
        "date_de_peremption": 20240901.0 + 365,
        "id_produit": 8,
        "quantite": 500,
        "statut": True,
        "retour": False
    },
    {
        "id": 9,
        "date_de_prod": 20230901.0,
        "date_de_peremption": 20230901.0 + 365,
        "id_produit": 9,
        "quantite": 1000,
        "statut": True,
        "retour": False
    },
    {
        "id": 10,
        "date_de_prod": 20240801.0,
        "date_de_peremption": 20240801.0 + 365,
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
        "date_arrivee": 20240605.0
    },
    {
        "id": 2,
        "id_entrepot": 2,
        "id_lot": 2,
        "date_arrivee": 20240810.0
    },
    {
        "id": 3,
        "id_entrepot": 3,
        "id_lot": 3,
        "date_arrivee": 20240815.0
    },
    {
        "id": 4,
        "id_entrepot": 4,
        "id_lot": 4,
        "date_arrivee": 20240405.0
    },
    {
        "id": 5,
        "id_entrepot": 5,
        "id_lot": 5,
        "date_arrivee": 20240902.0
    },
    {
        "id": 6,
        "id_entrepot": 6,
        "id_lot": 6,
        "date_arrivee": 20240510.0
    },
    {
        "id": 7,
        "id_entrepot": 7,
        "id_lot": 7,
        "date_arrivee": 20240305.0
    },
    {
        "id": 8,
        "id_entrepot": 8,
        "id_lot": 8,
        "date_arrivee": 20240915.0
    },
    {
        "id": 9,
        "id_entrepot": 9,
        "id_lot": 9,
        "date_arrivee": 20230910.0
    },
    {
        "id": 10,
        "id_entrepot": 10,
        "id_lot": 10,
        "date_arrivee": 20240820.0
    }
]

HISTORIQUE_PROCESS = [
    # Miel de lavande maritime (id_produit: 1)
    {"id_lot": 1, "id_process": 1},  # Extraction
    {"id_lot": 1, "id_process": 3},  # Emballage

    # Miel de sarrasin (id_produit: 2)
    {"id_lot": 2, "id_process": 1},  # Extraction
    {"id_lot": 2, "id_process": 3},  # Emballage

    # Confiture de pêche de vigne (id_produit: 3)
    {"id_lot": 3, "id_process": 1},  # Extraction
    {"id_lot": 3, "id_process": 2},  # Mélange
    {"id_lot": 3, "id_process": 3},  # Emballage

    # Confiture de rhubarbe (id_produit: 4)
    {"id_lot": 4, "id_process": 1},  # Extraction
    {"id_lot": 4, "id_process": 3},  # Emballage

    # Miel de jujubier (id_produit: 5)
    {"id_lot": 5, "id_process": 1},  # Extraction
    {"id_lot": 5, "id_process": 3},  # Emballage

    # Miel de thé (id_produit: 6)
    {"id_lot": 6, "id_process": 1},  # Extraction
    {"id_lot": 6, "id_process": 2},  # Mélange

    # Confiture de fruit du dragon (id_produit: 7)
    {"id_lot": 7, "id_process": 1},  # Extraction
    {"id_lot": 7, "id_process": 4},  # Conservation

    # Confiture de mangue (id_produit: 8)
    {"id_lot": 8, "id_process": 1},  # Extraction
    {"id_lot": 8, "id_process": 4},  # Conservation

    # Miel d’eucalyptus (id_produit: 9)
    {"id_lot": 9, "id_process": 1},  # Extraction
    {"id_lot": 9, "id_process": 3},  # Emballage

    # Confiture de goyave (id_produit: 10)
    {"id_lot": 10, "id_process": 1}, # Extraction
    {"id_lot": 10, "id_process": 2}, # Mélange

    # Confiture de dattes (id_produit: 11)
    {"id_lot": 11, "id_process": 1}, # Extraction
    {"id_lot": 11, "id_process": 4}, # Conservation

    # Sucre (id_produit: 12)
    {"id_lot": 12, "id_process": 4}, # Conservation

    # Arôme de thé (id_produit: 13)
    {"id_lot": 13, "id_process": 3}, # Emballage

    # Jus de citron (id_produit: 14)
    {"id_lot": 14, "id_process": 4}, # Conservation

    # Pectine (id_produit: 15)
    {"id_lot": 15, "id_process": 4}, # Conservation
]

DISTRIBUTIONS = [
    # Distribution pour Miel de lavande maritime
    {"id": 1, "id_entrepot": 1, "id_lot": 1, "id_distributeur": 1, "date_contractualisation": 20240601.0, "date_livraison": 20240615.0},
    {"id": 2, "id_entrepot": 2, "id_lot": 1, "id_distributeur": 2, "date_contractualisation": 20240602.0, "date_livraison": 20240616.0},

    # Distribution pour Miel de sarrasin
    {"id": 3, "id_entrepot": 1, "id_lot": 2, "id_distributeur": 1, "date_contractualisation": 20240801.0, "date_livraison": 20240810.0},
    {"id": 4, "id_entrepot": 2, "id_lot": 2, "id_distributeur": 3, "date_contractualisation": 20240802.0, "date_livraison": 20240812.0},

    # Distribution pour Confiture de pêche de vigne
    {"id": 5, "id_entrepot": 3, "id_lot": 3, "id_distributeur": 4, "date_contractualisation": 20240815.0, "date_livraison": 20240820.0},
    {"id": 6, "id_entrepot": 4, "id_lot": 3, "id_distributeur": 5, "date_contractualisation": 20240816.0, "date_livraison": 20240825.0},

    # Distribution pour Confiture de rhubarbe
    {"id": 7, "id_entrepot": 3, "id_lot": 4, "id_distributeur": 6, "date_contractualisation": 20240401.0, "date_livraison": 20240410.0},
    {"id": 8, "id_entrepot": 4, "id_lot": 4, "id_distributeur": 7, "date_contractualisation": 20240402.0, "date_livraison": 20240412.0},

    # Distribution pour Miel de jujubier
    {"id": 9, "id_entrepot": 5, "id_lot": 5, "id_distributeur": 8, "date_contractualisation": 20240901.0, "date_livraison": 20240905.0},

    # Distribution pour Miel de thé
    {"id": 10, "id_entrepot": 6, "id_lot": 6, "id_distributeur": 9, "date_contractualisation": 20240501.0, "date_livraison": 20240510.0},

    # Distribution pour Confiture de fruit du dragon
    {"id": 11, "id_entrepot": 7, "id_lot": 7, "id_distributeur": 10, "date_contractualisation": 20240301.0, "date_livraison": 20240310.0},

    # Distribution pour Confiture de mangue
    {"id": 12, "id_entrepot": 8, "id_lot": 8, "id_distributeur": 11, "date_contractualisation": 20240901.0, "date_livraison": 20240905.0},

    # Distribution pour Miel d’eucalyptus
    {"id": 13, "id_entrepot": 9, "id_lot": 9, "id_distributeur": 12, "date_contractualisation": 20230901.0, "date_livraison": 20230910.0},

    # Distribution pour Confiture de goyave
    {"id": 14, "id_entrepot": 10, "id_lot": 10, "id_distributeur": 13, "date_contractualisation": 20240801.0, "date_livraison": 20240810.0},
]

def populate_products(connection):
    query = """
    INSERT INTO Product_info (nom, description_étiquettes, quantité, photo_étiquettes, id_contenant, photo, version, date_mise_en_prod)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = [
        (
            product["nom"],
            product["description_étiquettes"],
            product["quantité"],
            product["photo_étiquettes"],
            product["id_contenant"],
            product["photo"],
            product["version"],
            product["date_mise_en_prod"]
        ) for product in PRODUITS
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting products: {e}")

def populate_costs(connection):
    query = """
    INSERT INTO Details_Couts (cout_prod, cout_matieres_premieres, prix_de_vente, id_produit, cout_marketing)
    VALUES (?, ?, ?, ?, ?)
    """
    params = [
        (
            cost["cout_prod"],
            cost["cout_matieres_premieres"],
            cost["prix_de_vente"],
            cost["id_produit"],
            cost["cout_marketing"]
        ) for cost in DETAILS_COUTS
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting costs: {e}")

def populate_ingredients(connection):
    query = "INSERT INTO Ingredients (nom) VALUES (?)"
    params = [(ingredient["nom"],) for ingredient in INGREDIENTS]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting ingredients: {e}")

def populate_compositions(connection):
    query = """
    INSERT INTO Composition_produit (id_produit, quantité, id_ingredient)
    VALUES (?, ?, ?)
    """
    params = [
        (
            composition["id_produit"],
            composition["quantité"],
            composition["id_ingredient"]
        ) for composition in COMPOSITION_PRODUIT
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting compositions: {e}")

def populate_fournisseurs_distributeurs(connection):
    for fournisseur in FOURNISSEURS_DISTRIBUTEURS:
        query = """
        INSERT INTO `Fournisseurs/Distributeurs` (id, nom, localisation, contact, type)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (
            fournisseur["id"],
            fournisseur["nom"],
            fournisseur["localisation"],
            fournisseur["contact"],
            fournisseur["type"],
        )
        try:
            execute_query(connection, query, params)
        except Exception as e:
            print(f"Error inserting fournisseur/distributeur {fournisseur['nom']}: {e}")

def populate_marchandises(connection):
    query = """
    INSERT INTO Marchandises (id, date_contractualisation, date_livraison, id_ingredient, quantité_kg, id_usine_livraison, id_fournisseur)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    params = [
        (
            marchandise["id"],
            marchandise["date_contractualisation"],
            marchandise["date_livraison"],
            marchandise["id_ingredient"],
            marchandise["quantité_kg"],
            marchandise["id_usine_livraison"],
            marchandise["id_fournisseur"]
        ) for marchandise in MARCHANDISES  
    ]
    
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting marchandises: {e}")

def populate_usines_entrepots(connection):
    for usine in USINES_ENTREPOTS:
        query = """
        INSERT INTO Usines_entrepots (id, localisation, contact, type)
        VALUES (?, ?, ?, ?)
        """
        params = (
            usine["id"],
            usine["localisation"],
            usine["contact"],
            usine["type"]
        )
        try:
            execute_query(connection, query, params)
        except Exception as e:
            print(f"Error inserting usine/entrepôt {usine['localisation']}: {e}")

def populate_process(connection):
    # Insertion des types de processus
    for process_type in PROCESS_TYPES:
        query = """
        INSERT INTO Process_Types (id, nom)
        VALUES (?, ?)
        """
        params = (
            process_type["id"],
            process_type["nom"]
        )
        try:
            execute_query(connection, query, params)
        except Exception as e:
            print(f"Error inserting process type {process_type['nom']}: {e}")

    # Insertion des données de process
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
            execute_query(connection, query, params)
        except Exception as e:
            print(f"Error inserting process data for marchandise ID {process['id_marchandise']}: {e}")

def populate_lots(connection):
    query = """
    INSERT INTO Lots (id, date_de_prod, date_de_peremption, id_produit, quantite, statut, retour)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    params = [
        (
            lot["id"],
            lot["date_de_prod"],
            lot["date_de_peremption"],
            lot["id_produit"],
            lot["quantite"],
            lot["statut"],
            lot["retour"]
        ) for lot in LOTS
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting lots: {e}")

def populate_stock(connection):
    query = """
    INSERT INTO Stock (id, id_entrepot, id_lot, date_arrivee)
    VALUES (?, ?, ?, ?)
    """
    params = [
        (
            stock["id"],
            stock["id_entrepot"],
            stock["id_lot"],
            stock["date_arrivee"]
        ) for stock in STOCK
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting stock: {e}")

def populate_historique_process(connection):
    query = """
    INSERT INTO Historique_process (id_lot, id_process)
    VALUES (?, ?)
    """
    params = [
        (historique["id_lot"], historique["id_process"]) for historique in HISTORIQUE_PROCESS
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting historique process: {e}")

def populate_distributions(connection):
    query = """
    INSERT INTO Distributions (id, id_entrepot, id_lot, id_distributeur, date_contractualisation, date_livraison)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    params = [
        (distribution["id"], 
         distribution["id_entrepot"], 
         distribution["id_lot"], 
         distribution["id_distributeur"], 
         distribution["date_contractualisation"], 
         distribution["date_livraison"]) 
        for distribution in DISTRIBUTIONS
    ]
    try:
        execute_query(connection, query, params)
    except Exception as e:
        print(f"Error inserting distributions: {e}")

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        populate_products(conn)
        populate_costs(conn)
        populate_ingredients(conn)
        populate_compositions(conn)
        populate_fournisseurs_distributeurs(conn)
        populate_marchandises(conn)
        populate_usines_entrepots(conn)
        populate_process(conn)
        populate_lots(conn)
        populate_stock(conn)
        populate_historique_process(conn)
        populate_distributions(conn)
        conn.close()