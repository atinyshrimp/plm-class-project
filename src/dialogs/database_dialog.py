"""Module to create a dialog for adding or editing rows in a database table. 
This module demonstrates how to create a dialog with input fields based on the column types of a database table.
The dialog allows users to add or edit rows in a database table by providing input fields for each column.
The input fields are dynamically created based on the column types of the table, allowing for a flexible and user-friendly interface.
The dialog also handles saving the data to the database and displaying error messages if the data cannot be saved.
"""

import re
from typing import Callable

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import (
    QComboBox,
    QDateTimeEdit,
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from database.database_manager import SQLiteManager


class DatabaseDialog(QDialog):
    """Dialog for adding or editing rows in a database table."""

    def __init__(
        self,
        db_manager,
        table_name,
        columns,
        row_data=None,
        parent=None,
        is_edit_mode=True,
    ):
        super().__init__(parent)
        self.db_manager = db_manager
        self.table_name = table_name
        self.columns = columns
        self.row_data = row_data
        self.foreign_keys = self.db_manager.get_foreign_keys(table_name)
        self.is_edit_mode = is_edit_mode
        self.init_ui()

    def init_ui(self):
        """Initializes the UI for the DatabaseDialog."""
        # Set the window title
        self.setWindowTitle(f"{'Edit' if self.is_edit_mode else 'Add'} Row")
        self.setFixedWidth(400)

        # Create the main layout
        layout = QVBoxLayout()

        # Create the form layout
        self.form_layout = QFormLayout()
        self.inputs = {}

        # Iterate over the columns to create input fields
        for column in self.columns[1:]:
            column_name = column["name"]
            column_type = column["type"]
            input_field = self._create_input_field(column_name, column_type)

            # If row_data is provided and in edit mode, populate the input fields with existing data
            if self.is_edit_mode and self.row_data:
                value = self.row_data.get(column_name, "")
                if isinstance(input_field, QSpinBox):
                    input_field.setValue(
                        int(str(value).replace(".", "") if value else 0)
                    )
                elif isinstance(input_field, QDoubleSpinBox):
                    input_field.setValue(float(value if value else 0))
                elif isinstance(input_field, QDateTimeEdit):
                    input_field.setDateTime(
                        QDateTime.fromString(value, "yyyy-MM-dd")
                        if value
                        else QDateTime.currentDateTime()
                    )
                elif isinstance(input_field, QComboBox):
                    index = (
                        input_field.findText(str(value))
                        if column_name not in ["type", "statut", "retour"]
                        else int(value)
                    )
                    print(str(value))
                    print(index)
                    if index != -1:
                        input_field.setCurrentIndex(index)
                else:
                    input_field.setText(str(value))

            # Store the input field in the inputs dictionary
            self.inputs[column_name] = input_field

            # Add the input field to the form layout
            self.form_layout.addRow(column_name, input_field)

        # Add the form layout to the main layout
        layout.addLayout(self.form_layout)

        # Create and connect the save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        # Set the main layout for the dialog
        self.setLayout(layout)

    def _create_input_field(self, column_name: str, column_type: str) -> QWidget:
        """Creates an input field based on the column type.

        Args:
            column_name (str): The name of the column.
            column_type (str): The type of the column.

            Returns:
                QWidget: The input field widget.
        """

        # Check if the column is a foreign key
        if column_type == "INTEGER" and self._is_foreign_key(column_name):
            input_field = QComboBox()
            ref_table = self.get_reference_table(column_name)
            ref_table = "Usines_Entrepots" if "/" in ref_table else ref_table
            ref_data = self.db_manager.get_table_as_list(ref_table)
            for row in ref_data:
                input_field.addItem(f"{str(row[0])}")

        # Check if the column type is INTEGER or BOOLEAN
        elif column_type == "INTEGER" and column_name != "cout_marketing":
            input_field = QSpinBox()
            input_field.setMaximum(999999999)  # Set maximum value for the spin box

        # Check if the column type is REAL and the column name contains "date"
        elif column_type == "REAL" and "date" in column_name.lower():
            input_field = QDateTimeEdit()
            input_field.setCalendarPopup(
                True
            )  # Enable calendar popup for date selection
            input_field.setDisplayFormat(
                "yyyy-MM-dd"
            )  # Set display format for the date
            input_field.setDateTime(
                QDateTime.currentDateTime()
            )  # Set current date and time

        # Check if the column type is REAL
        elif column_type == "REAL" or column_name == "cout_marketing":
            input_field = QDoubleSpinBox()
            input_field.setMaximum(
                999999999.99
            )  # Set maximum value for the double spin box

        # Check if the column type is TEXT
        elif column_type == "TEXT":
            input_field = QLineEdit()

        elif column_type == "BOOLEAN":
            input_field = QComboBox()
            if column_name == "statut":
                input_field.addItems(["Inactive", "Active"])
            elif column_name == "type":
                input_field.addItems(
                    ["Distributor", "Supplier"]
                    if self.table_name == "Fournisseurs_Distributeurs"
                    else ["Factory", "Warehouse"]
                )
            elif column_name == "retour":
                input_field.addItems(["No", "Yes"])

        # Default case for other column types
        else:
            input_field = QLineEdit()

        return input_field

    def _is_foreign_key(self, column_name: str) -> bool:
        """Checks if the column is a foreign key.

        Args:
            column_name (str): The name of the column.

        Returns:
            bool: True if the column is a foreign key, False otherwise.
        """
        return any(fk["column"] == column_name for fk in self.foreign_keys)

    def get_reference_table(self, column_name: str) -> str:
        """Gets the reference table for a foreign key column.

        Args:
            column_name (str): The name of the foreign key column.

        Returns:
            str: The name of the reference table.
        """
        for fk in self.foreign_keys:
            if fk["column"] == column_name:
                return fk["ref_table"]
        return None

    def save_data(self):
        """Saves the data to the database."""
        data = {}
        for column in self.columns[1:]:
            column_name = column["name"]
            column_type = column["type"]
            if column_type == "REAL" and "date" in column_name.lower():
                data[column_name] = (
                    self.inputs[column_name].dateTime().toString("yyyy-MM-dd")
                )
            elif column_type == "REAL" or column_name == "cout_marketing":
                data[column_name] = self.inputs[column_name].value()
            elif isinstance(self.inputs[column_name], QComboBox):
                data[column_name] = (
                    self.inputs[column_name].currentText()
                    if column_type != "BOOLEAN"
                    else self.inputs[column_name].currentIndex()
                )
            else:
                data[column_name] = self.inputs[column_name].text()

        if self.row_data:
            # Update existing row
            set_clause = ", ".join([f"{col['name']} = ?" for col in self.columns[1:]])
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
            params = list(data.values()) + [self.row_data["id"]]
        else:
            # Insert new row
            columns_clause = ", ".join([col["name"] for col in self.columns[1:]])
            placeholders = ", ".join(["?" for _ in self.columns[1:]])
            query = f"INSERT INTO {self.table_name} ({columns_clause}) VALUES ({placeholders})"
            params = list(data.values())

        try:
            self.db_manager.execute_query(query, params)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


def open_dialog(
    db_manager: SQLiteManager,
    table_name: str,
    column_id,
    parent: QWidget,
    refresh_fn: Callable,
    is_edit_mode: bool = False,
):
    """Opens the DatabaseDialog to add or edit a row in the table."""
    columns = db_manager.get_table_columns(table_name)
    row_data = db_manager.execute_query(
        f"SELECT * FROM {table_name} WHERE id = ?",
        (get_integer_from_column_name(column_id),),
    )[0]
    row_data = dict(zip([col["name"] for col in columns], row_data))

    dialog = DatabaseDialog(
        db_manager, table_name, columns, row_data, parent, is_edit_mode
    )
    if dialog.exec_() == QDialog.Accepted:
        refresh_fn()


def get_integer_from_column_name(column_name):
    """Extract integer from column name formatted as 'P###'.

    Args:
        column_name (str): The column name in the format 'P###'.

    Returns:
        int: The extracted integer.
    """
    match = re.search(r"\d+", column_name)
    if match:
        return int(match.group(0))
    return None
