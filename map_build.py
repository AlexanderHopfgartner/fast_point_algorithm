from random import randint
from os import system, name
from time import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def debug_print_maze(maze):
    """prints:

    Point name///Connection name///Connection price///start///end"""
    print([x.name for x in maze.points])
    print([x.name for x in maze.connections])
    print([x.price for x in maze.connections])
    print(maze.start, maze.end, "\n")


class Timer:

    def time_stop(self):
        self.time_stop.append(time())
        print(self.time_stop[-1] - self.start)

    def end_time(self):
        print(time() - self.start)


    def __init__(self):
        self.start = time()
        self.time_stop = []


class PointBuilding:
    """Takes a size: int, """

    def connect_in_range(self, distances: list[int] = ""):
        """Return a list of all Connections, By the points.
        ints form the list, set the fixed distance form the points

        If any int in the distance: list[int] >= point_amount it become default

        By default, [1, 2]"""
        all_connections = []
        if distances == "":
            distances = [1, 2]
        for x in distances:
            if x >= self.points_amount:
                distances = [1, 2]
        for distance in distances:
            for point in range(len(self.points) - distance):
                all_connections.append(Connection(self.points[point], self.points[point + int(distance)]))
        self.connections = all_connections
        return all_connections

    def connect_self(self):
        """Return a list of connects in range [1, 2]"""
        return self.connect_in_range([1, 2])

    def end_self(self):
        """Return random end Point"""
        return self.points[randint(0, len(self.points) - 1)]

    def points_self(self):
        """Return a list of Points in the range of the points_amount"""
        return [Point(x) for x in range(self.points_amount)]

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

    def set_end(self, end):
        """Change the end to the taken index"""
        self.end = self.points[end]

    def set_start(self, start):

        """Change the start to the taken index"""
        self.start = self.points[start]

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

    def start_self(self):
        """Return random start Point"""
        return self.points[randint(0, len(self.points) - 1)]

    def take_connection(self, bot, position, connection):
        """Add the investment of the Connection changes the current locaiton from the bot

        bot: Bot, position: Positon, connection: Conneciton"""
        bot.current_point = connection.take(bot, position)



    def __init__(self, size: int):
        self.points_amount = size
        self.points = self.points_self()
        self.connections = self.connect_self()
        self.start = self.start_self()
        self.end = self.end_self()


class Point:

    def add_conneciton(self, connection):
        pass

    def __init__(self, x=0):
        self.id = x
        """Id of the Point"""
        self.name = f"Point {x + 1}"
        """Name of the Class"""
        self.connections = []
        """All Connetions in a list"""

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

    def take(self, bot, point):
        """Return the other end of the point.

        Adds the price of the point to the bot investment

        Takes bot: Bot and point: Point"""

        bot.investment += self.price
        if point == self.connection_point1:
            return self.connection_point2
        else:
            return self.connection_point1

    def recalculate_price(self, start=3, end=6):
        """Recalculate the price of a Connection.

        By Default start=3, end=6 including start and end"""
        self.price = randint(start, end)

    def __init__(self, connection1, connection2):
        self.name = f"Connection of {connection1.name} and {connection2.name}"
        """Name of the Connection Point1"""
        self.connection_point1 = connection1
        """Name of the Connection Point2"""
        self.connection_point2 = connection2
        """List of two Points"""
        self.price = randint(3, 6)
        """Price to use the Path"""
        connection1.connections.append(self)
        connection2.connections.append(self)

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Bot:

    def __init__(self, bot_name="Fridolin", maze=PointBuilding(8)):
        self.name = bot_name
        self.current_point = maze.start
        self.goal = maze.end
        self.path = []
        self.investment = 0
        self.maze = maze

    def __call__(self, *args, **kwargs):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def find_path(self):
        """Take a random path until self.current_point == self.goal"""
        while not self.current_point == self.goal:
            connectionindex = randint(0, len(self.current_point.connections) - 1)
            self.current_point = self.current_point.connections[connectionindex].take(self, self.current_point)
