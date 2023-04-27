from random import randint
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Bot:
    def __init__(self, name="Fridolin", start=0):
        self.name = name
        self.current_point = start
        self.path = []
        self.investment = 0

    def find_path(self):
        pass

class Build:
    def __init__(self, size):
        self.points_amount = size
        self.points = []
        self.connections = []
        self.start = Point()
        self.end = Point()

    def build_points(self):
        """Build all points in the given range of self.
        Points_amount and connects them all in the connection range of 1 and 2"""
        self.points = [Point(x) for x in range(self.points_amount)]

        self.connect_in_range(input("Please enter the Number ob distance of every point, seperate them with a Space "
                                    "\", \"\nDefault: (\"1, 2\")\n").split(", "))
        for x in self.connections:
            x.calculate_price()

    def connect_in_range(self, *args):
        """Connects all points in a given distance"""
        if args == ([''],):
            args = [[1, 2]]
        else:
            for x in args[0]:
                if int(x) >= self.points_amount:
                    args = [[1, 2]]
        for distance in args[0]:
            for x in range(len(self.points)-int(distance)):
                self.connections.append(Connection([self.points[x], self.points[x+int(distance)]]))

    def set_end_start(self):
        self.start = self.points[randint(0, len(self.points)-1)]
        self.end = self.points[randint(0, len(self.points) - 1)]
        while self.start == self.end:
            self.set_end_start()


class Point:
    def __init__(self, x=0):
        self.id = x
        self.name = f"Point {x+1}"

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name


class Connection:
    def __init__(self, x):
        self.name = f"Conneciton of {x[0].name} and {x[1].name}"
        self.price = 0

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def calculate_price(self):
        self.price = randint(3, 6)


def debug_print_maze(maze):
    print([x.name for x in maze.points])
    print([x.name for x in maze.connections])
    print([x.price for x in maze.connections])
    print(maze.start, maze.end)


def build(size):
    maze = Build(size)
    maze.build_points()
    # debug_print_maze(maze)
    maze.set_end_start()
    return maze
