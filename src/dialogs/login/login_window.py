from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

import globals
from utils.styling import apply_stylesheet

# Liste des identifiants valides
VALID_USERS = {"admin": "admin123", "viewer": "viewer123"}


class LoginDialog(QDialog):
    def __init__(self, version):
        super().__init__()
        self.setWindowTitle(f"Hive (PLM Internal Software) v{version} — Login")
        self.setWindowIcon(QtGui.QIcon("assets/img/mgo_sa_icon_resized.png"))
        self.resize(400, 500)

        # Apply the stylesheet
        apply_stylesheet(self, "assets/styles/palette_style.qss")

        # Layout principal
        layout = QVBoxLayout()

        # Logo
        logo_label = QLabel(self)
        logo_pixmap = QtGui.QPixmap("assets/img/mgo_sa_logo_big.png")
        if logo_pixmap.isNull():
            print("Failed to load image")
        else:
            logo_pixmap = logo_pixmap.scaled(
                350, 350, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
            )
            logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Champs de texte pour l'utilisateur et le mot de passe
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Bouton de connexion
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Vérification des identifiants
        if username in VALID_USERS and VALID_USERS[username] == password:
            globals.current_user = username
            self.accept()  # Ferme la fenêtre de connexion avec succès
        else:
            # Affiche une boîte de message d'erreur
            QMessageBox.critical(self, "Error", "Incorrect username or password.")

    def closeEvent(self, event):
        """Déclenché lorsque l'utilisateur clique sur le bouton de fermeture (X)."""
        # Demande une confirmation avant de fermer
        reply = QMessageBox.question(
            self,
            "Exit",
            "Do you want to exit the application?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()  # Ferme l'application
        else:
            event.ignore()  # Annule la fermeture
