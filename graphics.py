from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cell():
    def __init__(self,
                 top_left: Point,
                 bottom_right: Point, 
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
    
    def draw(self, canvas: Canvas, fill_color="black"):
        if self.has_top_wall:
            canvas.create_line(
                self._x1,
                self._y1,
                self._x2,
                self._y1,
                fill=fill_color,
                width=2
            )
        if self.has_left_wall:
            canvas.create_line(
                self._x1,
                self._y1,
                self._x1,
                self._y2,
                fill=fill_color,
                width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self._x1,
                self._y2,
                self._x2,
                self._y2,
                fill=fill_color,
                width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self._x2,
                self._y1,
                self._x2,
                self._y2,
                fill=fill_color,
                width=2
            )

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
    def draw_cell(self, cell: Cell, fill_color: str = "black"):
        cell.draw(self.__canvas, fill_color)

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