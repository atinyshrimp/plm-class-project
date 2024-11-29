from database import create_connection, execute_query

# Données pour les produits
PRODUCTS = [
    {
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
        "id_produit": 1,  # Correspond au premier produit dans `PRODUCTS`
        "cout_prod": 12.50,  # Coût total de production
        "cout_matieres_premieres": 10.50,  # Coût des matières premières
        "prix_de_vente": 18.00,  # Prix de vente final
        "cout_marketing": 2.00,  # Coût du marketing
    },
    {
        "id_produit": 2,
        "cout_prod": 13.20,
        "cout_matieres_premieres": 11.20,
        "prix_de_vente": 19.00,
        "cout_marketing": 2.50,
    },
    {
        "id_produit": 3,
        "cout_prod": 9.50,
        "cout_matieres_premieres": 7.50,
        "prix_de_vente": 14.00,
        "cout_marketing": 1.50,
    },
    {
        "id_produit": 4,
        "cout_prod": 8.80,
        "cout_matieres_premieres": 6.80,
        "prix_de_vente": 13.00,
        "cout_marketing": 1.20,
    },
    {
        "id_produit": 5,
        "cout_prod": 15.50,
        "cout_matieres_premieres": 13.50,
        "prix_de_vente": 22.00,
        "cout_marketing": 3.00,
    },
    {
        "id_produit": 6,
        "cout_prod": 11.10,
        "cout_matieres_premieres": 9.10,
        "prix_de_vente": 16.00,
        "cout_marketing": 2.00,
    },
    {
        "id_produit": 7,
        "cout_prod": 13.60,
        "cout_matieres_premieres": 11.60,
        "prix_de_vente": 20.00,
        "cout_marketing": 2.50,
    },
    {
        "id_produit": 8,
        "cout_prod": 12.20,
        "cout_matieres_premieres": 10.20,
        "prix_de_vente": 18.50,
        "cout_marketing": 2.30,
    },
    {
        "id_produit": 9,
        "cout_prod": 14.40,
        "cout_matieres_premieres": 12.40,
        "prix_de_vente": 21.00,
        "cout_marketing": 2.70,
    },
    {
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
    {"id": 1, "nom": "Fournisseur Lavande Maritime", "localisation": "Côte d’Azur, France", "contact": "contact@lavandemaritime.com", "type": True},
    {"id": 2, "nom": "Fournisseur Sarrasin Bretagne", "localisation": "Bretagne, France", "contact": "contact@sarrasinbretagne.com", "type": True},
    {"id": 3, "nom": "Fournisseur Rhubarbe Belgique", "localisation": "Belgique", "contact": "contact@rhubarbebelgique.com", "type": True},
    {"id": 4, "nom": "Fournisseur Sarrasin Pays-Bas", "localisation": "Pays-Bas", "contact": "contact@sarrasinpaysbas.com", "type": True},
    {"id": 5, "nom": "Fournisseur Sidr Yémen", "localisation": "Yémen", "contact": "contact@sidryemen.com", "type": True},
    {"id": 6, "nom": "Fournisseur Pitaya Vietnam", "localisation": "Vietnam, Zones proches de Ho Chi Minh", "contact": "contact@pitayavietnam.com", "type": True},
    {"id": 7, "nom": "Fournisseur Miel de Thé Chine", "localisation": "Chine, Zhejiang", "contact": "contact@mieldethechine.com", "type": True},
    {"id": 8, "nom": "Fournisseur Miel de Thé Japon", "localisation": "Japon, Zhejiang", "contact": "contact@mieldethejapon.com", "type": True},
    {"id": 9, "nom": "Fournisseur Dattes Tunisie", "localisation": "Tozeur, Tunisie", "contact": "contact@dattestunisie.com", "type": True},
    {"id": 10, "nom": "Fournisseur Goyave Kenya", "localisation": "Régions côtières, Kenya", "contact": "contact@goyavekenya.com", "type": True},
    {"id": 11, "nom": "Fournisseur Eucalyptus Afrique du Sud", "localisation": "Provinces du Cap, Afrique du Sud", "contact": "contact@eucalyptusafriquedusud.com", "type": True},
    {"id": 12, "nom": "Distributeur Bangkok Thaïlande", "localisation": "Bangkok, Thaïlande", "contact": "contact@distributeurbangkok.com", "type": False},
    {"id": 13, "nom": "Distributeur Ho Chi Minh Vietnam", "localisation": "Ho Chi Minh Ville, Vietnam", "contact": "contact@distributeurhochiminh.com", "type": False},
    {"id": 14, "nom": "Distributeur Dakar Sénégal", "localisation": "Dakar, Sénégal", "contact": "contact@distributeurdakar.com", "type": False},
    {"id": 15, "nom": "Distributeur Mombasa Kenya", "localisation": "Mombasa, Kenya", "contact": "contact@distributeurmombasa.com", "type": False},
    {"id": 16, "nom": "Distributeur Paris Bruxelles", "localisation": "Paris, France / Bruxelles, Belgique", "contact": "contact@distributeurparisbruxelles.com", "type": False}
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
        ) for product in PRODUCTS
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
        execute_query(connection, query, params)


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        populate_products(conn)
        populate_costs(conn)
        populate_ingredients(conn)
        populate_compositions(conn)
        populate_fournisseurs_distributeurs(conn)
        conn.close()
