from random import randint


class Connection:
    """Class has a connection list of Points taken when called.

    By default, a price:
        in range of 3-6 INCLUDING start and end"""

    def move_to(self, bot, point):
        """Return the other end of the point.
        if point.id == self.connection_point1.id:

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
        """Name of the Connection"""
        self.connection_point1 = connection1
        """Name of the Connection Point1"""
        self.connection_point2 = connection2
        """Name of the Connection Point2"""
        self.price = randint(3, 6)
        """Price to use the Path"""
        self.distance = connection2.id - connection1.id
        """Distance form connection1, to connection2"""
        connection1.connections.append(self)
        connection2.connections.append(self)

    def direction(self, point):
        """Return the distance if the direction from the point is lower than the endpoint

        else distance * -1"""
        if point.id == self.connection_point1.id:
            return self.distance
        else:
            return self.distance * -1

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
