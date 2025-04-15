from copy import deepcopy
from graphics import Cell, Point, Window
from time import sleep

import random

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
        seed: int | None = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._draw_cells()
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for row in range(self._num_rows):
            self._cells.append([])
            for col in range(self._num_cols):
                self._cells[row].append(self._create_cell(row, col))

    def _create_cell(self, r, c):
        top_left = Point(self._x1 + (self._cell_size_x * c),
                         self._y1 + (self._cell_size_y * r))
        bottom_right = deepcopy(top_left)
        bottom_right.x += self._cell_size_x
        bottom_right.y += self._cell_size_y
        return Cell(top_left, bottom_right, self._win)
    
    def _draw_cells(self):
        if isinstance(self._win, Window):
            for row in range(self._num_rows):
                for col in range(self._num_cols):
                    self._draw_cell(row, col)

    def _draw_cell(self, r, c):
        if isinstance(self._win, Window):
            self._cells[r][c].draw()
            self._animate()

    def _animate(self):
        if isinstance(self._win, Window):
            self._win.redraw()
            sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        top_left : Cell = self._cells[0][0]
        top_left.has_top_wall = False
        bottom_right : Cell = self._cells[self._num_rows - 1][self._num_cols - 1]
        bottom_right.has_bottom_wall = False

    def _break_walls_r(self, r: int, c: int):
        curr_cell : Cell = self._cells[r][c]
        curr_cell.visited = True
        while True:
            possible_directions = []
            if 0 < r <= self._num_rows - 1 and not self._cells[r - 1][c].visited:
                possible_directions.append((r - 1, c))
            if 0 < c <= self._num_cols - 1 and not self._cells[r][c - 1].visited:
                possible_directions.append((r, c - 1))
            if 0 <= r < self._num_rows - 1 and not self._cells[r + 1][c].visited:
                possible_directions.append((r + 1, c))
            if 0 <= c < self._num_cols - 1 and not self._cells[r][c + 1].visited:
                possible_directions.append((r, c + 1))
            if not possible_directions:
                break
            choice = random.choice(possible_directions)
            dirRow = choice[0] - r # positive 1 down
            dirCol = choice[1] - c # positive 1 right
            src_cell : Cell = self._cells[r][c]
            dest_cell : Cell = self._cells[choice[0]][choice[1]]
            match dirRow, dirCol:
                case 1, 0:
                    src_cell.has_bottom_wall = False
                    dest_cell.has_top_wall = False
                case -1, 0:
                    src_cell.has_top_wall = False
                    dest_cell.has_bottom_wall = False
                case 0, 1:
                    src_cell.has_right_wall = False
                    dest_cell.has_left_wall = False
                case 0, -1:
                    src_cell.has_left_wall = False
                    dest_cell.has_right_wall = False
                case _:
                    raise ValueError("Invalid direction to break wall")
            self._break_walls_r(choice[0], choice[1])

    def _reset_cells_visited(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._cells[row][col].visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, r: int, c: int) -> bool:
        self._animate()
        current_cell : Cell = self._cells[r][c]
        current_cell.visited = True
        if current_cell is self._cells[self._num_rows - 1][self._num_cols - 1]:
            return True
        directions = []
        if 0 < r <= self._num_rows - 1 and not self._cells[r - 1][c].visited and not current_cell.has_top_wall:
            directions.append((r - 1, c))
        if 0 < c <= self._num_cols - 1 and not self._cells[r][c - 1].visited and not current_cell.has_left_wall:
            directions.append((r, c - 1))
        if 0 <= r < self._num_rows - 1 and not self._cells[r + 1][c].visited and not current_cell.has_bottom_wall:
            directions.append((r + 1, c))
        if 0 <= c < self._num_cols - 1 and not self._cells[r][c + 1].visited and not current_cell.has_right_wall:
            directions.append((r, c + 1))
        for row, col in directions:
            to_cell : Cell = self._cells[row][col]
            current_cell.draw_move(to_cell)
            finished = self._solve_r(row, col)
            if finished:
                return True
            else:
                current_cell.draw_move(to_cell, undo=True)

        return False
    