import math
import sys
from random import randint

import numpy as np
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

import Board

app = QApplication(sys.argv)
ui = None

def main():
    args = sys.argv

    len_args = len(args)
    num_rows, num_cols = 0, 0
    cells_loc = []
    n_generation = math.inf

    if len_args == 1:
        num_rows = randint(40, 80)
        num_cols = randint(80, 120)
        cells_loc = [(randint(40, num_rows) - 1, randint(80, num_cols - 1)) for n in range(2000)]

    elif len_args == 2:
        num_rows, num_cols, cells_loc = parse_args(args)

    elif len_args == 3:
        num_rows, num_cols, cells_loc = parse_args(args)
        n_generation = int(args[2])

    ui = Board.Board(num_rows, num_cols)
    for c in cells_loc:
        ui.set_status_on(c[0], c[1])

    i = 0
    while i < n_generation:
        i += 1
        ui.update_board()
        QTest.qWait(100)

    if n_generation < math.inf:
        current_status = ui.get_current_status()
        result_file = open('./result.txt', 'w')
        result_file.write(np.array_str(current_status))
        result_file.close()

    sys.exit(app.exec_())

def parse_cells_loc(args):
    return args[2:]

def parse_args(args):
    def parse_line(line):
        return line.replace('\n', '').split(' ')

    file_path = args[1]

    fp = open(file_path, 'rt')

    num_rows, num_cols = 0, 0
    cell_init_locs = []

    for idx, line in enumerate(fp):
        if idx == 0:
            l, r = parse_line(line)

            num_rows, num_cols = int(l), int(r)
        if idx > 1:
            l, r = parse_line(line)

            cell_init_locs.append((int(l), int(r)))

    return num_rows, num_cols, cell_init_locs


main()
