import csv
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidgetItem, QLabel, QMenu, QAction,
    QPushButton, QComboBox, QFileDialog, QMessageBox, QDateEdit, QListWidget, QToolBox
)
from PyQt5.QtCore import Qt
from utils.table import CustomTable
from datetime import datetime, timedelta
from widgets.collapsible import CollapsibleSection


class DistributionTrackingTab(QWidget):
    def __init__(self,db_manager):
        super().__init__()
        self.page_size = 10  # Number of rows per page
        self.current_page = 1
        self.total_pages = 1
        self.distribution_data = []  # Full dataset
        self.filtered_distribution_data = []  # Filtered dataset
        self.days_until_delivery = 7
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Search and Grouping Bar
        control_layout = QHBoxLayout()

        # Search Field
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search by Distributor, Lot ID, or Product ID...")
        self.search_field.textChanged.connect(self.filter_distribution_data)
        control_layout.addWidget(self.search_field)

        # Grouping Dropdown
        self.grouping_dropdown = QComboBox()
        self.grouping_dropdown.setStyleSheet("""
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
        self.grouping_dropdown.addItems(["No Grouping", "Group by Distributor", "Group by Product ID"])
        self.grouping_dropdown.currentIndexChanged.connect(self.group_distribution_data)
        control_layout.addWidget(self.grouping_dropdown)

        # Export Button
        export_button = QPushButton("Export to CSV")
        export_button.clicked.connect(self.export_distribution_data)
        control_layout.addWidget(export_button)

        main_layout.addLayout(control_layout)

        # Add date range filters
        filter_by_date_label = QLabel("Filter by Date Range:")
        self.start_date_field = QDateEdit()
        self.start_date_field.setCalendarPopup(True)
        self.end_date_field = QDateEdit()
        self.end_date_field.setCalendarPopup(True)
        self.end_date_field.setDate(datetime.now().date())
        self.filter_button = QPushButton("Apply Filter")
        self.filter_button.clicked.connect(self.filter_by_date_and_warehouse)

        # Add warehouse filter
        self.warehouse_dropdown = QComboBox()
        self.warehouse_dropdown.setStyleSheet("""
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
        self.warehouse_dropdown.addItem("All Warehouses")
        self.warehouse_dropdown.addItems(["Warehouse A", "Warehouse B", "Warehouse C"])

        # Arrange the filter layout
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(filter_by_date_label)
        filter_layout.addWidget(self.start_date_field)
        filter_layout.addWidget(self.end_date_field)
        filter_layout.addWidget(self.warehouse_dropdown)
        filter_layout.addWidget(self.filter_button)
        main_layout.addLayout(filter_layout)


        # Distribution Table
        self.distribution_table = CustomTable(10, 8)  # Initial size: 10 rows, 8 columns
        self.distribution_table.setHorizontalHeaderLabels([
            "Delivery Date", "Contract Date", "Lot", "Lot Quantity",
            "Departure Warehouse", "Distributor", "Distributor Location", "Product ID"
        ])
        self.distribution_table.setSizePolicy(self.distribution_table.sizePolicy().Expanding,
                                              self.distribution_table.sizePolicy().Expanding)
        self.distribution_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.distribution_table.customContextMenuRequested.connect(self.show_context_menu)
        main_layout.addWidget(self.distribution_table)

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

        # Upcoming Deliveries List and Button
        self.upcoming_deliveries_list = QListWidget()
        self.refresh_upcoming_deliveries_button = QPushButton("Refresh")
        self.refresh_upcoming_deliveries_button.clicked.connect(self.show_upcoming_deliveries)

        # Create content widget for upcoming deliveries
        upcoming_content_widget = QWidget()
        upcoming_content_layout = QVBoxLayout()
        upcoming_content_layout.addWidget(self.upcoming_deliveries_list)
        upcoming_content_layout.addWidget(self.refresh_upcoming_deliveries_button)
        upcoming_content_widget.setLayout(upcoming_content_layout)

        # Add collapsible section for upcoming deliveries
        upcoming_section = CollapsibleSection("Upcoming Deliveries", upcoming_content_widget)
        
        # Connect the toggled signal to refresh the deliveries when expanded
        upcoming_section.toggled.connect(lambda expanded: self.show_upcoming_deliveries() if expanded else None)
        
        # Add the section to the main layout
        main_layout.addWidget(upcoming_section)

        self.setLayout(main_layout)

        self.distribution_data = self.db_manager.fetch_query('fetch_distribution_tracking')

        '''[
            ("2023-01-15", "2023-01-10", "L001", 100, "Warehouse A", "Distributor A", "Location A", "P001"),
            ("2023-02-20", "2023-02-15", "L002", 50, "Warehouse B", "Distributor B", "Location B", "P002"),
            ("2023-03-25", "2023-03-20", "L003", 75, "Warehouse A", "Distributor A", "Location C", "P001"),
            ("2023-04-10", "2023-04-05", "L004", 120, "Warehouse C", "Distributor C", "Location D", "P003"),
            ("2023-05-30", "2023-05-25", "L005", 60, "Warehouse B", "Distributor B", "Location B", "P002"),
            ("2024-12-15", "2024-05-30", "L006", 80, "Warehouse C", "Distributor C", "Location D", "P004"),
        ]'''
        self.filtered_distribution_data = self.distribution_data[:]  # Start with unfiltered data
        self.total_pages = (len(self.distribution_data) + self.page_size - 1) // self.page_size
        self.update_distribution_table()

    def filter_by_date_and_warehouse(self):
        """Filter distributions by date range and warehouse."""
        start_date = self.start_date_field.date().toPyDate()
        end_date = self.end_date_field.date().toPyDate()
        selected_warehouse = self.warehouse_dropdown.currentText()

        self.filtered_distribution_data = [
            row for row in self.distribution_data
            if start_date <= datetime.strptime(row[0], "%Y-%m-%d").date() <= end_date
            and (selected_warehouse == "All Warehouses" or row[4] == selected_warehouse)
        ]
        self.total_pages = (len(self.filtered_distribution_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_distribution_table()

    def filter_distribution_data(self):
        """Filter distribution data based on the search input."""
        filter_text = self.search_field.text().lower()
        self.filtered_distribution_data = [
            row for row in self.distribution_data
            if any(filter_text in str(cell).lower() for cell in row)
        ]
        self.total_pages = (len(self.filtered_distribution_data) + self.page_size - 1) // self.page_size
        self.current_page = 1
        self.update_distribution_table()

    def group_distribution_data(self):
        """Group distribution data based on the selected option."""
        group_by = self.grouping_dropdown.currentText()
        key_index = None

        if group_by == "Group by Distributor":
            key_index = 5  # Distributor column
        elif group_by == "Group by Product ID":
            key_index = 7  # Product ID column
        else:
            key_index = 0 # Delivery Date

        if key_index is not None:
            self.filtered_distribution_data.sort(key=lambda x: x[key_index])

        self.update_distribution_table()

    def update_distribution_table(self):
        """Update the table to show the current page's data."""
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        page_data = self.filtered_distribution_data[start_index:end_index]

        self.distribution_table.setRowCount(len(page_data))
        for row_index, row_data in enumerate(page_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.distribution_table.setItem(row_index, col_index, item)

        self.page_label.setText(f"Page {self.current_page} of {self.total_pages}")
        self.previous_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def go_to_previous_page(self):
        """Navigate to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
            self.update_distribution_table()

    def go_to_next_page(self):
        """Navigate to the next page."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_distribution_table()

    def export_distribution_data(self):
        """Export distribution data to a CSV file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export to CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        # Write data to CSV
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Delivery Date", "Contract Date", "Lot", "Lot Quantity",
                "Departure Warehouse", "Distributor", "Distributor Location", "Product ID"
            ])
            writer.writerows(self.filtered_distribution_data)

    def show_context_menu(self, position):
        """Display context menu for distribution actions."""
        menu = QMenu(self)

        view_details_action = QAction("View Distribution Details", self)
        view_details_action.triggered.connect(self.show_distribution_details)
        menu.addAction(view_details_action)

        menu.exec_(self.distribution_table.viewport().mapToGlobal(position))

    def show_distribution_details(self):
        """Display details of a selected distribution in a popup."""
        selected_row = self.distribution_table.currentRow()
        if selected_row == -1:
            return
        global_row_index = (self.current_page - 1) * self.page_size + selected_row
        distribution = self.filtered_distribution_data[global_row_index]

        details_text = f"""
        Delivery Date: {distribution[0]}
        Contract Date: {distribution[1]}
        Lot: {distribution[2]}
        Lot Quantity: {distribution[3]}
        Departure Warehouse: {distribution[4]}
        Distributor: {distribution[5]}
        Distributor Location: {distribution[6]}
        Product ID: {distribution[7]}
        """
        QMessageBox.information(self, "Distribution Details", details_text)
        
    def show_upcoming_deliveries(self):
        """Display a list of deliveries scheduled within the next X days."""
        today = datetime.today().date()

        upcoming = [
            row for row in self.distribution_data
            if today <= datetime.strptime(row[0], "%Y-%m-%d").date() <= today + timedelta(days=self.days_until_delivery)
        ]

        # Clear the list widget and add upcoming deliveries
        self.upcoming_deliveries_list.clear()
        for row in upcoming:
            self.upcoming_deliveries_list.addItem(f"Lot {row[2]}: {row[0]} ({row[5]})")
            
        # print(self.upcoming_deliveries_list.item(0)[5])
