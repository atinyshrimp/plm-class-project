import sys
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QDesktopWidget,
    QDialog,
    QHBoxLayout,
    QMenuBar,
    QMessageBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

import globals
from components.data_tabs import DataTabs
from components.database_tabs import DatabaseTabs
from components.navbar import NavBar
from components.people_tabs import PeopleTabs
from components.process_tabs import ProcessTabs
from components.product_tabs import ProductTabs
from database.database_manager import SQLiteManager
from dialogs.login.login_window import LoginDialog
from utils.styling import apply_stylesheet


class PLMApp(QWidget):
    def __init__(self, version: str, db_manager: SQLiteManager):
        super().__init__()
        self.version = version  # Store the version
        self.db_manager = db_manager

        self.setWindowTitle(
            f"Hive (PLM Internal Software) v{self.version} — {globals.current_user}"
        )
        self.setWindowIcon(QtGui.QIcon("assets/img/mgo_sa_icon_resized.png"))

        # Apply the stylesheet
        apply_stylesheet(self, "assets/styles/palette_style.qss")

        self.init_ui()
        self.resize_window()

    def resize_window(self):
        """Resize the window based on the screen size to maintain the aspect ratio."""
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Set the window size to 70% of the screen width and 80% of the screen height
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.8)
        self.setFixedSize(window_width, window_height)

    def init_ui(self):
        main_layout = QVBoxLayout(self)  # Use QVBoxLayout to include the menu bar

        # Main content layout
        content_layout = QHBoxLayout()
        self.navbar = NavBar(self.db_manager)
        self.tab_widget_stack = QStackedWidget(self)

        # Initialize and add tab widgets
        self.product_tabs = ProductTabs(self.db_manager)
        self.people_tabs = PeopleTabs(self.db_manager)
        self.process_tabs = ProcessTabs(self.db_manager)
        self.data_tabs = DataTabs(self.db_manager)
        self.database_tabs = DatabaseTabs(self.db_manager)

        self.tab_widget_stack.addWidget(self.product_tabs)
        self.tab_widget_stack.addWidget(self.people_tabs)
        self.tab_widget_stack.addWidget(self.process_tabs)
        self.tab_widget_stack.addWidget(self.data_tabs)
        self.tab_widget_stack.addWidget(self.database_tabs)
        self.tab_widget_stack.setCurrentIndex(0)  # Default to the first tab set

        # Connect navbar clicks to change the displayed content
        self.navbar.currentRowChanged.connect(self.display_tabs)

        # Initialize the menu bar
        menubar = self.init_menu_bar()
        main_layout.setMenuBar(menubar)

        # Add navbar and tab widget stack to the layout
        content_layout.addWidget(self.navbar)
        content_layout.addWidget(self.tab_widget_stack)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def init_menu_bar(self):
        """Create and return the menu bar."""
        menubar = QMenuBar(self)

        # File Menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("Log Out", self.__log_out)
        file_menu.addAction("Exit", self.__close_application)

        if self.db_manager.is_admin:
            # Database Menu
            database_menu = menubar.addMenu("Database")
            view_database_action = QAction("View Database", self)
            view_database_action.triggered.connect(self.__go_to_database_tab)
            view_database_action.setShortcut("Ctrl+5")  # Shortcut key
            database_menu.addAction(view_database_action)

            add_row_menu = database_menu.addMenu("Add New Row")
            table_names = self.db_manager.get_all_tables()
            readable_table_names = [
                self.database_tabs._get_readable_table_name(table_name)
                for table_name in table_names
            ]
            tables = {
                readable_table_name: table_name
                for readable_table_name, table_name in zip(
                    readable_table_names, table_names
                )
            }

            print(tables)

            for table_name in sorted(readable_table_names):
                real_table_name = tables[table_name]
                add_row_menu.addAction(
                    table_name,
                    lambda table_name=real_table_name: self.database_tabs._open_dialog(
                        table_name,
                        self.database_tabs.get_table_widget(table_name),
                        is_edit_mode=False,
                    ),
                )

        # Navigation Menu
        navigation_menu = menubar.addMenu("Navigation")

        tab_names = ["Products", "People", "Process", "Data"]
        for index, tab_name in enumerate(tab_names):
            action = QAction(f"Go to {tab_name}", self)
            action.triggered.connect(lambda _, index=index: self.__go_to_tab(index))
            action.setShortcut(QKeySequence(f"Ctrl+{index + 1}"))  # Shortcut key
            navigation_menu.addAction(action)

        # View Menu
        view_menu = menubar.addMenu("View")
        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.refresh_tables)
        refresh_action.setShortcut("F5")  # Shortcut key
        view_menu.addAction(refresh_action)

        toggle_navbar_action = QAction("Show/Hide Navbar", self)
        toggle_navbar_action.triggered.connect(self.__toggle_navbar)
        toggle_navbar_action.setShortcut("Ctrl+H")  # Shortcut key
        view_menu.addAction(toggle_navbar_action)

        # Help Menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("User Guide", self.__show_user_guide)
        help_menu.addAction("Keyboard Shortcuts", self.__show_keyboard_shortcuts)
        help_menu.addSeparator()
        help_menu.addAction("About", self.__show_about)
        help_menu.addAction("Help", self.__show_help_documentation)
        help_menu.addSeparator()
        help_menu.addAction(
            "Visit GitHub Repository",
            lambda: webbrowser.open("https://github.com/atinyshrimp/plm-class-project"),
        )

        return menubar

    def display_tabs(self, index: int):
        """Update the content displayed based on the selected item in the navbar.

        Args:
            index (int): The index of the selected item in the navbar.
        """
        self.tab_widget_stack.setCurrentIndex(index)

    def switch_to_product_tab(self, product_id: str):
        """Switch to the Product Sheets tab and focus on the given product."""
        self.tab_widget_stack.setCurrentWidget(self.product_tabs)
        self.navbar.setCurrentRow(0)
        if hasattr(self.product_tabs, "focus_on_product_sheet"):
            self.product_tabs.tab_widget.setCurrentIndex(0)
            self.product_tabs.focus_on_product_sheet(product_id)

    def switch_to_cost_tab(self, product_id: str):
        """Switch to the Cost Details tab and focus on the given product."""
        self.tab_widget_stack.setCurrentWidget(self.product_tabs)
        self.navbar.setCurrentRow(0)
        if hasattr(self.product_tabs, "focus_on_product_sheet"):
            self.product_tabs.tab_widget.setCurrentIndex(1)
            self.product_tabs.cost_details_tab.search_field.setText(product_id)

    def switch_to_batch_tab(self, product_id: str):
        """Switch to the Batch History tab and focus on the given product."""
        self.tab_widget_stack.setCurrentWidget(self.data_tabs)
        self.navbar.setCurrentRow(3)
        if hasattr(self.data_tabs.batch_history_tab, "filter_by_product"):
            self.data_tabs.batch_history_tab.filter_by_product(product_id)

    def navigate_to_batch_history(self, lot_id: str):
        """Navigate to Batch History tab for the selected lot."""
        parent_widget = self.parentWidget()
        if hasattr(parent_widget, "switch_to_batch_tab"):
            parent_widget.switch_to_batch_tab(lot_id)

    # Menu actions
    def __log_out(self):
        reply = QMessageBox.question(
            self,
            "Log Out",
            "Are you sure you want to log out?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            globals.current_user = None
            self.close()

            # Display the login window
            login_dialog = LoginDialog(self.version)
            if login_dialog.exec_() == QDialog.Accepted:  # If login is successful
                # Initialize the database connection
                db_manager = SQLiteManager()

                # Create and launch a new instance of PLMApp
                self.__init__(self.version, db_manager)
                self.show()
            else:
                # Exit the application if login fails or the user closes the window
                sys.exit()

    def __close_application(self):
        self.close()

    def __go_to_database_tab(self):
        """Navigate to the Database tab."""
        self.navbar.setCurrentRow(4)
        self.tab_widget_stack.setCurrentIndex(4)

    def refresh_tables(self):
        for i in range(self.tab_widget_stack.count()):
            widget = self.tab_widget_stack.widget(i)
            if hasattr(widget, "refresh"):
                widget.refresh()

    def __toggle_navbar(self):
        self.navbar.setVisible(not self.navbar.isVisible())

    def __go_to_tab(self, index: int):
        """Navigate to the selected tab."""
        tab_widgets = [
            self.product_tabs,
            self.people_tabs,
            self.process_tabs,
            self.data_tabs,
        ]
        self.navbar.setCurrentRow(index)
        self.tab_widget_stack.setCurrentWidget(tab_widgets[index])

    def __show_user_guide(self):
        """Open detailed documentation for the application."""
        webbrowser.open(
            "https://github.com/atinyshrimp/plm-class-project/wiki/User-Guide"  # todo: update this link
        )

    def __show_keyboard_shortcuts(self):
        """Show a list of shortcuts for efficient usage."""
        shortcuts_message = f"""
        Keyboard Shortcuts:
        - Esc: Close Edit Mode
        - F5: Refresh Tables
        - Ctrl + H: Show/Hide Navbar
        - Ctrl + 1-{"5" if self.db_manager.is_admin else "4"}: Navigate to Products, People, Process, Data{", Database" if self.db_manager.is_admin else ""} tabs
        """
        QMessageBox.information(self, "Keyboard Shortcuts", shortcuts_message)

    def __show_about(self):
        about_message = f"PLM Tool v{self.version}\nDeveloped by MGO S.A. Group for managing product lifecycle."
        QMessageBox.about(self, "About", about_message)

    def __show_help_documentation(self):
        help_message = "For help, visit our documentation or contact support."
        QMessageBox.information(self, "Help", help_message)
