import webbrowser
from PyQt5 import QtGui
from PyQt5.QtWidgets import QAction, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget, QMenuBar, QDesktopWidget, QMessageBox
from components.navbar import NavBar
from components.product_tabs import ProductTabs
from components.people_tabs import PeopleTabs
from components.process_tabs import ProcessTabs
from components.data_tabs import DataTabs
from utils.styling import apply_stylesheet

class PLMApp(QWidget):
    def __init__(self, version):
        super().__init__()
        self.version = version  # Store the version
        self.setWindowTitle(f"Hive (PLM Internal Software) v{self.version}")
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

        # Initialize the menu bar
        menubar = self.init_menu_bar()
        main_layout.setMenuBar(menubar)

        # Main content layout
        content_layout = QHBoxLayout()
        self.navbar = NavBar()
        self.tab_widget_stack = QStackedWidget(self)

        # Initialize and add tab widgets
        self.tab_widget_stack.addWidget(ProductTabs())
        self.tab_widget_stack.addWidget(PeopleTabs())
        self.tab_widget_stack.addWidget(ProcessTabs())
        self.tab_widget_stack.addWidget(DataTabs())
        self.tab_widget_stack.setCurrentIndex(0)  # Default to the first tab set

        # Connect navbar clicks to change the displayed content
        self.navbar.currentRowChanged.connect(self.display_tabs)

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
        file_menu.addAction("New", self.new_file)

        save_action = QAction
        file_menu.addAction("Save", self.save_file)
        file_menu.addAction("Export", self.export_data)
        file_menu.addAction("Exit", self.close_application)

        # Edit Menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Undo", self.undo_action)
        edit_menu.addAction("Redo", self.redo_action)
        edit_menu.addAction("Cut", self.cut_action)
        edit_menu.addAction("Copy", self.copy_action)
        edit_menu.addAction("Paste", self.paste_action)

        # Help Menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("About", self.show_about)
        help_menu.addAction("Help", self.show_help_documentation)
        help_menu.addSeparator()
        help_menu.addAction("Visit GitHub Repository", lambda: webbrowser.open("https://github.com/atinyshrimp/plm-class-project"))

        return menubar

    def display_tabs(self, index):
        """Update the content displayed based on the selected item in the navbar."""
        self.tab_widget_stack.setCurrentIndex(index)

    # Menu actions
    def new_file(self):
        print("New File")

    def save_file(self):
        print("Save File")

    def export_data(self):
        print("Exporting Data...")

    def close_application(self):
        self.close()

    def undo_action(self):
        print("Undo Action")

    def redo_action(self):
        print("Redo Action")

    def cut_action(self):
        print("Cut Action")

    def copy_action(self):
        print("Copy Action")

    def paste_action(self):
        print("Paste Action")

    def show_about(self):
        about_message = f"PLM Tool v{self.version}\nDeveloped by MGO S.A. Group for managing product lifecycle."
        QMessageBox.about(self, "About", about_message)

    def show_help_documentation(self):
        help_message = "For help, visit our documentation or contact support."
        QMessageBox.information(self, "Help", help_message)