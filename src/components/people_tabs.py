from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QListWidget, QSizePolicy, QLineEdit
from utils.table import CustomTable

class PeopleTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Distribution Tracking Tab
        tab_widget.addTab(self.create_distribution_tab(), "Distribution Tracking")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def create_distribution_tab(self):
        """Create the Distribution tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        search_field = QLineEdit()
        search_field.setPlaceholderText("Search by Distributor or Lot ID...")
        layout.addWidget(search_field)

        table = CustomTable(8, 8)
        table.setHorizontalHeaderLabels([
            "Delivery Date", "Contract Date", "Lot",
            "Lot Quantity", "Departure Warehouse",
            "Distributor", "Distributor Location", "Product ID"
        ])
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(table)

        tab.setLayout(layout)
        return tab
