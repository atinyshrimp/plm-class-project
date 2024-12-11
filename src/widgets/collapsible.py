from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QListWidget, QHBoxLayout

class CollapsibleSection(QWidget):
    def __init__(self, title, content_widget):
        super().__init__()
        self.init_ui(title, content_widget)

    def init_ui(self, title, content_widget):
        layout = QVBoxLayout()

        # Toggle button
        self.toggle_button = QPushButton(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)  # Default: Not Expanded
        self.toggle_button.clicked.connect(self.toggle_content)
        layout.addWidget(self.toggle_button)

        # Frame for collapsible content
        self.content_frame = QFrame()
        self.content_frame.setLayout(QVBoxLayout())
        self.content_frame.layout().addWidget(content_widget)
        self.content_frame.setVisible(False) # Hide content upon creation
        layout.addWidget(self.content_frame)

        self.setLayout(layout)

    def toggle_content(self):
        """Show or hide the content based on the toggle button."""
        self.content_frame.setVisible(self.toggle_button.isChecked())
