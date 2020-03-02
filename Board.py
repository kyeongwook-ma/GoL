import numpy as np
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout

ON_COLOR = QColor(255, 255, 10)
OFF_COLOR = QColor(0, 0, 0)


class Board(QWidget):
    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Q:
            self.deleteLater()
        event.accept()

        self.quit_func()

    def __init__(self, row, col, quit_func):
        super().__init__()
        self.title = 'PyQt5 table'
        self.left = 0
        self.top = 0
        self.width = 2000
        self.height = 2000

        self.row = row
        self.col = col
        self.grids = np.zeros([row, col]).reshape(row, col)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable(row=row, col=col)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.showFullScreen()

        self.quit_func = quit_func

    def createTable(self, row, col):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.move(0, 0)

        for r in range(row):
            for c in range(col):
                self.tableWidget.setItem(r, c, QTableWidgetItem())
                self.tableWidget.item(r, c).setBackground(OFF_COLOR)

    def check_neighbour(self, check_row, check_col):

        def is_valid_neighbour(row, check_row, col, check_col):

            neighbour_row = check_row + row
            neighbour_column = check_col + col

            if neighbour_row == row and neighbour_column == col:
                return False

            if neighbour_row < 0 or neighbour_row >= self.row:
                return False

            if neighbour_column < 0 or neighbour_column >= self.col:
                return False

            return True

        search_min = -1
        search_max = 2

        neighbour_list = []

        for row in range(search_min, search_max):
            for col in range(search_min, search_max):

                if is_valid_neighbour(row, check_row, col, check_col):
                    neighbour_list.append((check_row + row, check_col + col))

        return neighbour_list


    # https: // en.wikipedia.org / wiki / Conway % 27s_Game_of_Life
    def update_board(self):

        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        # All other live cells die in the next generation.
        def is_will_be_dead(living_neighbour_count, row, col):
            if self.is_cell_alive(row, col):
                if len(living_neighbour_count) < 2 or len(living_neighbour_count) > 3:
                    return True

        # Any dead cell with three live neighbors becomes a live cell.
        # Any live cell with two or three neighbors survives.
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        def is_will_be_alive(living_neighbour_count, row, col):
            if self.is_cell_alive(row, col):
                if len(living_neighbour_count) == 3 or len(living_neighbour_count) == 2:
                    return True

            else:
                if len(living_neighbour_count) == 3:
                    return True

        will_be_dead = []
        will_be_alive = []

        for row in range(len(self.grids)):
            for col in range(len(self.grids[row])):

                check_neighbour = self.check_neighbour(row, col)

                living_neighbour_count = []

                for neighbour_cell in check_neighbour:
                    if self.is_cell_alive(neighbour_cell[0], neighbour_cell[1]):
                        living_neighbour_count.append(neighbour_cell)

                if is_will_be_alive(living_neighbour_count, row, col):
                    will_be_alive.append((row, col))

                if is_will_be_dead(living_neighbour_count, row, col):
                    will_be_dead.append((row, col))

        for cell_items in will_be_alive:
            self.set_status_on(cell_items[0], cell_items[1])
        for cell_items in will_be_dead:
            self.set_status_off(cell_items[0], cell_items[1])

    def set_status_on(self, row, col):
        self.tableWidget.item(row, col).setBackground(ON_COLOR)
        self.grids[row][col] = 1

    def set_status_off(self, row, col):
        self.tableWidget.item(row, col).setBackground(OFF_COLOR)
        self.grids[row][col] = 0

    def is_cell_alive(self, row, col):
        return self.grids[row][col] == 1

    def get_current_status(self):
        return self.grids
