from map_build import PointBuilding
from random import randint


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
            connection_index = randint(0, len(self.current_point.connections) - 1)
            self.current_point = self.current_point.connections[connection_index].take(self, self.current_point)
