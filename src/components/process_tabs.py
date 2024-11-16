from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QProgressBar, QLabel, QTabWidget
from components.product_tabs import create_table_tab

def create_progress_bar_tab(label, stages):
    tab = QWidget()
    layout = QVBoxLayout()
    combo = QComboBox()
    combo.addItems(stages)
    progress = QProgressBar()
    progress.setValue(50)
    
    layout.addWidget(QLabel(label))
    layout.addWidget(combo)
    layout.addWidget(progress)
    tab.setLayout(layout)
    return tab

def init_process_tabs():
    """Initialize process-related tabs."""
    process_tab_widget = QTabWidget()
    
    production_tab = create_progress_bar_tab("Production Stage", ["Raw Materials", "In Production", "Packaging", "Completed"])
    distribution_tab = create_table_tab(["Distribution Center", "Product", "Status"])

    process_tab_widget.addTab(production_tab, "Production Tracking")
    process_tab_widget.addTab(distribution_tab, "Distribution Tracking")
    
    return process_tab_widget
