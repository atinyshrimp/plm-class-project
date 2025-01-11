from PyQt5.QtCore import QRectF, QSize, Qt, QUrl
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ProductPhotoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.network_manager = QNetworkAccessManager()  # Initialize network manager
        self.network_manager.finished.connect(
            self.__on_image_loaded
        )  # Connect once in the constructor
        self.current_reply = None  # Keep track of the current network reply

    def __init_ui(self):
        layout = QVBoxLayout()

        # Create QLabel for the photo
        self.photo_label = QLabel("No Image")
        self.photo_label.setAlignment(Qt.AlignCenter)
        self.photo_label.setStyleSheet(
            "border: 1px solid #d3d3d3; background-color: #f9f9f9;"
        )
        self.photo_label.setFixedSize(200, 200)  # Set a fixed size for the image

        layout.addWidget(self.photo_label)
        self.setLayout(layout)

    def set_photo(self, photo_path: str):
        """Set the product photo from a local or online source."""
        # Cancel any ongoing network request
        if self.current_reply:
            self.current_reply.abort()
            # self.current_reply.deleteLater()

        if photo_path.startswith("http://") or photo_path.startswith("https://"):
            # Handle online images
            self.__load_online_image(photo_path)
        else:
            # Handle local images
            pixmap = QPixmap(photo_path)
            if not pixmap.isNull():
                rounded_pixmap = self.__apply_rounded_mask(pixmap)
                scaled_pixmap = rounded_pixmap.scaled(
                    200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.photo_label.setPixmap(scaled_pixmap)
                self.__photo_path = photo_path
            else:
                self.photo_label.setText("Image Not Found")

    def __load_online_image(self, url: str):
        """Load an image from an online source."""
        request = QNetworkRequest(QUrl(url))
        self.current_reply = self.network_manager.get(request)

    def __on_image_loaded(self, reply: QNetworkReply):
        """Callback for when the image download is complete."""
        # Only process the reply if it's the current reply
        if reply == self.current_reply:
            if reply.error() == reply.NoError:
                pixmap = QPixmap()
                pixmap.loadFromData(reply.readAll())
                if not pixmap.isNull():
                    scaled_pixmap = pixmap.scaled(
                        200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                    self.photo_label.setPixmap(scaled_pixmap)
                    self.__photo_path = reply.url().toString()
                else:
                    self.photo_label.setText("Failed to Load Image")
            else:
                self.photo_label.setText("Error Loading Image")

            # reply.deleteLater()
            self.current_reply = None

    def __apply_rounded_mask(self, pixmap: QPixmap) -> QPixmap:
        """Apply a rounded mask to the pixmap."""
        size = QSize(200, 200)
        rounded_pixmap = QPixmap(size)
        rounded_pixmap.fill(Qt.transparent)

        # Scale the pixmap to fit within the rounded rectangle while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create a rounded rectangle path
        path = QPainterPath()
        path.addRoundedRect(QRectF(0, 0, size.width(), size.height()), 10, 10)

        # Clip the painter to the rounded rectangle path
        painter.setClipPath(path)
        painter.drawPixmap(
            (size.width() - scaled_pixmap.width()) // 2,
            (size.height() - scaled_pixmap.height()) // 2,
            scaled_pixmap,
        )
        painter.end()

        return rounded_pixmap

    def get_photo_path(self):
        """Get the path of the current photo."""
        return getattr(self, "_ProductPhotoWidget__photo_path", "")
