import ctypes
import sys

from PyQt5.QtWidgets import QApplication, QDialog

import database.databaseManager as database
import dialogs.login.login_window as login
import globals
from components.main_window import PLMApp

VERSION = "1.3.0"

# Global variable to store the logged-in user
globals.current_user = None

if __name__ == "__main__":
    # Set the taskbar icon on Windows
    myappid = f"mgo_sa.plm_internal_software.{VERSION}"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Initialize the application
    app = QApplication(sys.argv)

    # Display the login window
    login_dialog = login.LoginDialog(VERSION)
    if login_dialog.exec_() == QDialog.Accepted:  # If login is successful
        # Initialize the database connection
        db_manager = database.SQLiteManager()

        # Create and launch the main window
        window = PLMApp(VERSION, db_manager)  # Pass the version to the main window
        window.show()

        sys.exit(app.exec_())
    else:
        # Exit the application if login fails or the user closes the window
        sys.exit()
