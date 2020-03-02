import sys
from random import randint

from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

import Board


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

    app = QApplication(sys.argv)
    ui = Board.Board(num_rows, num_cols)

    for c in cells_loc:
        ui.set_status_on(c[0], c[1])

    while True:
        QTest.qWait(100)
        ui.update_board()

    sys.exit(app.exec_())


def parse_cells_loc(args):
    return args[2:]


def parse_args(args):
    num_rows, num_cols = args[0].split(' ')
    nums_cell_init = args[1]
    return num_rows, num_cols, nums_cell_init


main()
