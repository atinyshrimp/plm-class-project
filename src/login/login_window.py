from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import globals
# Liste des identifiants valides
VALID_USERS = {
    "admin": "admin123",
    "viewer": "viewer123"
}

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion")
        self.resize(300, 150)

        # Layout principal
        layout = QVBoxLayout()

        # Champs de texte pour l'utilisateur et le mot de passe
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Nom d'utilisateur")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Bouton de connexion
        self.login_button = QPushButton("Se connecter", self)
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
            QMessageBox.critical(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def closeEvent(self, event):
        """Déclenché lorsque l'utilisateur clique sur le bouton de fermeture (X)."""
        # Demande une confirmation avant de fermer
        reply = QMessageBox.question(
            self,
            "Quitter",
            "Voulez-vous vraiment quitter l'application ?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()  # Ferme l'application
        else:
            event.ignore()  # Annule la fermeture

