from random import randint
from os import system, name
from time import time
from map_build_assets.conneciton import Connection
from map_build_assets.point import Point


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def debug_print_maze(maze, bot):
    """prints:

    Point name///Connection name///Connection price///start///end"""
    print([x.name for x in maze.points])
    print([x.name for x in maze.connections])
    print([x.price for x in maze.connections])
    print(maze.start, maze.end, "\n")
    print(bot.investment)

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

    def take_connection(self, position, connection):
        """Add the investment of the Connection changes the current location from the bot

        bot: Bot, position: Position, connection: Conneciton"""
        self.position.current_point = connection.take(self.position, position)

    def __init__(self, size: int):
        self.points_amount = size
        self.points = self.points_self()
        self.connections = self.connect_self()
        self.start = self.start_self()
        self.end = self.end_self()
        self.position = self.start
