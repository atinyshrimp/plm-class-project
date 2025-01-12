from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from .tabs.distribution_tracking_tab import DistributionTrackingTab


class PeopleTabs(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        """Initialize the UI for the PeopleTabs."""
        tab_widget = QTabWidget()

        # Add tabs to the tab widget
        self.distribution_tab = DistributionTrackingTab(self.db_manager)
        tab_widget.addTab(self.distribution_tab, "Supplier Tracking")

        # Main layout for PeopleTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def refresh(self):
        """Refresh the table in the active tab."""
        self.distribution_tab.refresh_table()
