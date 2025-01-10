from PyQt5.QtWidgets import QListWidget
from database.databaseManager import SQLiteManager


class NavBar(QListWidget):
    def __init__(self, db_manager: SQLiteManager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        self.insertItem(0, "Product")
        self.insertItem(1, "People")
        self.insertItem(2, "Process")
        self.insertItem(3, "Data")
        if self.db_manager.is_admin:
            self.insertItem(4, "Database")
        self.setFixedWidth(180)
        self.setSpacing(10)
        self.setCurrentRow(0)  # Default selection
