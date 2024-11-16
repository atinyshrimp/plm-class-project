from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QListWidget, QSizePolicy
from utils.table import CustomTable

class PeopleTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Supplier Tracking Tab
        supplier_tab = QWidget()
        supplier_layout = QVBoxLayout()
        supplier_table = CustomTable(5, 3)  # Example: 5 rows, 3 columns
        supplier_table.setHorizontalHeaderLabels(["Supplier", "Material", "Availability"])
        supplier_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        supplier_layout.addWidget(supplier_table)
        supplier_tab.setLayout(supplier_layout)

        # R&D Projects Tab
        rnd_tab = QWidget()
        rnd_layout = QVBoxLayout()
        rnd_project_list = QListWidget()
        rnd_layout.addWidget(QLabel("R&D Projects"))
        rnd_layout.addWidget(rnd_project_list)
        rnd_tab.setLayout(rnd_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(supplier_tab, "Supplier Tracking")
        tab_widget.addTab(rnd_tab, "R&D Projects")

        # Main layout for PeopleTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)