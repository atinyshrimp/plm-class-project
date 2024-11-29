from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

class ProductPhotoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.network_manager = QNetworkAccessManager()  # Initialize network manager

    def init_ui(self):
        layout = QVBoxLayout()

        # Create QLabel for the photo
        self.photo_label = QLabel("No Image")
        self.photo_label.setAlignment(Qt.AlignCenter)
        self.photo_label.setStyleSheet("border: 1px solid #d3d3d3; background-color: #f9f9f9;")
        self.photo_label.setFixedSize(200, 200)  # Set a fixed size for the image

        layout.addWidget(self.photo_label)
        self.setLayout(layout)

    def set_photo(self, photo_path):
        """Set the product photo from a local or online source."""
        if photo_path.startswith("http://") or photo_path.startswith("https://"):
            # Handle online images
            self.load_online_image(photo_path)
        else:
            # Handle local images
            pixmap = QPixmap(photo_path)
            if not pixmap.isNull():
                self.photo_label.setPixmap(pixmap)
                self.photo_label.setScaledContents(True)  # Scale the image to fit the QLabel
            else:
                self.photo_label.setText("Image Not Found")

    def load_online_image(self, url):
        """Load an image from an online source."""
        request = QNetworkRequest(QUrl(url))
        self.network_manager.finished.connect(self.on_image_loaded)
        self.network_manager.get(request)

    def on_image_loaded(self, reply):
        """Callback for when the image download is complete."""
        if reply.error() == reply.NoError:
            pixmap = QPixmap()
            pixmap.loadFromData(reply.readAll())
            if not pixmap.isNull():
                self.photo_label.setPixmap(pixmap)
                self.photo_label.setScaledContents(True)  # Scale the image to fit the QLabel
            else:
                self.photo_label.setText("Failed to Load Image")
        else:
            self.photo_label.setText("Error Loading Image")
        reply.deleteLater()
