import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)


class PhotoFileInput(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.file_name = None
        self.__init_ui()

    def __init_ui(self):
        self.layout = QHBoxLayout()

        self.label = QLabel("No file chosen", self)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Choose Photo", self)
        self.button.clicked.connect(self.__show_file_dialog)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setWindowTitle("Photo File Input")

    def __show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Choose Photo",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
            options=options,
        )
        if fileName:
            self.file_path = fileName
            self.file_name = fileName.split("/")[-1]
            self.label.setText(self.file_name)

    def setText(self, text):
        self.file_path = text
        self.file_name = text.split("/")[-1]
        self.label.setText(self.file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PhotoFileInput()
    ex.show()
    sys.exit(app.exec_())
