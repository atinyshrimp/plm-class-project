from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QSizePolicy, QLineEdit
from utils.table import CustomTable
from .tabs.batch_history_tab import BatchHistoryTab

class DataTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Batch History Tab
        self.batch_history_tab = BatchHistoryTab()
        tab_widget.addTab(self.batch_history_tab, "Batch History")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def create_batch_history_tab(self):
        """Create the Batch History tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        table = CustomTable(8, 7)
        table.setHorizontalHeaderLabels([
            "Lot ID", "Product ID", "Quantity", "Production Date",
            "Expiry Date", "Status", "Return"
        ])
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(table)

        search_field = QLineEdit()
        search_field.setPlaceholderText("Search by Lot ID...")
        layout.addWidget(search_field)
        tab.setLayout(layout)
        return tab
