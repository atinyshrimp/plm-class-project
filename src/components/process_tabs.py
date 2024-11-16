from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QComboBox, QLabel, QProgressBar, QSizePolicy
from utils.table import CustomTable

class ProcessTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Production Tracking Tab
        production_tab = QWidget()
        production_layout = QVBoxLayout()
        production_stage_combo = QComboBox()
        production_stage_combo.addItems(["Raw Materials", "In Production", "Packaging", "Completed"])
        production_progress = QProgressBar()
        production_progress.setValue(50)
        production_layout.addWidget(QLabel("Production Stage:"))
        production_layout.addWidget(production_stage_combo)
        production_layout.addWidget(production_progress)
        production_tab.setLayout(production_layout)

        # Process History Tab
        process_history_tab = QWidget()
        process_history_layout = QVBoxLayout()
        process_table = CustomTable(5, 3)  # Example: 5 rows, 3 columns
        process_table.setHorizontalHeaderLabels(["Process ID", "Date", "Stage"])
        process_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        process_history_layout.addWidget(process_table)
        process_history_tab.setLayout(process_history_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(production_tab, "Production Tracking")
        tab_widget.addTab(process_history_tab, "Process History")

        # Main layout for ProcessTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
