SQL_QUERIES = {
    "fetch_product_details": """
        SELECT 
            printf('P%04d', pi.id) AS id_produit,
            pi.nom AS nom_produit,
            pi.quantite AS quantité_produit,
            printf('V%d', pi.version) AS version_produit,
            pi.date_mise_en_prod AS date_mise_en_prod,
            printf('C%04d', pi.id_contenant) AS id_contenant,
            pi.description_etiquettes,
            GROUP_CONCAT(
                ing.nom || ' (' || 
                CAST(ROUND((cp.quantite * 100.0 / pi.quantite)) AS INTEGER) || '%)', ', '
            ) AS ingredients_details,
            pi.photo
        FROM 
            Product_info pi
        LEFT JOIN 
            Composition_produit cp ON pi.id = cp.id_produit
        LEFT JOIN 
            Ingredients ing ON cp.id_ingredient = ing.id
        GROUP BY 
            pi.id, pi.nom, pi.quantite, pi.version, pi.date_mise_en_prod, pi.id_contenant, pi.description_etiquettes, pi.photo
        ORDER BY 
            pi.id, cp.quantite DESC;
    """,
    "fetch_cost_details": """
        SELECT 
            printf('P%04d', id_produit) AS id_produit,
            cout_prod AS cout_production,
            cout_matieres_premieres AS cout_matieres_premieres,
            prix_de_vente AS prix_de_vente,
            cout_marketing AS cout_marketing,
            (cout_prod + cout_matieres_premieres + cout_marketing) AS somme_des_couts,
            (prix_de_vente - (cout_prod + cout_matieres_premieres + cout_marketing)) / prix_de_vente * 100 AS marge
        FROM 
            Details_Couts
    """,
    "fetch_stock_and_location": """
        SELECT 
            printf('L%04d', Lots.id) AS id_lot,
            printf('P%04d', Lots.id_produit) AS id_produit,
            Lots.quantite AS quantite_par_lot,
            Lots.date_de_peremption,
            Stock.date_arrivee,
            Usines_entrepots.id AS id_entrepot,
            Usines_entrepots.localisation AS localisation_entrepot
        FROM 
            Lots
        JOIN 
            Stock ON Stock.id_lot = Lots.id
        JOIN 
            Usines_entrepots ON Usines_entrepots.id = Stock.id_entrepot
    """,
    "fetch_production_tracking": """
        SELECT 
            printf('L%04d', L.id) AS Id_lot,
            printf('P%04d', PI.id) AS Id_produit,
            PT.nom AS Process_name,
            P.date AS Date,
            UE.localisation AS Usine,
            I.nom As Ingredients,
            printf('M%04d', M.id) AS Id_marchandise
        FROM 
            Historique_Process HP
        JOIN 
            Lots L ON HP.id_lot = L.id
        JOIN 
            Process P ON HP.id_process = P.id
        JOIN 
            Process_Types PT ON P.id_process_type = PT.id
        LEFT JOIN 
            Marchandises M ON P.id_marchandise = M.id
        JOIN 
            Ingredients I ON P.id_ingredient = I.id
        JOIN 
            Usines_entrepots UE ON P.id_usine = UE.id
        JOIN 
            Product_info PI ON L.id_produit = PI.id
        ORDER BY 
            P.date;
    """,
    "fetch_production_tracking_aggregated": """
        SELECT 
            printf('L%04d', L.id) AS Id_lot,
            printf('P%04d', PI.id) AS Id_produit,
            PT.nom AS Process_name,
            P.date AS Date,
            UE.localisation AS Usine,
            GROUP_CONCAT(I.nom, ', ') AS Ingredients,
            GROUP_CONCAT(M.id, ', ') AS Id_marchandises
        FROM 
            Historique_Process HP
        JOIN 
            Lots L ON HP.id_lot = L.id
        JOIN 
            Process P ON HP.id_process = P.id
        JOIN 
            Process_Types PT ON P.id_process_type = PT.id
        LEFT JOIN 
            Marchandises M ON P.id_marchandise = M.id
        JOIN 
            Ingredients I ON P.id_ingredient = I.id
        JOIN 
            Usines_entrepots UE ON P.id_usine = UE.id
        JOIN 
            Product_info PI ON L.id_produit = PI.id
        GROUP BY 
            L.id, PT.nom, P.date, PI.id, UE.localisation
        ORDER BY 
            P.date;
    """,
    "fetch_merchant_tracking": """
        SELECT
            printf('M%04d', m.id) AS id_marchandises,
            m.date_livraison,
            i.nom AS ingredient,
            m.quantite_kg AS quantité,
            u.localisation AS usine_de_livraison,
            f.nom AS fournisseur
        FROM
            Marchandises m
        JOIN
            Ingredients i ON m.id_ingredient = i.id
        JOIN
            Usines_entrepots u ON m.id_usine_livraison = u.id
        JOIN
            Fournisseurs_Distributeurs f ON m.id_fournisseur = f.id
        ORDER BY
            m.date_livraison;
    """,
    "fetch_distribution_tracking": """
        SELECT
            d.date_livraison,
            d.date_contractualisation,
            printf('L%04d', l.id) AS lot,
            l.quantite AS quantité_lot,
            ue.localisation AS entrepot_de_depart,
            fd.nom AS distributeur,
            fd.localisation AS localisation_distributeur,
            printf('P%04d', pi.id) AS id_produit
        FROM
            Distributions d
        JOIN
            Lots l ON d.id_lot = l.id
        JOIN
            Usines_entrepots ue ON d.id_entrepot = ue.id
        JOIN
            Fournisseurs_Distributeurs fd ON d.id_distributeur = fd.id
        JOIN
            Product_info pi ON l.id_produit = pi.id
        ORDER BY
            d.date_livraison;
    """,
    "fetch_lot_history": """
        SELECT
            printf('L%04d', L.id) AS Id_lot,
            printf('P%04d', PI.id) AS Id_produit,
            L.quantite AS Quantité,
            L.date_de_prod AS Date_de_prod,
            L.date_de_peremption AS Date_peremption,
            L.statut AS Statut,
            L.retour AS Retour
        FROM
            Lots L
        JOIN
            Product_info PI ON L.id_produit = PI.id
        ORDER BY
            L.id;
    """,
}
