from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit

class BatchDetailsDialog(QDialog):
    def __init__(self, batch_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Batch Details - Lot {batch_data[0]}")
        self.resize(400, 300)
        self.init_ui(batch_data)

    def init_ui(self, batch_data):
        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"<b>Lot ID:</b> {batch_data[0]}"))
        layout.addWidget(QLabel(f"<b>Product ID:</b> {batch_data[1]}"))
        layout.addWidget(QLabel(f"<b>Process Name:</b> {batch_data[2]}"))
        layout.addWidget(QLabel(f"<b>Date:</b> {batch_data[3]}"))
        layout.addWidget(QLabel(f"<b>Factory:</b> {batch_data[4]}"))
        layout.addWidget(QLabel("<b>Ingredients:</b>"))
        ingredients_field = QTextEdit(batch_data[5])
        ingredients_field.setReadOnly(True)
        layout.addWidget(ingredients_field)
        layout.addWidget(QLabel(f"<b>Merchandise ID:</b> {batch_data[6]}"))

        self.setLayout(layout)