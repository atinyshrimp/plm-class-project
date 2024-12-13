from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QGuiApplication, QImage, QPixmap
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from io import BytesIO



class SupplierAnalyticsWindow(QDialog):
    def __init__(self, supplier_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supplier Analytics")
        self.resize(800, 600)
        self.supplier_data = supplier_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.fig = Figure()
        ax = self.fig.add_subplot(111)

        # Aggregate data for chart
        supplier_counts = {}
        for row in self.supplier_data:
            supplier = row[5]
            supplier_counts[supplier] = supplier_counts.get(supplier, 0) + 1

        # Plot supplier activity
        suppliers = list(supplier_counts.keys())
        counts = list(supplier_counts.values())
        ax.bar(suppliers, counts, color="skyblue")

        ax.set_title("Deliveries by Supplier")
        ax.set_xlabel("Supplier")
        ax.set_ylabel("Number of Deliveries")

        canvas = FigureCanvas(self.fig)
        layout.addWidget(canvas)
        self.setLayout(layout)

        # Export buttons
        button_layout = QHBoxLayout()
        export_image_button = QPushButton("Export as Image")
        export_image_button.clicked.connect(self.export_as_image)
        copy_clipboard_button = QPushButton("Copy to Clipboard")
        copy_clipboard_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(export_image_button)
        button_layout.addWidget(copy_clipboard_button)
        layout.addLayout(button_layout)

    def export_as_image(self):
        """Export the graph as an image file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Graph", "", "PNG Files (*.png);;JPEG Files (*.jpg)")
        if file_path:
            self.fig.savefig(file_path, format='png')
            QMessageBox.information(self, "Export Successful", f"Graph exported to {file_path}")

    def copy_to_clipboard(self):
        """Copy the graph to the clipboard."""
        # Save the figure to a buffer
        buffer = BytesIO()
        self.fig.savefig(buffer, format='png')
        buffer.seek(0)

        # Load the image into a QImage
        image = QImage.fromData(buffer.read())
        buffer.close()

        # Copy the image to the clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setPixmap(QPixmap.fromImage(image))
        QMessageBox.information(self, "Copy Successful", "Graph copied to clipboard")