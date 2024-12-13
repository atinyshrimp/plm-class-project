from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QLabel, QLineEdit,
    QDateEdit, QComboBox, QPushButton, QFileDialog, QMessageBox, QSizePolicy,
    QMenu, QAction
)
from PyQt5.QtCore import Qt, QDate
from utils.table import CustomTable
import csv

class ProductionTrackingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.page_size = 10
        self.current_page = 1
        self.total_pages = 1
        self.production_data = []
        self.filtered_production_data = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Export Button
        export_button = QPushButton("Export to CSV")
        export_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        export_button.adjustSize()
        export_button.clicked.connect(self.export_data)
        main_layout.addWidget(export_button, alignment=Qt.AlignRight)

        # Filter Controls
        filter_layout = QHBoxLayout()

        # Date Range Filter
        start_date_label = QLabel("Start Date:")
        self.start_date_picker = QDateEdit()
        self.start_date_picker.setCalendarPopup(True)
        self.start_date_picker.setDate(QDate.currentDate())

        end_date_label = QLabel("End Date:")
        self.end_date_picker = QDateEdit()
        self.end_date_picker.setCalendarPopup(True)
        self.end_date_picker.setDate(QDate.currentDate())

        # Product ID Filter
        product_id_label = QLabel("Product ID:")
        self.product_id_field = QLineEdit()
        self.product_id_field.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        self.product_id_field.setPlaceholderText("Enter Product ID")

        # Factory Location Filter
        factory_label = QLabel("Factory Location:")
        self.factory_dropdown = QComboBox()
        self.factory_dropdown.setStyleSheet("""
            QComboBox {
                border: 1px solid #F4C542;
                border-radius: 5px;
                padding: 5px 10px;
                background-color: #ffffff;
                color: #333;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: none;
                background: #f8f9fa;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #ced4da;
                background-color: #ffffff;
                color: #333;
                selection-background-color: #ffe6cc;
                selection-color: #000;
                padding: 5px;
            }
        """)

        self.factory_dropdown.addItem("All")
        self.factory_dropdown.addItem("Usine A")
        self.factory_dropdown.addItem("Usine B")
        self.factory_dropdown.addItem("Usine C")

        # Button to apply filters
        self.filter_button = QPushButton("Apply Filter")
        self.filter_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.filter_button.adjustSize()
        self.filter_button.clicked.connect(self.filter_production_data)


        # Add filters to layout
        filter_layout.addWidget(start_date_label)
        filter_layout.addWidget(self.start_date_picker)
        filter_layout.addWidget(end_date_label)
        filter_layout.addWidget(self.end_date_picker)
        filter_layout.addWidget(product_id_label)
        filter_layout.addWidget(self.product_id_field)
        filter_layout.addWidget(factory_label)
        filter_layout.addWidget(self.factory_dropdown)
        filter_layout.addWidget(self.filter_button)
        main_layout.addLayout(filter_layout)

        # Production Records Table
        self.production_table = CustomTable()
        self.production_table.setColumnCount(7)
        self.production_table.setHorizontalHeaderLabels([
            "Lot ID", "Product ID", "Process Name", "Date",
            "Factory", "Ingredients", "Merchandise ID"
        ])
        self.setup_context_menu()

        main_layout.addWidget(self.production_table)

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

        self.setLayout(main_layout)

        # Load Dummy Data
        self.load_dummy_data()
        self.update_production_table()

    def load_dummy_data(self):
        """Load dummy production data for testing."""
        self.production_data = [
            ("L001", "P001", "Mixing", "2024-01-15", "Usine A", "Sugar, Water", "M001"),
            ("L002", "P002", "Filling", "2024-02-10", "Usine B", "Flour, Eggs", "M002"),
            ("L003", "P003", "Packaging", "2024-03-20", "Usine A", "Honey, Wax", "M003"),
            ("L004", "P004", "Sealing", "2024-04-25", "Usine C", "Salt, Pepper", "M004"),
            ("L005", "P005", "Labeling", "2024-05-30", "Usine A", "Oil, Herbs", "M005"),
        ]
        self.filtered_production_data = self.production_data[:]
        self.total_pages = (len(self.production_data) + self.page_size - 1) // self.page_size

        # Determine the oldest expiration and arrival dates
        earliest_date = min(row[3] for row in self.production_data)
        most_recent_date = max(row[3] for row in self.production_data)

        # Set date pickers to the oldest dates minus one day
        self.start_date_picker.setDate(QDate.fromString(earliest_date, "yyyy-MM-dd").addDays(-1))
        self.end_date_picker.setDate(QDate.fromString(most_recent_date, "yyyy-MM-dd").addDays(1))


    def update_production_table(self):
        """Update the production table for the current page."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        page_data = self.filtered_production_data[start:end]

        self.production_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data):
                self.production_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

        # Update pagination controls
        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def filter_production_data(self):
        """Filter production data based on date range, product ID, and factory location."""
        start_date = self.start_date_picker.date().toString("yyyy-MM-dd")
        end_date = self.end_date_picker.date().toString("yyyy-MM-dd")
        product_id = self.product_id_field.text().lower()
        factory = self.factory_dropdown.currentText()

        self.filtered_production_data = [
            row for row in self.production_data
            if start_date <= row[3] <= end_date  # Date Range Filter
            and (not product_id or product_id in row[1].lower())  # Product ID Filter
            and (factory == "All" or row[4] == factory)  # Factory Location Filter
        ]

        self.total_pages = (len(self.filtered_production_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_production_table()

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_production_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_production_table()

    def export_data(self):
        """Export filtered production data to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Production Data", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Lot ID", "Product ID", "Process Name", "Date",
                    "Factory", "Ingredients", "Merchandise ID"
                ])
                writer.writerows(self.filtered_production_data)
            QMessageBox.information(self, "Export Successful", f"Data exported to {file_path}")

    def setup_context_menu(self):
        self.production_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.production_table.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        """Show context menu for the selected production."""
        selected_row = self.production_table.currentRow()
        if selected_row == -1:
            return

        batch_data = self.filtered_production_data[selected_row]

        menu = QMenu(self)
        cost_details_action = QAction("View Cost Details", self)
        cost_details_action.triggered.connect(lambda: self.navigate_to_cost_details(batch_data[1]))

        menu.addAction(cost_details_action)
        menu.exec_(self.production_table.viewport().mapToGlobal(position))

    def navigate_to_cost_details(self, product_id):
        """Navigate to Cost Details tab for the selected product."""
        parent_widget = self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget()
        if hasattr(parent_widget, "switch_to_cost_tab"):
            parent_widget.switch_to_cost_tab(product_id)
