class Point(object):
    """Class is a Point in the Simulation.
    take num: int """
    point_id = 0

    def __init__(self, num: int = 0):
        Point.point_id += 1
        self.point_id = Point.point_id
        self.num = num
        """Id of the Point."""
        self.name = f"Point {num + 1}"
        """Name of the Point."""
        self.connections = []
        """All Connections in a list."""

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
