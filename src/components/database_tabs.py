from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
    QTableWidgetItem,
    QMenu,
    QAction,
    QMessageBox,
    QTableWidget,
    QPushButton,
)
from dialogs.database_dialog import DatabaseDialog
from utils.table import CustomTable
from database.databaseManager import SQLiteManager


class DatabaseTabs(QWidget):
    def __init__(self, db_manager: SQLiteManager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        """Initializes the UI for the DatabaseTabs component."""
        self.tab_widget = QTabWidget()

        # Add tabs for each table in the database
        tables = [
            "Composition_produit",
            "Details_Couts",
            "Distributions",
            "Fournisseurs_Distributeurs",
            "Historique_Process",
            "Ingredients",
            "Lots",
            "Marchandises",
            "Process",
            "Process_Types",
            "Product_info",
            "Stock",
            "Usines_Entrepots",
        ]

        for table in tables:
            self._add_table_tab(self.tab_widget, table)

        # Add button for adding a new row
        self.add_button = QPushButton("Add New Row")
        self.add_button.clicked.connect(
            lambda: self._open_dialog(
                self.tab_widget.currentWidget().table_name,
                self.tab_widget.currentWidget(),
                is_edit_mode=False,
            )
        )

        # Main layout for DatabaseTabs
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.add_button)
        self.setLayout(main_layout)

    def _add_table_tab(self, tab_widget: QTabWidget, title: str):
        """Adds a tab to the tab widget for the given table.

        Args:
            tab_widget (QTabWidget): The tab widget to add the table to.
            title (str): The title of the table to add.
        """
        # Retrieve rows and columns for the given table
        rows = self.db_manager.get_table_as_list(title)
        columns = self.db_manager.get_table_columns(title)

        # Create a custom table with the number of rows and columns
        table = CustomTable(len(rows), len(columns))

        # Set the horizontal header labels to readable column names
        table.setHorizontalHeaderLabels(
            [self._get_readable_column_name(col["name"]) for col in columns]
        )

        # Store the table name in the table widget
        table.table_name = title

        # Populate the table with data
        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

        # Set context menu policy and connect the custom context menu request to the handler
        table.setContextMenuPolicy(Qt.CustomContextMenu)
        table.customContextMenuRequested.connect(
            lambda pos: self._open_menu(pos, table)
        )

        # Add the table as a new tab in the tab widget with a readable title
        tab_widget.addTab(table, self._get_readable_table_name(title))

    def _delete_row(self, row_id: int):
        """Deletes the selected row from the table."""
        selected_row = row_id
        if selected_row >= 0:
            reply = QMessageBox.question(
                self,
                "Delete Row",
                "Are you sure you want to delete this row?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                pass
                # self.removeRow(selected_row)
                # self._delete_row_from_db(selected_row)

    def _delete_row_from_db(self, table_name: str, row_id: int):
        """Deletes a row from the database.

        Args:
            table_name (str): The name of the table.
            row_id (int): The ID of the row to delete.
        """
        self.db_manager.execute_query(
            f"DELETE FROM {table_name} WHERE id = ?", (row_id,)
        )
        self.db_manager.commit()

    def _open_menu(self, position: int, table: QTableWidget):
        """Opens a context menu at the given position.

        Args:
            position (int): The position to open the context menu at.
        """
        selected_row = table.currentRow()
        if selected_row == -1:
            return

        menu = QMenu()

        edit_action = QAction("Edit Row", self)
        edit_action.triggered.connect(
            lambda: self._open_dialog(table.table_name, table, selected_row)
        )
        menu.addAction(edit_action)

        delete_action = QAction("Delete Row", self)
        delete_action.triggered.connect(lambda: self._delete_row(selected_row))
        menu.addAction(delete_action)
        menu.exec_(table.viewport().mapToGlobal(position))

    def _open_dialog(
        self,
        table_name: str,
        table: QTableWidget,
        row_idx: int = None,
        is_edit_mode: bool = True,
    ):
        """Opens a dialog to add or edit a row in the table.

        Args:
            table_name (str): The name of the table.
            table (QTableWidget): The table to add or edit the row in.
            row_idx (int): The index of the row to edit.
        """

        columns = self.db_manager.get_table_columns(table_name)
        row_data = None
        if row_idx is not None:
            row_data = {
                columns[col_idx]["name"]: table.item(row_idx, col_idx).text()
                for col_idx in range(len(columns))
            }
        dialog = DatabaseDialog(
            self.db_manager, table_name, columns, row_data, self, is_edit_mode
        )
        if dialog.exec_():
            self._refresh_table(table, table_name)

    def _get_readable_table_name(self, table_name: str) -> str:
        """Converts a table name to a more readable format.

        Args:
            table_name (str): The table name to convert.

        Returns:
            str: The converted table name.
        """

        readable_names = {
            "Composition_produit": "Product Composition",
            "Details_Couts": "Cost Details",
            "Distributions": "Distributions",
            "Fournisseurs_Distributeurs": "Suppliers and Distributors",
            "Historique_Process": "Process History",
            "Ingredients": "Ingredients",
            "Lots": "Batches",
            "Marchandises": "Goods",
            "Process": "Process",
            "Process_Types": "Process Types",
            "Product_info": "Product Information",
            "Stock": "Stock",
            "Usines_Entrepots": "Factories and Warehouses",
        }
        return readable_names.get(table_name, table_name)

    def _get_readable_column_name(self, column_name: str) -> str:
        """Converts a column name to a more readable format.

        Args:
            column_name (str): The column name to convert.

        Returns:
            str: The converted column name.
        """

        readable_names = {
            "id": "ID",
            "nom": "Name",
            "date": "Date",
            "quantite": "Quantity",
            "quantite_kg": "Quantity (kg)",
            "prix": "Price",
            "localisation": "Location",
            "id_produit": "Product ID",
            "id_marchandise": "Merchandise ID",
            "id_ingredient": "Ingredient ID",
            "id_usine": "Factory ID",
            "id_entrepot": "Warehouse ID",
            "id_process": "Process ID",
            "id_process_type": "Process Type ID",
            "id_lot": "Batch ID",
            "id_fournisseur": "Supplier ID",
            "id_distributeur": "Distributor ID",
            "id_usine_livraison": "Delivery Warehouse ID",
            "id_contenant": "Container ID",
            "cout_prod": "Production Cost",
            "cout_matieres_premieres": "Raw Material Cost",
            "prix_de_vente": "Selling Price",
            "cout_marketing": "Marketing Cost",
            "date_arrivee": "Arrival Date",
            "date_contractualisation": "Contract Date",
            "date_mise_en_prod": "Production Date",
            "date_de_prod": "Production Date",
            "date_de_peremption": "Expiration Date",
            "date_livraison": "Delivery Date",
            "statut": "Status",
            "retour": "Return",
            "description_etiquettes": "Description",
            "photo_etiquettes": "Picture",
        }

        return (
            readable_names.get(column_name, column_name)
            if column_name in readable_names
            else column_name.title()
        )

    def _refresh_table(self, table: QTableWidget, table_name: str):
        """Refreshes the data in the given table.

        Args:
            table (QTableWidget): The table to refresh.
            table_name (str): The name of the table to refresh.
        """
        rows = self.db_manager.get_table_as_list(table_name)
        table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

    def get_table_widget(self, table_name: str) -> QTableWidget:
        """Returns the table widget for the given table name.

        Args:
            table_name (str): The name of the table.

        Returns:
            QTableWidget: The table widget for the given table name.
        """
        for i in range(self.tab_widget.count()):
            table = self.tab_widget.widget(i)
            if table.table_name == table_name:
                return table
        return None
