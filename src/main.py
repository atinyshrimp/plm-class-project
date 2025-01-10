from PyQt5.QtWidgets import QApplication, QDialog
from components.main_window import PLMApp
import dialogs.login.login_window as login
import database.databaseManager as database
import sys
import globals
import ctypes

VERSION = "1.0.0"

# Variable globale pour stocker l'utilisateur connecté
globals.current_user = None


if __name__ == "__main__":
    # Configure l'icône de la barre des tâches sur Windows
    myappid = f"mgo_sa.plm_internal_software.{VERSION}"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Initialisation de l'application
    app = QApplication(sys.argv)

    # Affiche la fenêtre de connexion
    login_dialog = login.LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:  # Si la connexion réussit
        # initalise la liaison avec la bdd
        db_manager = database.SQLiteManager()
        # Crée et lance la fenêtre principale

        # exemple d'utilisation de la fonction pour récupérer les infos d'une table raw
        # db_manager présent et initié dans chaque classe QT, on peut l'appeler avec self.db_manager.function()
        num_table = 5
        name_table = [
            "Composition_produit",
            "Details_Couts",
            "Distributions",
            "Fournisseurs_Distributeurs",
            "Historique_Process",
            "Ingredients",
            "Lots",
            "Marchandises",
            "Process",
            "Process_Types",
            "Product_info",
            "Stock",
            "Usines_Entrepots",
        ]
        if db_manager.is_admin:
            print(
                name_table[num_table],
                db_manager.get_table_as_list(name_table[num_table]),
            )

        window = PLMApp(VERSION, db_manager)  # Passe la version à la fenêtre principale
        window.show()
        print(globals.current_user)
        sys.exit(app.exec_())
    else:
        # Quitte l'application si la connexion échoue ou si l'utilisateur ferme la fenêtre
        sys.exit()
