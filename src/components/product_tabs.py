from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QTableWidgetItem, QGridLayout,
    QLineEdit, QTextEdit, QLabel, QSizePolicy, QPushButton
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from utils.table import CustomTable
from widgets.product_photo_widget import ProductPhotoWidget

class ProductTabs(QWidget):
    def __init__(self):
        super().__init__()
        
         # Initialize all fields before calling init_ui
        self.id_field = QLineEdit()
        self.name_field = QLineEdit()
        self.description_field = QTextEdit()
        self.quantity_field = QLineEdit()
        self.container_field = QLineEdit()
        self.version_field = QLineEdit()
        self.date_field = QLineEdit()
        self.ingredients_field = QTextEdit()
        
        # Pagination Configuration
        self.page_size = 10  # Number of rows per page
        self.current_page = 1  # Current page
        self.total_pages = 1  # Total pages
        self.dummy_data = []  # Store product data
        self.filtered_data = [] # 
        
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
        overall_tab_layout = QVBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search by name, ID, or container...")
        self.search_field.textChanged.connect(self.__filter_products)
        
        self.search_field.setContentsMargins(10, 0, 20, 0)

        overall_tab_layout.addWidget(self.search_field)
        
        product_sheet_tab_layout = QHBoxLayout()
        
        # Product Table (on the left, larger size)
        table_layout = QVBoxLayout()
        self.product_table = CustomTable()
        self.product_table.setColumnCount(5)
        self.product_table.setHorizontalHeaderLabels(["ID", "Name", "Quantity", "Version", "Production Date"])
        self.product_table.itemSelectionChanged.connect(self._display_product_details)
        self.product_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.product_table.setMinimumWidth(500)  # Set a larger minimum width for the table
        
        # Monitor selection changes
        selection_model = self.product_table.selectionModel()
        selection_model.selectionChanged.connect(self._on_selection_changed)

        table_layout.addWidget(self.product_table)
        
        # Add pagination controls
        pagination_layout = QHBoxLayout()
        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self._go_to_previous_page)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self._go_to_next_page)
        self.page_label = QLabel("Page 1 of 1")
        self.page_label.setAlignment(Qt.AlignCenter)

        pagination_layout.addWidget(self.previous_button)
        pagination_layout.addWidget(self.page_label)
        pagination_layout.addWidget(self.next_button)
        table_layout.addLayout(pagination_layout)
        
        product_sheet_tab_layout.addLayout(table_layout, stretch=3)  # Assign more space to the table

        # Product Details Form (on the right)
        details_widget = QWidget()
        details_layout = QVBoxLayout()  # Use a vertical layout for a modern stacked design

        # Group box for details with a more modern look
        details_group_box = QWidget()
        details_group_box.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 12px;
            }
        """)
        details_group_layout = QVBoxLayout()

        # Photo Section
        photo_section = QHBoxLayout()
        self.photo_widget = ProductPhotoWidget()
        photo_section.addStretch(1)
        photo_section.addWidget(self.photo_widget)
        photo_section.addStretch(1)
        details_group_layout.addLayout(photo_section)

        # Details Grid
        details_grid = QGridLayout()
        details_grid.setSpacing(5)
        details_grid.setColumnStretch(1, 2)

        # Create a list of field labels and corresponding attributes
        field_info = [
            ("ID", self.id_field),
            ("Name", self.name_field),
            ("Quantity", self.quantity_field),
            ("Container", self.container_field),
            ("Version", self.version_field),
            ("Production Date", self.date_field)
        ]

        # Create fields with modern styling
        for row, (label, field) in enumerate(field_info):
            label_widget = QLabel(f"<b>{label}:</b>")
            label_widget.setStyleSheet("""
                QLabel {
                    color: #333;
                    font-size: 14px;
                    padding: 0;
                }
            """)
            
            field.setReadOnly(True)
            field.setStyleSheet("""
                QLineEdit {
                    background-color: #f8f9fa;
                    border: 1px solid #ced4da;
                    border-radius: 4px;
                    padding: 6px;
                    font-size: 14px;
                }
                QLineEdit:focus {
                    border-color: #80bdff;
                }
            """)
            
            details_grid.addWidget(label_widget, row, 0)
            details_grid.addWidget(field, row, 1)

        # Description Section
        description_label = QLabel("<b>Description:</b>")
        description_label.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 14px;
                padding: 0;
            }
        """)
        self.description_field.setReadOnly(True)
        self.description_field.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 6px;
                font-size: 14px;
            }
        """)

        # Ingredients Section
        ingredients_label = QLabel("<b>Ingredients:</b>")
        ingredients_label.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 14px;
            }
        """)
        self.ingredients_field.setReadOnly(True)
        self.ingredients_field.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 6px;
                font-size: 14px;
            }
        """)

        # Add sections to the layout
        details_group_layout.addLayout(details_grid)
        details_group_layout.addWidget(description_label)
        details_group_layout.addWidget(self.description_field)
        details_group_layout.addWidget(ingredients_label)
        details_group_layout.addWidget(self.ingredients_field)

        # Set layout for the group box
        details_group_box.setLayout(details_group_layout)

        # Add the group box to the details layout
        details_layout.addWidget(details_group_box)
        details_widget.setLayout(details_layout)

        # Add details widget to the main layout
        product_sheet_tab_layout.addWidget(details_widget, stretch=2)

        # Set the layout to the specific tab
        product_sheet_tab_layout.setContentsMargins(10, 10, 10, 10)  # Add some padding
        overall_tab_layout.addLayout(product_sheet_tab_layout)
        product_sheet_tab.setLayout(overall_tab_layout)
        
        # Populate the table
        self._load_dummy_data()
        self._update_table()

    def _load_dummy_data(self):
        self.dummy_data = [
            (1, "Honey Jar", 50, "1.0", "2023-10-01", "JAR001", "Pure organic honey", "Honey (90%), Beeswax (10%)", "https://m.media-amazon.com/images/I/81XTYU+nntL.jpg"),
            (2, "Berry Jam", 100, "1.1", "2023-09-15", "JAR002", "Mixed berry jam", "Strawberries (70%), Sugar (30%)", "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/4B7C3510-7041-4B5D-8000-1D10B1BA4678/Derivates/6749ac4e-586d-4055-9df2-5a96832897f6.jpg"),
            (3, "Lemon Marmalade", 75, "2.0", "2023-08-20", "JAR003", "Zesty lemon marmalade", "Lemons (60%), Sugar (40%)", "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-871488_11-35ddf4e.jpg?quality=90&resize=440,400"),
            (4, "Almond Butter", 120, "1.0", "2023-09-10", "JAR004", "Smooth almond butter", "Almonds (100%)", "https://www.inspiredtaste.net/wp-content/uploads/2020/06/Homemade-Almond-Butter-Recipe-1200.jpg"),
            (5, "Herbal Honey", 60, "1.2", "2023-11-01", "JAR005", "Infused with natural herbs", "Honey (85%), Herbs (15%)", "https://www.herbco.com/images/page/herbalhoney/images/RECIPE-honey-spread2.jpg"),
            (6, "Chocolate Spread", 110, "2.0", "2023-06-15", "JAR006", "", "", "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/8EABE1FD-5729-4A87-828E-B8C57603E5EA/Derivates/A57910CF-D62E-4713-9E77-1C281412D3DF.jpg"),
            (7, "Strawberry Jam", 90, "1.3", "2023-07-01", "JAR002", "", "", "https://itsnotcomplicatedrecipes.com/wp-content/uploads/2022/01/Strawberry-Jam-Feature.jpg"),
            (8, "Blueberry Jam", 80, "1.0", "2023-05-20", "JAR002", "", "", "https://www.wildernesswife.com/wp-content/uploads/2023/09/blueberry_jam1.jpg"),
            (9, "Peanut Butter", 150, "1.2", "2023-04-10", "JAR004", "", "", "https://pinchofyum.com/wp-content/uploads/Homemade-Peanut-Butter-Square.png"),
            (10, "Citrus Marmalade", 70, "2.1", "2023-03-01", "JAR003", "", "", "https://www.bigbearfarms.in/cdn/shop/products/ThreeCitrusMarmalade-1.png?v=1663151497"),
            (11, "Caramel Sauce", 40, "1.0", "2023-02-01", "JAR001", "", "", "https://handletheheat.com/wp-content/uploads/2022/06/caramel-sauce-SQUARE-1.png"),
            (12, "Organic Honey", 55, "1.0", "2023-01-15", "JAR005", "", "", "https://cdn.shopify.com/s/files/1/0262/6374/8713/files/organic-honey_1000x.png?v=1726646497"),
        ]

        self.filtered_data = self.dummy_data[:] # Initialize filtered data with all products
        self.page_size = 5
        self.total_pages = (len(self.dummy_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        
    def _update_table(self):
        """Update the table to display the current page's data."""
        self.product_table.clearContents()
        start = (self.current_page - 1) * self.page_size
        end = min(start + self.page_size, len(self.filtered_data))  # Use filtered data
        page_data = self.filtered_data[start:end]

        self.product_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data[:5]):  # Limit to displayed columns
                self.product_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

        # Update pagination controls
        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def _go_to_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self._update_table()

    def _go_to_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self._update_table()

    def _display_product_details(self):
        """Display detailed information about the selected product."""
        selected_row = self.product_table.currentRow()
        if selected_row == -1:
            self.__clear_details_view()
            return

        product = self.dummy_data[selected_row]
        self.photo_widget.set_photo(str(product[8]))  # Set the photo
        self.id_field.setText(str(product[0]))
        self.name_field.setText(product[1])
        self.description_field.setText(product[6])  # Description
        self.quantity_field.setText(str(product[2]))
        self.container_field.setText(product[5])  # Container ID
        self.version_field.setText(product[3])
        self.date_field.setText(product[4])  # Date
        self.ingredients_field.setText(product[7])  # Ingredients
        
    def __clear_details_view(self):
        self.photo_widget.photo_label.setPixmap(QPixmap())
        self.photo_widget.photo_label.setText("No Image Found")
        
        self.id_field.setText("")
        self.name_field.setText("")
        self.description_field.setText("")  # Description
        self.quantity_field.setText("")
        self.container_field.setText("")  # Container ID
        self.version_field.setText("")
        self.date_field.setText("")  # Date
        self.ingredients_field.setText("")  # Ingredients

    def __filter_products(self):
        """Filter based on `Name` field
        """
        filter_text = self.search_field.text().lower()
        self.filtered_data = [product for product in self.dummy_data if filter_text in product[1].lower()]  # Filter by Name (column 1)
    
        # Reset pagination for filtered data
        self.total_pages = (len(self.filtered_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        
        # Update the table to show the filtered data
        self._update_table()

    def _reset_filter(self):
        """Reset the search filter and show all data."""
        self.filtered_data = self.dummy_data[:]  # Reset to full dataset
        self.search_field.clear()  # Clear the search input
        self.total_pages = (len(self.filtered_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self._update_table()


    def _on_selection_changed(self, selected, deselected):
        """Handle selection changes and clear the detailed view if nothing is selected."""
        if not self.product_table.selectionModel().hasSelection():  # No rows selected
            self.__clear_details_view()

