from graphics import Line, Point, Window

def main():
    win = Window(800, 600, "Maze Solver")
    line1 = Line(Point(2,3), Point(200, 300))
    win.draw_line(line1, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()