from PyQt5.QtWidgets import QWidget, QTabWidget, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QTextEdit, QSizePolicy, QPushButton
from utils.table import CustomTable

class ProductTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Product Sheets Tab
        product_sheet_tab = QWidget()
        product_form_layout = QFormLayout()
        product_form_layout.addRow(QLabel("Product Code:"), QLineEdit())
        product_form_layout.addRow(QLabel("Product Name:"), QLineEdit())
        product_form_layout.addRow(QLabel("Description:"), QTextEdit())
        product_form_layout.addRow(QLabel("Production Date:"), QLineEdit())  # You can replace this with a QDateEdit if needed
        product_form_layout.addRow(QLabel("Photo:"), QPushButton("Upload Photo"))  # Photo upload button
        product_sheet_tab.setLayout(product_form_layout)

        # Batch History Tab
        batch_history_tab = QWidget()
        batch_history_layout = QVBoxLayout()
        batch_table = CustomTable(5, 3)  # Example: 5 rows, 3 columns
        batch_table.setHorizontalHeaderLabels(["Batch Number", "Date", "Status"])
        batch_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        batch_history_layout.addWidget(batch_table)
        batch_history_tab.setLayout(batch_history_layout)

        # Market Studies Tab
        market_study_tab = QWidget()
        market_study_layout = QVBoxLayout()
        market_study_layout.addWidget(QLabel("Market Study Results:"))
        market_study_layout.addWidget(QTextEdit())
        market_study_tab.setLayout(market_study_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(product_sheet_tab, "Product Sheets")
        tab_widget.addTab(batch_history_tab, "Batch History")
        tab_widget.addTab(market_study_tab, "Market Studies")

        # Main layout for ProductTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
