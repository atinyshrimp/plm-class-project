from PyQt5.QtWidgets import QListWidget, QWidget, QTabWidget, QLabel, QVBoxLayout
from components.product_tabs import create_table_tab

def create_list_tab(label):
    tab = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel(label))
    layout.addWidget(QListWidget())
    tab.setLayout(layout)
    return tab

def init_people_tabs():
    """Initialize people-related tabs."""
    people_tab_widget = QTabWidget()
    supplier_tab = create_table_tab(["Supplier", "Material", "Availability"])
    rnd_tab = create_list_tab("R&D Projects")

    people_tab_widget.addTab(supplier_tab, "Supplier Tracking")
    people_tab_widget.addTab(rnd_tab, "R&D Projects")
    
    return people_tab_widget