from random import randint


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
