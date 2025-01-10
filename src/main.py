from PyQt5.QtWidgets import QApplication, QDialog
from components.main_window import PLMApp
import dialogs.login.login_window as login
import database.databaseManager as database
import sys
import globals
import ctypes

VERSION = "1.2.0"

# Variable globale pour stocker l'utilisateur connecté
globals.current_user = None


if __name__ == "__main__":
    # Configure l'icône de la barre des tâches sur Windows
    myappid = f"mgo_sa.plm_internal_software.{VERSION}"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Initialisation de l'application
    app = QApplication(sys.argv)

    # Affiche la fenêtre de connexion
    login_dialog = login.LoginDialog(VERSION)
    if login_dialog.exec_() == QDialog.Accepted:  # Si la connexion réussit
        # initalise la liaison avec la bdd
        db_manager = database.SQLiteManager()
        # Crée et lance la fenêtre principale
        window = PLMApp(VERSION,db_manager)  # Passe la version à la fenêtre principale

        window.show()
        print(globals.current_user)
        sys.exit(app.exec_())
    else:
        # Quitte l'application si la connexion échoue ou si l'utilisateur ferme la fenêtre
        sys.exit()
