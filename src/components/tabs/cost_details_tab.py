from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QTableWidgetItem, QMenu, QAction, QFileDialog
from utils.table import CustomTable
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import csv

class ProductCostDetailsTab(QWidget):
    def __init__(self,db_manager):
        super().__init__()
        self.page_size = 10
        self.current_page = 1
        self.total_pages = 1
        self.db_manager = db_manager
        self.cost_data = []
        self.filtered_cost_data = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # Search Bar
        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search by Product ID...")
        self.search_field.textChanged.connect(self.filter_cost_data)
        search_layout.addWidget(self.search_field)

        # Add a refresh button
        export_button = QPushButton("Export to CSV")
        export_button.clicked.connect(self.export_cost_details)
        search_layout.addWidget(export_button)
        main_layout.addLayout(search_layout)

        # Filter Controls
        filter_layout = QHBoxLayout()

        # Cost Range Filter
        self.min_cost_field = QLineEdit()
        self.min_cost_field.setPlaceholderText("Min Production Cost")
        self.min_cost_field.textChanged.connect(self.filter_cost_data)
        self.max_cost_field = QLineEdit()
        self.max_cost_field.setPlaceholderText("Max Production Cost")
        self.max_cost_field.textChanged.connect(self.filter_cost_data)

        # Margin Filter
        self.negative_margin_filter = QPushButton("Show Negative Margins Only")
        self.negative_margin_filter.setCheckable(True)
        self.negative_margin_filter.clicked.connect(self.filter_cost_data)

        # Add to layout
        filter_layout.addWidget(QLabel("Cost Range:"))
        filter_layout.addWidget(self.min_cost_field)
        filter_layout.addWidget(self.max_cost_field)
        filter_layout.addWidget(self.negative_margin_filter)
        main_layout.addLayout(filter_layout)

        # Table for Cost Details
        self.cost_table = CustomTable()
        self.cost_table.setColumnCount(7)
        self.cost_table.setHorizontalHeaderLabels([
            "Product ID", "Production Cost (€)", "Raw Materials Cost (€)", "Marketing Cost (€)",
            "Selling Price (€)", "Total Cost (€)", "Margin (%)"
        ])
         # Enable context menu on the table
        self.cost_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.cost_table.customContextMenuRequested.connect(self.show_context_menu)
        main_layout.addWidget(self.cost_table)

        # Pagination Controls
        pagination_layout = QHBoxLayout()
        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.go_to_previous_page)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.go_to_next_page)
        self.page_label = QLabel("Page 1 of 1")
        pagination_layout.addWidget(self.previous_button)
        pagination_layout.addWidget(self.page_label, alignment=Qt.AlignCenter)
        pagination_layout.addWidget(self.next_button)
        main_layout.addLayout(pagination_layout)

        # Cost Summary
        self.summary_label = QLabel("Total Costs: -")
        main_layout.addWidget(self.summary_label)

        self.setLayout(main_layout)

        # Load Dummy Data
        self.load_data()
        self.update_cost_table()

    def load_data(self):
        """Load dummy cost data for testing."""
        self.cost_data = self.db_manager.fetch_query('fetch_cost_details')
        '''[
            ("P001", 500, 200, 100, 1000),
            ("P002", 600, 250, 150, 1200),
            ("P003", 550, 300, 200, 1300),
            ("P004", 700, 350, 250, 1500),
            ("P005", 400, 150, 100, 900),
            ("P006", 450, 180, 120, 950),
        ]'''

        # Add Total Cost and Margin as calculated columns
        self.cost_data = [
            row + (row[1] + row[2] + row[3], (row[4] - (row[1] + row[2] + row[3])) / row[4] * 100) for row in self.cost_data
        ]
        self.filtered_cost_data = self.cost_data[:]
        self.total_pages = (len(self.cost_data) + self.page_size - 1) // self.page_size

    def update_cost_table(self):
        """Update the table for the current page."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        page_data = self.filtered_cost_data[start:end]

        self.cost_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(f"{col_data:.2f}" if isinstance(col_data, float) else str(col_data))

                # Highlight rows with negative margins
                if col_index == 6 and col_data < 0:
                    item.setBackground(QColor("#ffcccc"))  # Light red background

                self.cost_table.setItem(row_index, col_index, item)

        # Update pagination controls
        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

        # Update the summary
        self.update_cost_summary()

    def update_cost_summary(self):
        """Update the cost summary based on the filtered data."""
        total_production = sum(row[1] for row in self.filtered_cost_data)
        total_raw_materials = sum(row[2] for row in self.filtered_cost_data)
        total_marketing = sum(row[3] for row in self.filtered_cost_data)
        total_costs = sum(row[5] for row in self.filtered_cost_data)

        self.summary_label.setText(
            f"Total Costs - Production: €{total_production}, Raw Materials: €{total_raw_materials}, "
            f"Marketing: €{total_marketing}, Overall: €{total_costs}"
        )

    def filter_cost_data(self):
        """Filter cost data based on search input."""
        filter_text = self.search_field.text().lower()
        self.filtered_cost_data = [
            row for row in self.cost_data
            if filter_text in row[0].lower() or filter_text in row[0].lower()
        ]
        self.total_pages = (len(self.filtered_cost_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_cost_table()
     
    def export_cost_details(self):
        """Export batch history to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export to CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        # Write data to CSV
        with open(file_path, "w", newline="", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Product ID", "Production Cost (€)", "Raw Materials Cost (€)", "Marketing Cost (€)",
                "Selling Price (€)", "Total Cost (€)", "Margin (%)"
            ])  # Header
            writer.writerows(self.filtered_cost_data)  # Rows

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_cost_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_cost_table()

    def show_context_menu(self, position):
        """Show a context menu with actions for the selected product."""
        selected_row = self.cost_table.currentRow()
        if selected_row == -1:
            return

        product_id = self.cost_table.item(selected_row, 0).text()

        menu = QMenu(self)
        
        link_action = QAction(f"View Product Details ({product_id})", self)
        link_action.triggered.connect(lambda: self.navigate_to_product_tab(product_id))
        menu.addAction(link_action)
        
        link_batch_action = QAction(f"View Batch History ({product_id})", self)
        link_batch_action.triggered.connect(lambda: self.navigate_to_batch_tab(product_id))
        menu.addAction(link_batch_action)

        menu.exec_(self.cost_table.viewport().mapToGlobal(position))
        
    def navigate_to_product_tab(self, product_id):
        """Navigate to the Product Sheets tab and focus on the selected product."""
        parent_widget = self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget()
        if hasattr(parent_widget, "switch_to_product_tab"):
            parent_widget.switch_to_product_tab(product_id)
        
    def navigate_to_batch_tab(self, product_id):
        """Navigate to the Batch History tab and filter by the given product."""
        parent_widget = self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget()
        print(parent_widget)
        if hasattr(parent_widget, "switch_to_batch_tab"):
            parent_widget.switch_to_batch_tab(product_id)
            return

    def filter_cost_data(self):
        """Filter cost data based on search input and advanced filters."""
        filter_text = self.search_field.text().lower()
        min_cost = float(self.min_cost_field.text() or 0)
        max_cost = float(self.max_cost_field.text() or float("inf"))
        show_negative_margins = self.negative_margin_filter.isChecked()
        
        # Change button label if it's checked
        if (self.negative_margin_filter.isChecked()):
            self.negative_margin_filter.setText("Show All Margins")
        else:
            self.negative_margin_filter.setText("Show Negative Margins Only")  

        self.filtered_cost_data = [
            row for row in self.cost_data
            if (filter_text in row[0].lower()) and  # Search by Product ID
            (min_cost <= row[1] <= max_cost) and  # Production Cost in Range
            (not show_negative_margins or row[6] < 0)  # Negative Margins
        ]

        self.total_pages = (len(self.filtered_cost_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_cost_table()
