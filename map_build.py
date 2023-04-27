from random import randint
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Bot:
    def __init__(self, bot_name="Fridolin", start=0):
        self.name = bot_name
        self.current_point = start
        self.path = []
        self.investment = 0

    def __call__(self, *args, **kwargs):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def find_path(self):
        pass


class PointBuilding:
    """Takes a size: int, """
    def __init__(self, size: int):
        self.points_amount = size
        self.points = self.points_self()
        self.connections = self.connect_self()
        self.start = self.start_self()
        self.end = self.end_self()

    def rebuild_build_points(self, size: int = 8, distance: list[int] = [1, 2],
                             price_start: int = 3, price_end: int = 6, start: int = 0, end: int = -1):
        """Rebuild all points.

        size: takes an int and RE-defines the point amount. By default, int(8)

        distance: takes a list of ints and RE-defines the distances between the points. By default, list(int(1), int(2))

        start: takes an int and RE-defines the start. By default, 3

        Build all points in the given range of points_amount
        connects them all by default, in a range of 1 and 2"""
        self.points_amount = size
        self.connections = self.connect_in_range(distance)
        for connection in self.connections:
            connection.recalculate_price(start=price_start, end=price_end)
        self.set_start_end(start, end)

    def points_self(self):
        return [Point(x) for x in range(self.points_amount)]

    def connect_self(self):
        return self.connect_in_range([1, 2])

    def connect_in_range(self, distances: list[int] = ""):
        """Return a list of all Connections, By the points.
        ints form the list, set the fixed distance form the points

        If any int in the distance: list[int] >= point_amount it become default

        By default, [1, 2]"""
        print(distances)
        all_connections = []
        if distances == "":
            distances = [1, 2]
        for x in distances:
            if x >= self.points_amount:
                distances = [1, 2]
        for distance in distances:
            for point in range(len(self.points)-distance):
                all_connections.append(Connection([self.points[point], self.points[point+int(distance)]]))
        self.connections = all_connections
        return all_connections

    def start_self(self):
        """Return random start Point"""
        return self.points[randint(0, len(self.points)-1)]

    def end_self(self):
        """Return random end Point"""
        return self.points[randint(0, len(self.points) - 1)]

    def set_start(self, start):
        """Change the start to the taken index"""
        self.start = self.points[start]

    def set_end(self, end):
        """Change the end to the taken index"""
        self.end = self.points[end]

    def set_start_end(self, *args, **kwargs):
        """Change the start and the end to the given kwargs. By default, RANDOM

        start: int = to index the start Point
        end: int = to index the end Point"""
        try:
            kwargs["start"]
        except KeyError:
            self.start = self.start_self()
        else:
            self.set_start([kwargs["start"]])

        try:
            kwargs["start"]
        except KeyError:
            self.end = self.end_self()
        else:
            self.set_end([kwargs["end"]])


class Point:
    def __init__(self, x=0):
        self.id = x
        """Id of the Point"""
        self.name = f"Point {x+1}"
        """Name of the Class"""

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Connection:
    """Class has a connection list of Points taken when called.

    By default, a price:
        in range of 3-6 INCLUDING start and end"""
    def __init__(self, x: list):
        self.name = f"Connection of {x[0].name} and {x[1].name}"
        """Name of the Connection"""
        self.connection = x
        """List of two Points"""
        self.price = randint(3, 6)
        """Price to use the Path"""

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def recalculate_price(self, start=3, end=6):
        """Recalculate the price of a Connection.

        By Default start=3, end=6 including start and end"""
        self.price = randint(start, end)


def debug_print_maze(maze):
    print([x.name for x in maze.points])
    print([x.name for x in maze.connections])
    print([x.price for x in maze.connections])
    print(maze.start, maze.end, "\n")
