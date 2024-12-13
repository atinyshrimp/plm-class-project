from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class SupplierContactDialog(QDialog):
    def __init__(self, supplier_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Contact {supplier_name}")
        self.resize(400, 200)
        self.init_ui(supplier_name)

    def init_ui(self, supplier_name):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"<b>Supplier Name:</b> {supplier_name}"))
        layout.addWidget(QLabel("<b>Email:</b> supplier@example.com"))
        # layout.addWidget(QLabel("<b>Phone:</b> +123 456 789"))
        layout.addWidget(QLabel("<b>Address:</b> 123 Supplier Street, City, Country"))

        self.setLayout(layout)
