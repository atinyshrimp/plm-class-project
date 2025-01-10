from datetime import datetime
from io import BytesIO

import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import QGuiApplication, QImage, QPixmap
from PyQt5.QtWidgets import (
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QBoxLayout,
)


class StockTrendsWindow(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.setWindowTitle("Stock Trends by Location")
        self.resize(800, 600)
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout(self)

        # Create the matplotlib figure
        self.fig = Figure()
        # ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        # Parse the data into a format suitable for plotting
        trends = self.parse_data(self.data)

        # Plot each location's stock trends
        self.plot_trends(trends)

        self.set_layout(layout)

    def parse_data(self, data: list, is_test: bool = False):
        """Parse the data into a format suitable for plotting.

        Args:
            data (list): A list of tuples containing the location, stock level, and arrival date.
            is_test (bool): A flag to indicate whether the function is being called for testing purposes.

        Returns:
            dict: A dictionary containing the stock trends for each location.
        """
        if is_test:
            # Dummy implementation
            return {
                "Paris": [50, 45, 40, 38, 30],
                "Lyon": [80, 75, 72, 70, 68],
                "Marseille": [100, 95, 90, 85, 80],
            }

        # Parse the data into a dictionary
        trends = {}
        for location, stock_level, arrival_date in data:
            if "," in location:
                location = location.split(",")[-1].strip()
            arrival_date = datetime.strptime(
                arrival_date, "%Y-%m-%d"
            )  # Adjust the format as needed
            if location in trends:
                trends[location].append((arrival_date, stock_level))
            else:
                trends[location] = [(arrival_date, stock_level)]
        return trends

    def plot_trends(self, trends: dict):
        """Plot the stock trends for each location."""
        # Create a subplot
        ax = self.fig.add_subplot(111)
        all_dates = []

        # Iterate over each location's trend data
        for location, trend in trends.items():
            # Sort the trend data by date and unpack into separate lists
            dates, stock_levels = zip(*sorted(trend))
            if len(stock_levels) < 2:
                continue
            all_dates.extend(dates)
            # Plot the stock levels over time for the current location
            ax.plot(dates, stock_levels, label=location)

        # Set the title and labels for the axes
        ax.set_title("Stock Trends by Location")
        ax.set_xlabel("Time")
        ax.set_ylabel("Stock Level")

        # Format the x-axis to show dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())

        # Set the x-axis limits to the range of all dates
        ax.set_xlim(min(all_dates), max(all_dates))

        # Add a legend to the plot
        ax.legend()

        # Redraw the canvas to update the plot
        self.canvas.draw()

    def set_layout(self, layout: QBoxLayout):
        """Set the layout of the dialog window.

        Args:
            layout (QBoxLayout): The layout to set for the dialog window.
        """
        self.canvas = FigureCanvas(self.fig)

        button_layout = QHBoxLayout()
        export_image_button = QPushButton("Export as Image")
        export_image_button.clicked.connect(self.export_as_image)
        copy_clipboard_button = QPushButton("Copy to Clipboard")
        copy_clipboard_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(export_image_button)
        button_layout.addWidget(copy_clipboard_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def export_as_image(self):
        """Export the graph as an image file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Graph", "", "PNG Files (*.png);;JPEG Files (*.jpg)"
        )
        if file_path:
            self.fig.savefig(file_path, format="png")
            QMessageBox.information(
                self, "Export Successful", f"Graph exported to {file_path}"
            )

    def copy_to_clipboard(self):
        """Copy the graph to the clipboard."""
        # Save the figure to a buffer
        buffer = BytesIO()
        self.fig.savefig(buffer, format="png")
        buffer.seek(0)

        # Load the image into a QImage
        image = QImage.fromData(buffer.read())
        buffer.close()

        # Copy the image to the clipboard
        clipboard = QGuiApplication.clipboard()
        clipboard.setPixmap(QPixmap.fromImage(image))
        QMessageBox.information(self, "Copy Successful", "Graph copied to clipboard")
