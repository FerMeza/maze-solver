from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Window():
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Cell():
    def __init__(self,
                 top_left: Point,
                 bottom_right: Point,
                 win: Window | None = None,
                 has_left_wall: bool = True,
                 has_right_wall: bool = True, 
                 has_top_wall: bool = True, 
                 has_bottom_wall: bool = True,
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win
    
    def draw(self):
        if not isinstance(self._win, Window):
            return
        line = Line(Point(self._x1, self._y1), Point(self._x2,self._y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(self._x1, self._y1), Point(self._x1,self._y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(self._x1, self._y2), Point(self._x2,self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(self._x2, self._y1), Point(self._x2,self._y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if not isinstance(self._win, Window):
            return
        self_center_x = (self._x1 + self._x2) // 2
        self_center_y = (self._y1 + self._y2) // 2
        src_point = Point(self_center_x, self_center_y)
        other_center_x = (to_cell._x1 + to_cell._x2) // 2
        other_center_y = (to_cell._y1 + to_cell._y2) // 2
        dest_point = Point(other_center_x, other_center_y)
        line = Line(src_point, dest_point)
        color = "red"
        if undo:
            color = "gray"
        self._win.draw_line(line, color)

class Line():
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=2
        )