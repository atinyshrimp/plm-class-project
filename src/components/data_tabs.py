from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QSizePolicy
from utils.table import CustomTable

class DataTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Cost Details Tab
        cost_tab = QWidget()
        cost_layout = QVBoxLayout()
        cost_table = CustomTable(5, 3)  # Example: 5 rows, 3 columns
        cost_table.setHorizontalHeaderLabels(["Item", "Cost", "Quantity"])
        cost_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        cost_layout.addWidget(cost_table)
        cost_tab.setLayout(cost_layout)

        # Stock and Location Tab
        stock_tab = QWidget()
        stock_layout = QVBoxLayout()
        stock_table = CustomTable(5, 3)  # Example: 5 rows, 3 columns
        stock_table.setHorizontalHeaderLabels(["Location", "Product", "Available Stock"])
        stock_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        stock_layout.addWidget(stock_table)
        stock_tab.setLayout(stock_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(cost_tab, "Cost Details")
        tab_widget.addTab(stock_tab, "Stock & Location")

        # Main layout for DataTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)