import csv

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAction,
    QComboBox,
    QDateEdit,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMenu,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QDialog,
)

from dialogs.stock_trends_window import StockTrendsWindow
from dialogs.database_dialog import open_dialog
from utils.table import CustomTable


class StockLocationTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.page_size = 20
        self.current_page = 1
        self.total_pages = 1
        self.db_manager = db_manager
        self.stock_data = []
        self.filtered_stock_data = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Interaction Buttons
        buttons_layout = QHBoxLayout()

        # Stock Trends Visualization
        trends_button = QPushButton("View Stock Trends")
        trends_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        trends_button.adjustSize()
        trends_button.clicked.connect(self.open_stock_trends_window)
        buttons_layout.addWidget(trends_button)

        # Export to CSV
        export_button = QPushButton("Export to CSV", self)
        export_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        export_button.adjustSize()
        export_button.clicked.connect(self.export_data)
        buttons_layout.addWidget(export_button)

        buttons_layout.setAlignment(Qt.AlignRight)
        main_layout.addLayout(buttons_layout)

        # Filter Controls
        filter_layout = QHBoxLayout()

        # Expiration Date Filter
        expiration_date_label = QLabel("Expiration Date After:")
        self.expiration_date_picker = QDateEdit()
        self.expiration_date_picker.setCalendarPopup(True)
        self.expiration_date_picker.setDate(QDate.currentDate())

        # Arrival Date Filter
        arrival_date_label = QLabel("Arrival Date After:")
        self.arrival_date_picker = QDateEdit()
        self.arrival_date_picker.setCalendarPopup(True)
        self.arrival_date_picker.setDate(QDate.currentDate())

        # Location Filter
        location_label = QLabel("Location:")
        self.location_dropdown = QComboBox()
        self.location_dropdown.setStyleSheet(
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
        self.location_dropdown.addItem("All")
        self.__populate_locations()

        # Button to apply filters
        self.filter_button = QPushButton("Apply Filter")
        self.filter_button.clicked.connect(self.filter_stock_data)

        # Add filters to layout
        filter_layout.addWidget(expiration_date_label)
        filter_layout.addWidget(self.expiration_date_picker)
        filter_layout.addWidget(arrival_date_label)
        filter_layout.addWidget(self.arrival_date_picker)
        filter_layout.addWidget(location_label)
        filter_layout.addWidget(self.location_dropdown)
        filter_layout.addWidget(self.filter_button)
        main_layout.addLayout(filter_layout)

        # Table for Stock Details
        self.stock_table = CustomTable()
        self.stock_table.setColumnCount(7)
        self.stock_table.setHorizontalHeaderLabels(
            [
                "Lot ID",
                "Product ID",
                "Quantity",
                "Expiration Date",
                "Arrival Date",
                "Warehouse",
                "Location",
            ]
        )

        if self.db_manager.is_admin:
            # Enable context menu on the table
            self.stock_table.setContextMenuPolicy(Qt.CustomContextMenu)
            self.stock_table.customContextMenuRequested.connect(self.show_context_menu)

        main_layout.addWidget(self.stock_table)

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
        self.update_stock_table()

    def load_data(self):
        """Load dummy stock data for testing."""
        self.stock_data = self.db_manager.fetch_query("fetch_stock_and_location")
        """[
            ("L001", "P001", 50, "2024-06-01", "2024-01-15", "Warehouse A", "Paris"),
            ("L002", "P002", 80, "2024-03-01", "2024-02-10", "Warehouse B", "Lyon"),
            ("L003", "P003", 100, "2023-12-15", "2023-11-20", "Warehouse C", "Marseille"),
            ("L004", "P004", 75, "2024-05-01", "2024-02-01", "Warehouse D", "Paris"),
            ("L005", "P005", 60, "2023-12-30", "2023-12-10", "Warehouse E", "Lyon"),
        ]"""
        self.filtered_stock_data = self.stock_data[:]
        self.total_pages = (len(self.stock_data) + self.page_size - 1) // self.page_size

        # Determine the oldest expiration and arrival dates
        oldest_expiration_date = min(row[3] for row in self.stock_data)
        oldest_arrival_date = min(row[4] for row in self.stock_data)

        # Set date pickers to the oldest dates minus one day
        self.expiration_date_picker.setDate(
            QDate.fromString(oldest_expiration_date, "yyyy-MM-dd").addDays(-1)
        )
        self.arrival_date_picker.setDate(
            QDate.fromString(oldest_arrival_date, "yyyy-MM-dd").addDays(-1)
        )

    def __populate_locations(self):
        """Populate the location dropdown with locations from the database."""
        locations = self.db_manager.fetch_query("fetch_locations")
        print(locations)
        for location in locations:
            self.location_dropdown.addItem(location[0])

    def update_stock_table(self):
        """Update the stock table for the current page."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        page_data = self.filtered_stock_data[start:end]

        self.stock_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))

                # Highlight low quantity
                if col_index == 2 and row_data[2] <= 50:  # Threshold: Quantity < 50
                    item.setBackground(QColor("#fff4cc"))  # Light yellow

                # Highlight expiring soon
                if col_index == 3:
                    expiration_date = QDate.fromString(row_data[3], "yyyy-MM-dd")
                    if (
                        expiration_date <= QDate.currentDate().addDays(30)
                        and expiration_date > QDate.currentDate()
                    ):  # Expiring in 30 days
                        item.setBackground(QColor("#ffc4c4"))  # Light red

                self.stock_table.setItem(row_index, col_index, item)

        # Update pagination controls
        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def filter_stock_data(self):
        """Filter stock data based on expiration date, arrival date, and location."""
        expiration_date = self.expiration_date_picker.date().toString("yyyy-MM-dd")
        arrival_date = self.arrival_date_picker.date().toString("yyyy-MM-dd")
        location = self.location_dropdown.currentText()

        self.filtered_stock_data = [
            row
            for row in self.stock_data
            if row[3] > expiration_date  # Expiration Date Filter
            and row[4] > arrival_date  # Arrival Date Filter
            and (location == "All" or location in row[6])  # Location Filter
        ]

        self.total_pages = (
            len(self.filtered_stock_data) + self.page_size - 1
        ) // self.page_size
        self.current_page = 1
        self.update_stock_table()

    def show_context_menu(self, position: int):
        """Show a context menu with actions for the selected product.

        Args:
            position (int): The position of the context menu.
        """
        selected_row = self.stock_table.currentRow()
        if selected_row == -1:
            return

        batch_id = self.stock_table.item(selected_row, 0).text()
        warehouse_id = self.stock_table.item(selected_row, 5).text()

        menu = QMenu(self)

        edit_batch_action = QAction(f"Edit Batch ({batch_id})", self)
        edit_batch_action.triggered.connect(
            lambda: self.open_database_dialog("Lots", batch_id)
        )
        menu.addAction(edit_batch_action)

        edit_warehouse_action = QAction(f"Edit Warehouse ({warehouse_id})", self)
        edit_warehouse_action.triggered.connect(
            lambda: self.open_database_dialog("Usines_Entrepots", warehouse_id)
        )
        menu.addAction(edit_warehouse_action)

        menu.exec_(self.stock_table.viewport().mapToGlobal(position))

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_stock_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_stock_table()

    def export_data(self):
        """Export filtered stock data to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Stock Data", "", "CSV Files (*.csv)"
        )
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "Lot ID",
                        "Product ID",
                        "Quantity",
                        "Expiration Date",
                        "Arrival Date",
                        "Warehouse",
                        "Location",
                    ]
                )
                writer.writerows(self.filtered_stock_data)
            QMessageBox.information(
                self, "Export Successful", f"Data exported to {file_path}"
            )

    def open_stock_trends_window(self):
        """Open the Stock Trends Window."""
        data = [(row[6], row[2], row[4]) for row in self.filtered_stock_data]
        trends_window = StockTrendsWindow(data, self)
        trends_window.exec_()  # Open the dialog as a modal window

    def open_database_dialog(self, table_name: str, column_id: str):
        """Open the Database Dialog."""
        open_dialog(
            self.db_manager, table_name, column_id, self, self.refresh_data, True
        )

    def refresh_data(self):
        """Refresh the stock data and update the table."""
        self.load_data()
        self.update_stock_table()
