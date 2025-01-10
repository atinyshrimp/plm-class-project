import csv

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAction,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QMessageBox,
    QPushButton,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from dialogs.database_dialog import open_dialog
from utils.table import CustomTable


class BatchHistoryTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
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
        self.search_field.setPlaceholderText(
            "Search by Lot ID, Product ID, or Status..."
        )
        self.search_field.textChanged.connect(self.filter_batch_history)
        control_layout.addWidget(self.search_field)

        # Grouping Dropdown
        self.grouping_dropdown = QComboBox()
        self.grouping_dropdown.setStyleSheet(
            """
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
        """
        )

        self.grouping_dropdown.addItems(
            ["No Grouping", "Group by Product ID", "Group by Status"]
        )
        self.grouping_dropdown.currentIndexChanged.connect(self.group_batch_history)
        control_layout.addWidget(self.grouping_dropdown)

        # Export Button
        export_button = QPushButton("Export to CSV")
        export_button.clicked.connect(self.export_batch_history)
        control_layout.addWidget(export_button)

        main_layout.addLayout(control_layout)

        # Batch Table
        self.batch_table = CustomTable(10, 7)  # Initial size: 10 rows, 7 columns
        self.batch_table.setHorizontalHeaderLabels(
            [
                "Lot ID",
                "Product ID",
                "Quantity",
                "Production Date",
                "Expiry Date",
                "Status",
                "Return",
            ]
        )
        self.batch_table.setSizePolicy(
            self.batch_table.sizePolicy().Expanding,
            self.batch_table.sizePolicy().Expanding,
        )
        self.batch_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.batch_table.customContextMenuRequested.connect(self.show_context_menu)
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

        self.load_data()
        self.setLayout(main_layout)

    def load_data(self):
        self.batch_data = self.db_manager.fetch_query("fetch_lot_history")
        self.filtered_batch_data = self.batch_data[:]  # Start with unfiltered data
        self.total_pages = (len(self.batch_data) + self.page_size - 1) // self.page_size
        self.update_batch_table()

    def filter_batch_history(self):
        """Filter batch history based on the search input."""
        filter_text = self.search_field.text().lower()

        # Apply filter
        self.filtered_batch_data = [
            row
            for row in self.batch_data
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

    def show_context_menu(self, position):
        """Display context menu for batch actions."""
        selected_row = self.batch_table.currentRow()
        if selected_row == -1:
            return

        batch_data = self.filtered_batch_data[selected_row]

        menu = QMenu(self)

        report_action = QAction("View Report", self)
        report_action.triggered.connect(self.show_batch_report)
        menu.addAction(report_action)

        mark_inactive_action = QAction("Mark as Inactive", self)
        mark_inactive_action.triggered.connect(self.mark_batch_as_inactive)
        menu.addAction(mark_inactive_action)

        mark_shipped_action = QAction("Mark as Shipped", self)
        mark_shipped_action.triggered.connect(self.mark_batch_as_shipped)
        menu.addAction(mark_shipped_action)

        if self.db_manager.is_admin:
            menu.addSeparator()
            edit_batch_action = QAction(f"Edit Batch ({batch_data[0]})", self)
            edit_batch_action.triggered.connect(
                lambda: open_dialog(
                    self.db_manager, "Lots", batch_data[0], self, self.load_data, True
                )
            )
            menu.addAction(edit_batch_action)

        menu.exec_(self.batch_table.viewport().mapToGlobal(position))

    def show_batch_report(self):
        """Display detailed batch information in a popup."""
        selected_row = self.batch_table.currentRow()
        if selected_row == -1:
            return
        global_row_index = (self.current_page - 1) * self.page_size + selected_row
        batch = self.filtered_batch_data[global_row_index]

        report_text = f"""
        Lot ID: {batch[0]}
        Product ID: {batch[1]}
        Quantity: {batch[2]}
        Production Date: {batch[3]}
        Expiry Date: {batch[4]}
        Status: {batch[5]}
        Return: {batch[6]}
        """
        QMessageBox.information(self, "Batch Report", report_text)

    def mark_batch_as_inactive(self):
        """Mark the selected batch as inactive."""
        selected_row = self.batch_table.currentRow()
        if selected_row == -1:
            return
        global_row_index = (self.current_page - 1) * self.page_size + selected_row
        batch = self.filtered_batch_data[global_row_index]
        self.filtered_batch_data[global_row_index] = batch[:5] + ("Inactive", batch[6])
        self.update_batch_table()

    def mark_batch_as_shipped(self):
        """Mark the selected batch as shipped."""
        selected_row = self.batch_table.currentRow()
        if selected_row == -1:
            return
        global_row_index = (self.current_page - 1) * self.page_size + selected_row
        batch = self.filtered_batch_data[global_row_index]
        self.filtered_batch_data[global_row_index] = batch[:5] + ("Shipped", batch[6])
        self.update_batch_table()

    def export_batch_history(self):
        """Export batch history to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export to CSV", "", "CSV Files (*.csv)"
        )
        if not file_path:
            return

        # Write data to CSV
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Lot ID",
                    "Product ID",
                    "Quantity",
                    "Production Date",
                    "Expiry Date",
                    "Status",
                    "Return",
                ]
            )  # Header
            writer.writerows(self.filtered_batch_data)  # Rows

    def filter_by_product(self, product_id):
        """Filter batch history by the given product ID."""
        self.search_field.setText(product_id)  # Assuming there's a search field
