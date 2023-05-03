from map_build import PointBuilding, debug_print_maze
from random import randint


class BotHolder:
    id_counter = 0

    def __init__(self, *args):
        BotHolder.id_counter += 1
        self.name = f"{args[0].name}_{BotHolder.id_counter}"
        self.current_point = args[0].current_point
        self.goal = args[0].goal
        self.current_path = []
        self.path_holder = []
        self.maze = args[0].maze

    def backtrack(self):
        if self.current_point == self.goal:
            self.path_holder.append(self.current_path[::])
            return
        for connection in self.current_point.connections:
            if connection not in self.current_path:
                self.move_unmove(connection)
                self.backtrack()
                self.move_unmove(connection)

    def move_unmove(self, connection):
        if self.current_path and self.current_path[-1] == connection:
            self.current_path.pop()
        else:
            self.current_path.append(connection)
        self.current_point = connection.move_from(self.current_point)


class Bot(BotHolder):

    def __init__(self, bot_name="Fridolin", maze=PointBuilding(8)):
        self.name = bot_name
        self.current_point = maze.start
        self.goal = maze.end
        self.path = []
        self.investment = 0
        self.maze = maze
        super().__init__(self)

    def __call__(self, *args, **kwargs):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def move_path(self, ):
        for connection in self.path:
            connection.move_from(self.current_point)

    def take_path(self, connection):
        self.current_point = connection.move_from(self.current_point)

    def untake_path(self, connection):
        self.current_path.pop()
        self.current_location \
            = connection.move_from(self.current_point)

    def price(self, path):
        return sum([connection.price for connection in path])

    def current_price(self):
        return sum([connection.price for connection in self.current_path])

    def find_path1(self):
        self.backtrack()
        min_path_id = [self.price(path) for path in self.path_holder].index(min([self.price(path) for path in self.path_holder]))
        self.path = self.path_holder[min_path_id]
        self.investment = self.price(self.path)
        [self.take_path(connection) for connection in self.path]


        # if self.current_location == self.goal:
        #     if not self.path:
        #         self.path = self.current_path
        #     if self.current_price() < self.price():
        #         self.path = self.current_path
        # for connection in self.current_location.connections:
        #     if connection not in self.current_path:
        #         self.take_path(connection)
        #         self.find_path1()
        #         self.untake_path(connection)
        # print(self.path)
        # self.investment = self.price()
        # self.move_path()

    def find_path(self):
        """Take the fastest path, from current_point to goal by orienting py Points and Connections"""
        while not self.current_point == self.goal:
            pass

        # while not self.current_point == self.goal:
        #     if self.current_point.id + 1 < self.goal.id:
        #         self.path.append(self.current_point.connections_up[1])
        #         self.current_point = self.current_point.connections_up[1].move_from(self, self.current_point)
        #     elif self.current_point.id < self.goal.id:
        #         self.path.append(self.current_point.connections_up[0])
        #         self.current_point = self.current_point.connections_up[0].move_from(self, self.current_point)
        #     elif self.current_point.id - 1 > self.goal.id:
        #         self.path.append(self.current_point.connections_down[1])
        #         self.current_point = self.current_point.connections_down[1].move_from(self, self.current_point)
        #     else:
        #         self.path.append(self.current_point.connections_down[0])
        #         self.current_point = self.current_point.connections_down[0].move_from(self, self.current_point)

    # Backtracking
