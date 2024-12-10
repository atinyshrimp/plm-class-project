from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidgetItem, QFileDialog, QPushButton, QComboBox, QLabel
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from utils.table import CustomTable
import csv

class BatchHistoryTab(QWidget):
    def __init__(self):
        super().__init__()
        self.page_size = 5  # Number of rows per page
        self.current_page = 1
        self.total_pages = 1
        self.batch_data = []  # Full dataset
        self.filtered_batch_data = []  # Filtered dataset
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Search and Grouping Bar
        control_layout = QHBoxLayout()

        # Search Field
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search by Lot ID, Product ID, or Status...")
        self.search_field.textChanged.connect(self.filter_batch_history)
        control_layout.addWidget(self.search_field)

        # Grouping Dropdown
        self.grouping_dropdown = QComboBox()
        self.grouping_dropdown.addItems(["No Grouping", "Group by Product ID", "Group by Status"])
        self.grouping_dropdown.currentIndexChanged.connect(self.group_batch_history)
        control_layout.addWidget(self.grouping_dropdown)

        # Export Button
        export_button = QPushButton("Export to CSV")
        export_button.clicked.connect(self.export_batch_history)
        control_layout.addWidget(export_button)

        main_layout.addLayout(control_layout)

        # Batch Table
        self.batch_table = CustomTable(10, 7)  # Initial size: 10 rows, 7 columns
        self.batch_table.setHorizontalHeaderLabels([
            "Lot ID", "Product ID", "Quantity", "Production Date",
            "Expiry Date", "Status", "Return"
        ])
        self.batch_table.setSizePolicy(self.batch_table.sizePolicy().Expanding, self.batch_table.sizePolicy().Expanding)
        main_layout.addWidget(self.batch_table)

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

        # Dummy Data
        self.batch_data = [
            ("L001", "P001", 100, "2023-01-15", "2023-06-15", "Active", "None"),
            ("L002", "P002", 50, "2023-02-20", "2023-07-20", "Shipped", "None"),
            ("L003", "P001", 75, "2023-03-10", "2023-08-10", "Active", "Returned"),
            ("L004", "P003", 120, "2023-04-25", "2023-09-25", "Inactive", "None"),
            ("L005", "P002", 30, "2023-05-05", "2023-10-05", "Shipped", "None"),
            ("L006", "P001", 60, "2023-06-10", "2023-11-10", "Expired", "Returned"),
        ]
        self.filtered_batch_data = self.batch_data[:]  # Start with unfiltered data
        self.total_pages = (len(self.batch_data) + self.page_size - 1) // self.page_size
        self.update_batch_table()

    def filter_batch_history(self):
        """Filter batch history based on the search input."""
        filter_text = self.search_field.text().lower()

        # Apply filter
        self.filtered_batch_data = [
            row for row in self.batch_data
            if any(filter_text in str(cell).lower() for cell in row)
        ]

        # Update the table
        self.update_batch_table()

    def group_batch_history(self):
        """Group batch history based on the selected option."""
        group_by = self.grouping_dropdown.currentText()
        key_index = None

        if group_by == "Group by Product ID":
            key_index = 1  # Product ID column
        elif group_by == "Group by Status":
            key_index = 5  # Status column

        if key_index is not None:
            self.filtered_batch_data.sort(key=lambda x: x[key_index])

        self.update_batch_table()

    def update_batch_table(self):
        """Update the batch history table with filtered data."""
        self.batch_table.setRowCount(len(self.filtered_batch_data))

        for row_index, row_data in enumerate(self.filtered_batch_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                # Apply color-coding for Status
                if col_index == 5:  # Status column
                    item.setBackground(self.get_status_color(row_data[5]))
                self.batch_table.setItem(row_index, col_index, item)

        # self.batch_table.resizeColumnsToContents()

    def get_status_color(self, status):
        """Return a color based on the batch status."""
        colors = {
            "Active": QColor("#b3ffcc"),  # Green
            "Shipped": QColor("#cce0ff"),  # Blue
            "Inactive": QColor("#ffe6cc"),  # Orange
            "Expired": QColor("#ffcccc"),  # Red
            "Returned": QColor("#ffff99"),  # Yellow
        }
        return colors.get(status, QColor("#ffffff"))  # Default: White

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_batch_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_batch_table()

    def export_batch_history(self):
        """Export batch history to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export to CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        # Write data to CSV
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Lot ID", "Product ID", "Quantity", "Production Date",
                             "Expiry Date", "Status", "Return"])  # Header
            writer.writerows(self.filtered_batch_data)  # Rows
