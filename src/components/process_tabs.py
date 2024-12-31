from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QComboBox, QLabel, QProgressBar, QSizePolicy
from utils.table import CustomTable
from .tabs.production_tracking_tab import ProductionTrackingTab
from .tabs.supplier_availability_tab import SupplierAvailabilityTab

class ProcessTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Production Tracking Tab
        production_tab = ProductionTrackingTab()

        # Supplier Availability Tab
        process_history_tab = SupplierAvailabilityTab()

        # Add tabs to the tab widget
        tab_widget.addTab(production_tab, "Production Tracking")
        tab_widget.addTab(process_history_tab, "Supplier Availability")

        # Main layout for ProcessTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
