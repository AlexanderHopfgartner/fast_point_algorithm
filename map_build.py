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


Distances = tuple[int, int]


def debug_print_maze(maze, bot, head_info) -> list[str]:
    """Return: list [str]\nPoint:[X],\nConnections:[x],\nPrices:[X],\nStart: start.Point,\nGoal: goal.Point,
    current position: current_position.Point,\nCost: path.price, Path: [X],\n length of the path: len(path)"""
    return ["\n" + f"{head_info:^20}".center(80, "*") + "\n\n",
            "Points:\t\t\t\t", [x.name for x in maze.points],
            "Connections:\t\t", [x.name for x in maze.connections],
            "Prices:\t\t\t\t", [str(x.price) for x in maze.connections],
            "\nSTART:\t\t\t\t" + str(maze.start), "\nGOAL:\t\t\t\t" + str(maze.end),
            "\ncurrent position:\t" + str(bot.current_point) + " ",
            "\nCost : " + str(bot.price()), "\nPath: ",
            [[path, maze.connections.index(path)] for path in bot.path], "length of the path: " + str(len(bot.path))]


class PointBuilding(object):
    """Class is a Simulation holder
    takes:
    size: int defines size of the Simulation and point_amount. By default, 12
    distances: tuple[int, int] distances from Point1 and Point2. By default, (1, 2)
    distances CAN take tuple with multiple amounts of int (can cause IDE-highlight).
    start: int index of the start. By default, 0
    end: int index of the end. By default, -1"""

    def connect_in_range(self, distances: Distances) -> list[Connection]:
        """Return a list of all Connections.

        Take distances: tuple[int, int] the distance form Point1 to Point2
        distances CAN take tuple with multiple amounts of int (can cause IDE-highlight).

        If ANY int in the distance: tuple[int, Int] >= point_amount it become default

        By default, (1, 2)"""
        all_connections = []
        for x in distances:
            if x >= self.points_amount:
                distances = (1, 2)
        for distance in distances:
            for point in range(len(self.points) - distance):
                all_connections.append(Connection(self.points[point], self.points[point + int(distance)]))
        self.connections = all_connections
        return all_connections

    def connect_self(self, distances: Distances = (1, 2)) -> list[Connection]:
        """Return a list of connects in range (1, 2)"""
        return self.connect_in_range(distances)

    def end_self(self) -> Point:
        """Return random end Point"""
        return self.points[randint(0, len(self.points) - 1)]

    def points_self(self) -> list[Point]:
        """Return a list of Points in the range of the points_amount"""
        return [Point(x) for x in range(self.points_amount)]

    def rebuild_build_points(self, size: int = 12, distances: Distances = (1, 2),
                             price_start: int = 3, price_end: int = 10, start: int = 0, end: int = -1):
        """Rebuild all points.

        size: int = re-defines the point amount. By default, 12
        distances: tuple[int, int] re-defines the distances between the points. By default, (1, 2)
        distances CAN take tuple with multiple amounts of int (can cause IDE-highlight).
        price_start: int set start range of the price. By default, 3
        price_end: int set end range of the price. By default, 10
        start: int re-defines the start. By default, 0
        end: int re-define the end. By default -1"""
        self.points_amount = size
        self.points = []
        self.connections = []
        self.start = Point()
        self.end = Point()

        self.points = self.points_self()
        self.connections = self.connect_in_range(distances)
        for connection in self.connections:
            connection.recalculate_price(start=price_start, end=price_end)
        self.set_start_end(start, end)

    def set_end(self, end: int):
        """Change the end to the taken index"""
        self.end = self.points[end]

    def set_start(self, start: int):
        """Change the start to the taken index"""
        self.start = self.points[start]

    def set_start_end(self, *args, **kwargs):
        """Change the start and the end to the given kwargs. By default, RANDOM

        start: int = index of the start Point
        end: int = index of the end Point"""
        while self.start == self.end:
            if args:
                if args[0] <= self.points_amount:
                    self.set_start(args[0])
                else:
                    self.start = self.start_self()
            try:
                kwargs["start"]
            except KeyError:
                self.start = self.start_self()
            else:
                if kwargs["start"] <= self.points_amount:
                    self.set_start(kwargs["start"])
                else:
                    self.start = self.start_self()
            if len(args) > 1:
                if args[1] <= self.points_amount:
                    self.set_start(args[1])
                else:
                    self.start = self.start_self()
            try:
                kwargs["start"]
            except KeyError:
                self.end = self.end_self()
            else:
                if kwargs["end"] <= self.points_amount:
                    self.set_end(kwargs["end"])
                else:
                    self.end = self.end_self()
            if self.start == self.end and args and kwargs:
                self.end = self.end_self()
                self.start = self.start_self()
                break

    def start_self(self) -> Point:
        """Return random start Point"""
        return self.points[randint(0, len(self.points) - 1)]

    def take_connection(self, connection: Connection):
        """Change the position to the other end of the Connection"""
        self.position = connection.move_from(self.position)

    def __init__(self, size: int = 12, distances: Distances = (1, 2), start: int = 0, end: int = -1):
        """Default is a Creator recommendation for performance"""
        self.points_amount = size
        self.points: list[Point] = self.points_self()
        self.connections: list[Connection] = self.connect_self(distances)
        self.start: Point = Point()
        self.set_start(start)
        self.end: Point = Point()
        self.set_end(end)
        self.position: Point = self.start
        self.set_start_end()
