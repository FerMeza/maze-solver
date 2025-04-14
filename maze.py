from copy import deepcopy
from graphics import Cell, Point, Window
from time import sleep

class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for row in range(self._num_rows):
            self._cells.append([])
            for col in range(self._num_cols):
                self._cells[row].append(self._create_cell(row, col))
                self._draw_cell(row, col)

    def _create_cell(self, r, c):
        top_left = Point(self._x1 + (self._cell_size_x * c),
                         self._y1 + (self._cell_size_y * r))
        bottom_right = deepcopy(top_left)
        bottom_right.x += self._cell_size_x
        bottom_right.y += self._cell_size_y
        return Cell(top_left, bottom_right, self._win)

    def _draw_cell(self, r, c):
        if isinstance(self._win, Window):
            self._cells[r][c].draw()
            self._animate()

    def _animate(self):
        if isinstance(self._win, Window):
            self._win.redraw()
            sleep(0.05)