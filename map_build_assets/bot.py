from map_build import PointBuilding, debug_print_maze
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
        """Take the best in order of direction"""
        while not self.current_point == self.goal:
            if self.current_point.id + 1 < self.goal.id:
                self.path.append(self.current_point.connections_up[1])
                self.current_point = self.current_point.connections_up[1].move_to(self, self.current_point)
            elif self.current_point.id < self.goal.id:
                self.path.append(self.current_point.connections_up[0])
                self.current_point = self.current_point.connections_up[0].move_to(self, self.current_point)
            elif self.current_point.id - 1 > self.goal.id:
                self.path.append(self.current_point.connections_down[1])
                self.current_point = self.current_point.connections_down[1].move_to(self, self.current_point)
            else:
                self.path.append(self.current_point.connections_down[0])
                self.current_point = self.current_point.connections_down[0].move_to(self, self.current_point)
                
    # Backtracking
