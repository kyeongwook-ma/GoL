import sys
from random import randint

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

import Board

app = QApplication(sys.argv)
is_running = True


def main():
    args = sys.argv

    len_args = len(args)
    num_rows, num_cols = 0, 0
    cells_loc = []

    if len_args == 1:
        num_rows = randint(40, 80)
        num_cols = randint(80, 120)
        cells_loc = [(randint(40, num_rows) - 1, randint(80, num_cols - 1)) for n in range(2000)]

    elif len_args == 2:
        num_rows, num_cols, nums_cell_init = parse_args(args)
        cells_loc = parse_cells_loc(args)

    elif len_args == 3:
        num_rows, num_cols, nums_cell_init = parse_args(args)
        cells_loc = parse_cells_loc(args)

    app.aboutToQuit.connect(app.deleteLater)

    ui = Board.Board(num_rows, num_cols, quit)
    for c in cells_loc:
        ui.set_status_on(c[0], c[1])

    while is_running:
        QTest.qWait(100)
        ui.update_board()


def quit():
    is_running = False
    QCoreApplication.instance().quit()


def parse_cells_loc(args):
    return args[2:]


def parse_args(args):
    num_rows, num_cols = args[0].split(' ')
    nums_cell_init = args[1]
    return num_rows, num_cols, nums_cell_init


main()
