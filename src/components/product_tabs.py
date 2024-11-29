from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QTableWidgetItem, QFormLayout,
    QLineEdit, QTextEdit, QLabel, QSizePolicy
)
from utils.table import CustomTable
from widgets.product_photo_widget import ProductPhotoWidget

class ProductTabs(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        # Product Sheets Tab
        product_sheet_tab = QWidget()
        self._init_product_sheets(product_sheet_tab)

        # Batch History Tab
        batch_history_tab = QWidget()
        batch_history_layout = QVBoxLayout()
        batch_table = CustomTable(5, 3)
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

    def _init_product_sheets(self, product_sheet_tab):
        # Create the main horizontal layout for the table and details view
        product_sheet_tab_layout = QHBoxLayout()

        # Product Table (on the left, larger size)
        self.product_table = CustomTable()
        self.product_table.setColumnCount(5)
        self.product_table.setHorizontalHeaderLabels(["ID", "Nom", "Quantité", "Version", "Date de Production"])
        self.product_table.itemSelectionChanged.connect(self._display_product_details)
        self.product_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.product_table.setMinimumWidth(500)  # Set a larger minimum width for the table
        product_sheet_tab_layout.addWidget(self.product_table, stretch=3)  # Assign more space to the table

        # Product Details Form (on the right)
        details_widget = QWidget()
        details_layout = QVBoxLayout()  # Use a vertical layout for a modern stacked design

        # Group box for details
        group_box = QWidget()
        group_layout = QFormLayout()
        

        # Photo Widget
        self.photo_widget = ProductPhotoWidget()

        # Create text fields for product details
        self.id_field = QLineEdit()
        self.name_field = QLineEdit()
        self.description_field = QTextEdit()
        self.description_field.setMaximumHeight(50)
        self.quantity_field = QLineEdit()
        self.container_field = QLineEdit()
        self.version_field = QLineEdit()
        self.date_field = QLineEdit()
        self.ingredients_field = QTextEdit()

        # Make fields read-only
        for widget in [
            self.id_field, self.name_field, self.description_field, self.quantity_field,
            self.container_field, self.version_field, self.date_field, self.ingredients_field
        ]:
            widget.setReadOnly(True)

        # Create the overall layout
        group_layout = QVBoxLayout()

        # Top Row: Image and Basic Info (ID, Name, Description)
        top_row_layout = QHBoxLayout()

        # Left: Picture
        self.photo_widget = ProductPhotoWidget()
        top_row_layout.addWidget(self.photo_widget, stretch=1)

        # Right: Basic Info (ID, Name, Description)
        basic_info_layout = QFormLayout()
        basic_info_layout.addRow("", self.id_field)
        basic_info_layout.addRow("", self.name_field)
        basic_info_layout.addRow("", self.description_field)

        basic_info_widget = QWidget()
        basic_info_widget.setLayout(basic_info_layout)
        top_row_layout.addWidget(basic_info_widget, stretch=2)

        # Add the top row to the overall layout
        group_layout.addLayout(top_row_layout)

        # Remaining Fields: Quantité, Contenant ID, Version, Date, Ingrédients
        remaining_fields_layout = QFormLayout()
        remaining_fields_layout.addRow("<b>Quantité:</b>", self.quantity_field)
        remaining_fields_layout.addRow("<b>Contenant ID:</b>", self.container_field)
        remaining_fields_layout.addRow("<b>Version:</b>", self.version_field)
        remaining_fields_layout.addRow("<b>Date de Production:</b>", self.date_field)
        remaining_fields_layout.addRow("<b>Ingrédients:</b>", self.ingredients_field)

        # Add the remaining fields to the overall layout
        group_layout.addLayout(remaining_fields_layout)

        # Style the group box
        group_box.setLayout(group_layout)
        group_box.setStyleSheet("""
            QWidget {
                border: 1px solid #d3d3d3;
                border-radius: 5px;
                padding: 10px;
                background-color: #f9f9f9;
            }
            QLabel {
                font-size: 12px;
            }
            QLineEdit, QTextEdit {
                background-color: #ffffff;
                border: 1px solid #d3d3d3;
                border-radius: 3px;
                padding: 5px;
            }
        """)

        details_layout.addWidget(group_box)
        details_widget.setLayout(details_layout)
        product_sheet_tab_layout.addWidget(details_widget, stretch=2)  # Allocate less space than the table

        # Populate the table with dummy data
        self._load_dummy_data()

        # Set the layout to the specific tab
        product_sheet_tab.setLayout(product_sheet_tab_layout)

    def _load_dummy_data(self):
        dummy_data = [
            (1, "Honey Jar", 50, "1.0", "2023-10-01", "JAR001", "Pure organic honey", "Honey (90%), Beeswax (10%)", "https://m.media-amazon.com/images/I/81XTYU+nntL.jpg"),
            (2, "Berry Jam", 100, "1.1", "2023-09-15", "JAR002", "Mixed berry jam", "Strawberries (70%), Sugar (30%)", "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/4B7C3510-7041-4B5D-8000-1D10B1BA4678/Derivates/6749ac4e-586d-4055-9df2-5a96832897f6.jpg"),
            (3, "Lemon Marmalade", 75, "2.0", "2023-08-20", "JAR003", "Zesty lemon marmalade", "Lemons (60%), Sugar (40%)", "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-871488_11-35ddf4e.jpg?quality=90&resize=440,400"),
            (4, "Almond Butter", 120, "1.0", "2023-09-10", "JAR004", "Smooth almond butter", "Almonds (100%)", "https://www.inspiredtaste.net/wp-content/uploads/2020/06/Homemade-Almond-Butter-Recipe-1200.jpg"),
            (5, "Herbal Honey", 60, "1.2", "2023-11-01", "JAR005", "Infused with natural herbs", "Honey (85%), Herbs (15%)", "https://www.herbco.com/images/page/herbalhoney/images/RECIPE-honey-spread2.jpg"),
        ]

        self.product_table.setRowCount(len(dummy_data))
        for row_index, row_data in enumerate(dummy_data):
            for col_index, col_data in enumerate(row_data[:5]):
                self.product_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

        self.dummy_data = dummy_data
        self.product_table.resizeColumnsToContents()

    def _display_product_details(self):
        """Display detailed information about the selected product."""
        selected_row = self.product_table.currentRow()
        if selected_row == -1:
            return

        product = self.dummy_data[selected_row]
        self.photo_widget.set_photo(str(product[8]))  # Set the photo
        self.id_field.setText(str(product[0]))
        self.name_field.setText(product[1])
        self.description_field.setText(product[6])  # Description
        self.quantity_field.setText(str(product[2]))
        self.container_field.setText(product[5])  # Contenant ID
        self.version_field.setText(product[3])
        self.date_field.setText(product[4])  # Date
        self.ingredients_field.setText(product[7])  # Ingredients
