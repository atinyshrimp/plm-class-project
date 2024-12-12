from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QGuiApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class StockTrendsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Stock Trends by Location")
        self.resize(800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create the matplotlib figure
        self.fig = Figure()
        ax = self.fig.add_subplot(111)

        # Dummy trend data
        trends = {
            "Paris": [50, 45, 40, 38, 30],
            "Lyon": [80, 75, 72, 70, 68],
            "Marseille": [100, 95, 90, 85, 80],
        }

        # Plot each location's stock trends
        for location, values in trends.items():
            ax.plot(range(len(values)), values, marker="o", label=location)

        ax.set_title("Stock Trends by Location")
        ax.set_xlabel("Time Period")
        ax.set_ylabel("Stock Quantity")
        ax.legend()

        # Add the matplotlib canvas to the dialog layout
        canvas = FigureCanvas(self.fig)
        layout.addWidget(canvas)

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
        from io import BytesIO
        buffer = BytesIO()
        self.fig.savefig(buffer, format='png')
        buffer.seek(0)

        # Load the image into a QImage
        from PyQt5.QtGui import QImage, QPixmap
        image = QImage.fromData(buffer.read())
        buffer.close()

        # Copy the image to the clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setPixmap(QPixmap.fromImage(image))
        QMessageBox.information(self, "Copy Successful", "Graph copied to clipboard")