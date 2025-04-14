from graphics import Cell, Point, Window

def main():
    win = Window(800, 600, "Maze Solver")
    c = Cell(win, Point(50, 50), Point(200, 200))
    c2 = Cell(win, Point(250, 250), Point(450, 450), True, True, False, False)
    c.draw()
    c2.draw()
    c.draw_move(c2, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()