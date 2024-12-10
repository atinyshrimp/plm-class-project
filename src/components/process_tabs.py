from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QSizePolicy, QLineEdit
from utils.table import CustomTable

class ProcessTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Production Tracking Tab
        tab_widget.addTab(self.create_production_tracking_tab(), "Production Tracking")

        # Supplier Availability Tab
        tab_widget.addTab(self.create_supplier_tab(), "Supplier Availability")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def create_production_tracking_tab(self):
        """Create the Production Tracking tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        search_field = QLineEdit()
        search_field.setPlaceholderText("Search by Lot ID or Process Name...")
        layout.addWidget(search_field)

        table = CustomTable(8, 7)
        table.setHorizontalHeaderLabels([
            "Lot ID", "Process Name", "Date", "Product ID",
            "Goods ID", "Ingredients", "Factory"
        ])
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(table)

        tab.setLayout(layout)
        return tab

    def create_supplier_tab(self):
        """Create the Supplier Availability tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        search_field = QLineEdit()
        search_field.setPlaceholderText("Search by Supplier or Goods ID...")
        layout.addWidget(search_field)

        table = CustomTable(8, 7)
        table.setHorizontalHeaderLabels([
            "Goods ID", "Contract Date", "Delivery Date",
            "Ingredient", "Quantity", "Delivery Factory", "Supplier"
        ])
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(table)

        tab.setLayout(layout)
        return tab