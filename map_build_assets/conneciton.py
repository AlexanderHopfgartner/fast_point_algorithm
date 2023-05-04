from random import randint

from map_build_assets.point import Point


class Connection(object):
    """Class is a connection Object of two points taken when called.

    By default, price:
        in range of 3-10 INCLUDING start and end."""

    def direction(self, point):
        """Return the distance in the right distance from the parameter point: Point
        to the other end.\n\n +distance/-distance"""
        if point.num == self.connection_point1.num:
            return self.distance
        else:
            return self.distance * -1

    def move_from(self, point: Point) -> Point:
        """Return the other end of the Point.

        Take point: Point"""
        if point == self.connection_point1:
            return self.connection_point2
        else:
            return self.connection_point1

    def recalculate_price(self, start: int = 3, end: int = 10):
        """Recalculate the price of a Connection.

        Take start: int start range (included)
        end: int end range (included)
        By Default start=3, end=10 including start and end"""
        self.price: int = randint(start, end)

    def __init__(self, connection1: Point, connection2: Point, start: int = 3, end: int = 10):
        self.name: str = f"Connection of {connection1.name} and {connection2.name}"
        """Name of the Connection."""
        self.connection_point1: Point = connection1
        """Name of the Connection Point1."""
        self.connection_point2: Point = connection2
        """Name of the Connection Point2."""
        self.price: int = randint(start, end)
        """Price to use the Path."""
        self.distance: int = connection2.num - connection1.num
        """Distance form connection1, to connection2."""
        connection1.connections.append(self)
        connection2.connections.append(self)

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
