class Point:

    def __init__(self, x=0):
        self.id = x
        """Id of the Point"""
        self.name = f"Point {x + 1}"
        """Name of the Class"""
        self.connections = []
        """All Connections in a list"""
        self.connections_up = []
        """All Connections in a list on the increasing path"""
        self.connections_down = []
        """All Connections in a list on the decreasing path"""

    def __call__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
