from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout


class GoL(QWidget):
    def __init__(self, row, col):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200

        self.initUI(row, col)

    def initUI(self, row, col):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable(row=row, col=col)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def createTable(self, row, col):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)
