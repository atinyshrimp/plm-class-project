from PyQt5.QtWidgets import QTabWidget
from components.product_tabs import create_table_tab

def init_data_tabs():
    """Initialize data-related tabs."""
    data_tab_widget = QTabWidget()
    
    cost_tab = create_table_tab(["Item", "Cost", "Quantity"])
    stock_tab = create_table_tab(["Location", "Product", "Available Stock"])

    data_tab_widget.addTab(cost_tab, "Cost Details")
    data_tab_widget.addTab(stock_tab, "Stock & Location")
    
    return data_tab_widget
