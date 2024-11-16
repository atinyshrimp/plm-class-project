from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QSizePolicy, QHeaderView

# Utility Class for CustomTable
class CustomTable(QTableWidget):
    def __init__(widget, rows=5, columns=3, headers=None):
        super().__init__(rows, columns)
        widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widget.verticalHeader().setVisible(False)
        if headers:
            widget.setHorizontalHeaderLabels(headers)
