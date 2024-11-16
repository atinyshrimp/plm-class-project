from PyQt5.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QTextEdit
from utils.table import CustomTable

def create_form_tab(labels):
    tab = QWidget()
    layout = QFormLayout()
    for label in labels:
        layout.addRow(QLabel(f"{label}:"), QLineEdit())
    tab.setLayout(layout)
    return tab

def create_table_tab(headers, example_data=False):
    table = CustomTable(headers=headers)
    if example_data:
        table.setItem(0, 0, QTableWidgetItem("Batch 001"))
        table.setItem(0, 1, QTableWidgetItem("2023-10-10"))
        table.setItem(0, 2, QTableWidgetItem("Complete"))
    tab = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(table)
    tab.setLayout(layout)
    return tab

def create_text_edit_tab(label):
    tab = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel(label))
    layout.addWidget(QTextEdit())
    tab.setLayout(layout)
    return tab

def init_product_tabs():
    product_tab_widget = QTabWidget()
    product_sheet_tab = create_form_tab(["Product Code", "Product Name", "Description"])
    batch_history_tab = create_table_tab(["Batch Number", "Date", "Status"], example_data=True)
    market_study_tab = create_text_edit_tab("Market Study Results")

    product_tab_widget.addTab(product_sheet_tab, "Product Sheets")
    product_tab_widget.addTab(batch_history_tab, "Batch History")
    product_tab_widget.addTab(market_study_tab, "Market Studies")

    return product_tab_widget