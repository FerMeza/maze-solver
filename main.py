from graphics import Cell, Point, Window

def main():
    win = Window(800, 600, "Maze Solver")
    c = Cell(Point(50, 50), Point(200, 200))
    c2 = Cell(Point(150, 100), Point(300, 200), True, True, False, False)
    win.draw_cell(c, "black")
    win.draw_cell(c2, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()