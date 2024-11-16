from PyQt5.QtWidgets import QListWidget

class NavBar(QListWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.insertItem(0, "Product")
        self.insertItem(1, "People")
        self.insertItem(2, "Process")
        self.insertItem(3, "Data")
        self.setFixedWidth(180)
        self.setSpacing(10)
        self.setCurrentRow(0)  # Default selection