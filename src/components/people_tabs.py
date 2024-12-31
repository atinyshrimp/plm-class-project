from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from .tabs.distribution_tracking_tab import DistributionTrackingTab

class PeopleTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Add tabs to the tab widget
        self.distribution_tab = DistributionTrackingTab()
        tab_widget.addTab(self.distribution_tab, "Supplier Tracking")

        # Main layout for PeopleTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)