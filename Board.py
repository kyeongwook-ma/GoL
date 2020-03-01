from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout

class GoL(QWidget):

    def __init__(self, row, col):
        super().__init__()
        self.title = 'PyQt5 table'
        self.left = 0
        self.top = 0
        self.width = 2000
        self.height = 2000

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable(row=row, col=col)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.showFullScreen()

    def createTable(self, row, col):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)

        for r in range(row):
            for c in range(col):
                self.tableWidget.setItem(r, c, QTableWidgetItem())
                self.tableWidget.item(r, c).setBackground(QColor(0, 0, 0))

    def update_board(self):
        pass

    def set_status_on(self, row, col):
        pass

    def set_status_off(self, row, col):
        pass
