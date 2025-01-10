import login.login_window as login
import database.databaseManager as database
import sys
import globals
import ctypes

VERSION = "0.8.0"

# Variable globale pour stocker l'utilisateur connecté
globals.current_user = None




if __name__ == "__main__":
    # Affiche la fenêtre de connexion
    globals.current_user = 'admin'
    db_manager = database.SQLiteManager()


    # exemple d'utilisation de la fonction pour récupérer les infos d'une table raw
    # db_manager présent et initié dans chaque classe QT, on peut l'appeler avec self.db_manager.function()

    update_row_distribution = {"id": 1, "id_entrepot": 1, "id_lot": 1, "id_distributeur": 1, "date_contractualisation": "2024-09-01", "date_livraison": "2024-06-15"}

    name_table = ['Composition_produit','Details_Couts','Distributions','Fournisseurs_Distributeurs','Historique_Process','Ingredients','Lots','Marchandises','Process','Process_Types','Product_info','Stock','Usines_Entrepots']
    
    print("\n \n recupere les infos d'une table:")
    print(name_table[5],db_manager.get_table_as_list(name_table[5]))

    print("\n \n recupere les propositions d'une table:")
    print(db_manager.get_row_suggestion(name_table[7]))

    print("\n \n update une table:")
    db_manager.update_row('Distributions',update_row_distribution)

    print("\n \n supprime une ligne")
    db_manager.delete_row('Distributions',2)



