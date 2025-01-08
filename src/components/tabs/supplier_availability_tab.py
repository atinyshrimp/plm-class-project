from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QLineEdit,
    QPushButton, QTableWidgetItem, QFileDialog, QMessageBox, QSizePolicy,
    QMenu, QAction
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor
from utils.table import CustomTable
from dialogs.supplier_contact_window import SupplierContactDialog
from dialogs.supplier_analytics_window import SupplierAnalyticsWindow
import csv


class SupplierAvailabilityTab(QWidget):
    def __init__(self,db_manager):
        super().__init__()
        self.page_size = 10
        self.current_page = 1
        self.total_pages = 1
        self.db_manager = db_manager
        self.supplier_data = []
        self.filtered_supplier_data = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Buttons Layout
        buttons_layout = QHBoxLayout()

        # Supplier Analytics Button
        analytics_button = QPushButton("View Supplier Analytics")
        analytics_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        analytics_button.adjustSize()
        analytics_button.clicked.connect(self.show_supplier_analytics)
        buttons_layout.addWidget(analytics_button)


        # Export Button
        export_button = QPushButton("Export to CSV")
        export_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        export_button.adjustSize()
        export_button.clicked.connect(self.export_data)
        buttons_layout.addWidget(export_button)

        buttons_layout.setAlignment(Qt.AlignRight)
        main_layout.addLayout(buttons_layout)

        # Filter Controls
        filter_layout = QHBoxLayout()

        # Date Range Filter
        start_date_label = QLabel("Start Delivery Date:")
        self.start_date_picker = QDateEdit()
        self.start_date_picker.setCalendarPopup(True)
        self.start_date_picker.setDate(QDate.currentDate())
        self.start_date_picker.dateChanged.connect(self.filter_supplier_data)

        end_date_label = QLabel("End Delivery Date:")
        self.end_date_picker = QDateEdit()
        self.end_date_picker.setCalendarPopup(True)
        self.end_date_picker.setDate(QDate.currentDate())
        self.end_date_picker.dateChanged.connect(self.filter_supplier_data)

        # Supplier/Ingredient Filter (optional)
        supplier_label = QLabel("Supplier Name:")
        self.supplier_field = QLineEdit()
        self.supplier_field.setPlaceholderText("Enter Supplier Name or ID")
        self.supplier_field.textChanged.connect(self.filter_supplier_data)

        ingredient_label = QLabel("Ingredient:")
        self.ingredient_field = QLineEdit()
        self.ingredient_field.setPlaceholderText("Enter Ingredient")
        self.ingredient_field.textChanged.connect(self.filter_supplier_data)

        # Add filters to layout
        filter_layout.addWidget(start_date_label)
        filter_layout.addWidget(self.start_date_picker)
        filter_layout.addWidget(end_date_label)
        filter_layout.addWidget(self.end_date_picker)
        filter_layout.addWidget(supplier_label)
        filter_layout.addWidget(self.supplier_field)
        filter_layout.addWidget(ingredient_label)
        filter_layout.addWidget(self.ingredient_field)
        main_layout.addLayout(filter_layout)

        # Supplier Data Table
        self.supplier_table = CustomTable()
        self.supplier_table.setColumnCount(6)
        self.supplier_table.setHorizontalHeaderLabels([
            "Merchandise ID", "Delivery Date", "Ingredient",
            "Quantity", "Factory Location", "Supplier Name"
        ])
        self.supplier_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.supplier_table.customContextMenuRequested.connect(self.show_context_menu)
        main_layout.addWidget(self.supplier_table)

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
        self.load_data()
        self.update_supplier_table()

    def show_context_menu(self, position):
        """Show context menu for the selected production."""
        selected_row = self.supplier_table.currentRow()
        if selected_row == -1:
            return

        supplier_data = self.filtered_supplier_data[selected_row]

        menu = QMenu(self)

        supplier_contact_action = QAction("Contact Supplier", self)
        supplier_contact_action.triggered.connect(lambda: self.show_supplier_contact(supplier_data[5]))

        menu.addAction(supplier_contact_action)
        menu.exec_(self.supplier_table.viewport().mapToGlobal(position))

    def show_supplier_contact(self, supplier_name):
        """Open the Supplier Contact dialog."""
        dialog = SupplierContactDialog(supplier_name, self)
        dialog.exec_()

    def show_supplier_analytics(self):
        """Open the Supplier Analytics window."""
        analytics_window = SupplierAnalyticsWindow(self.supplier_data, self)
        analytics_window.exec_()

    def load_data(self):
        """Load dummy supplier data for testing."""
        self.supplier_data = self.db_manager.fetch_query("fetch_merchant_tracking")
        '''[
            ("M001", "2024-01-10", "Sugar", 1000, "Usine A", "Supplier A"),
            ("M002", "2024-02-15", "Flour", 2000, "Usine B", "Supplier B"),
            ("M003", "2024-03-20", "Oil", 1500, "Usine A", "Supplier A"),
            ("M004", "2024-04-25", "Salt", 500, "Usine C", "Supplier C"),
            ("M005", "2024-05-30", "Honey", 800, "Usine B", "Supplier D"),
        ]'''
        self.filtered_supplier_data = self.supplier_data[:]
        self.total_pages = (len(self.supplier_data) + self.page_size - 1) // self.page_size

        # Determine the oldest and earliest delivery dates
        oldest_date = min(row[1] for row in self.supplier_data)
        earliest_date = max(row[1] for row in self.supplier_data)

        # Set date pickers to the oldest date minus one day
        self.start_date_picker.setDate(QDate.fromString(oldest_date, "yyyy-MM-dd").addDays(-1))
        # Set date pickers to the most recent date plus one day
        self.end_date_picker.setDate(QDate.fromString(earliest_date, "yyyy-MM-dd").addDays(1))

    def update_supplier_table(self):
        """Update the supplier table for the current page."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        page_data = self.filtered_supplier_data[start:end]

        self.supplier_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                
                # Highlight critical deliveries
                if col_index == 1:  # Delivery Date column
                    delivery_date = QDate.fromString(row_data[1], "yyyy-MM-dd")
                    if delivery_date <= QDate.currentDate().addDays(7) and delivery_date >= QDate.currentDate():
                        item.setBackground(QColor("#ffc4c4"))  # Light red

                self.supplier_table.setItem(row_index, col_index, item)

        # Update pagination controls
        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def check_upcoming_deliveries(self):
        """Check for deliveries within the next 7 days and show a notification."""
        upcoming_deliveries = [
            row for row in self.filtered_supplier_data
            if QDate.fromString(row[1], "yyyy-MM-dd") <= QDate.currentDate().addDays(7) and QDate.fromString(row[1], "yyyy-MM-dd") >= QDate.currentDate()
        ]

        if upcoming_deliveries:
            QMessageBox.information(
                self, "Upcoming Deliveries",
                f"There are {len(upcoming_deliveries)} deliveries scheduled within the next 7 days."
            )

    def filter_supplier_data(self):
        """Filter supplier data based on date range, supplier name, and ingredient."""
        start_date = self.start_date_picker.date().toString("yyyy-MM-dd")
        end_date = self.end_date_picker.date().toString("yyyy-MM-dd")
        supplier = self.supplier_field.text().lower()
        ingredient = self.ingredient_field.text().lower()

        self.filtered_supplier_data = [
            row for row in self.supplier_data
            if start_date <= row[1] <= end_date  # Date Range Filter
            and (not supplier or supplier in row[5].lower())  # Supplier Filter
            and (not ingredient or ingredient in row[2].lower())  # Ingredient Filter
        ]

        self.total_pages = (len(self.filtered_supplier_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_supplier_table()
        self.check_upcoming_deliveries()

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_supplier_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_supplier_table()

    def export_data(self):
        """Export filtered supplier data to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Supplier Data", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Merchandise ID", "Delivery Date", "Ingredient",
                    "Quantity", "Factory Location", "Supplier Name"
                ])
                writer.writerows(self.filtered_supplier_data)
            QMessageBox.information(self, "Export Successful", f"Data exported to {file_path}")
