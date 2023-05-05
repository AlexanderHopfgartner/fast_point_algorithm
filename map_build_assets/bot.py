from map_build import PointBuilding, debug_print_maze


class BotHolder:
    """Class is a holder to calculate for the Bot."""
    id_counter = 0

    def __init__(self, *args):
        BotHolder.id_counter += 1
        self.name = f"{args[0].name}_{BotHolder.id_counter}"
        self.current_point = args[0].current_point
        self.goal = args[0].goal
        self.current_path = []
        self.path_holder = []
        self.maze = args[0].maze
        self.orderd_connections = []

    def backtrack(self):
        """Return with all bruteforce path POSSIBILITIES copied in the path_holder."""
        if self.current_point == self.goal:
            self.path_holder.append(self.current_path[:])
            return
        for connection in self.current_point.connections:
            if connection not in self.current_path:
                self.move_unmove(connection)
                self.backtrack()
                self.move_unmove(connection)

    def closest(self, distance):
        return self.current_point.connections[min(range(len(self.current_point.connections)), key=lambda i: abs([connection.direction(self.current_point) for connection in self.current_point.connections][i] - distance))]

    def distance_ordered(self):
        ordered_list = []
        all_connections = self.current_point.connections
        while all_connections:
            closest_connection = self.closest(self.goal.num)
            ordered_list.append(all_connections.pop(all_connections.index(closest_connection)))
        return ordered_list

    def move_unmove(self, connection):
        """Move the connection: Connection.
        Removes Connection, if it was the last Connection in the current_path.
        else appends it to the current_path."""
        if self.current_path and self.current_path[-1] == connection:
            self.current_path.pop()
        else:
            self.current_path.append(connection)
        self.current_point = connection.move_from(self.current_point)

    def fast_backtrack(self):
        if self.current_point == self.goal:
            self.path_holder.append(self.current_path[:])
            return
        for connection in self.distance_ordered():
            if connection not in self.current_path:
                self.move_unmove(connection)
                self.fast_backtrack()
                self.move_unmove(connection)


def calc_price(path):
    return sum([connection.price for connection in path])


class Bot(BotHolder):

    def move_path(self, ):
        for connection in self.path:
            connection.move_from(self.current_point)

    def take_path(self, connection):
        self.current_point = connection.move_from(self.current_point)

    def price(self):
        return sum([connection.price for connection in self.path])

    def current_price(self):
        return sum([connection.price for connection in self.current_path])

    def find_path(self):
        action = ""
        while not action:
            new_log = []
            action = input("Please enter your preferred method [normal/fast/quit]:\n>>>").lower()[0]
            if action == "n":
                self.backtrack()
                self.path = self.path_holder[[calc_price(path) for path in self.path_holder].index(
                    min([calc_price(path) for path in self.path_holder]))]
                self.investment = self.price()
                [self.take_path(connection) for connection in self.path]
                new_log = debug_print_maze(self.maze, self, "Backtrack, normal")
                self.investment = 0
                [self.take_path(connection) for connection in self.path[::-1]]
                self.path, self.path_holder = ([], [])
            elif action == "f":
                self.fast_backtrack()
                self.path = self.path_holder[[calc_price(path) for path in self.path_holder].index(min([calc_price(path) for path in self.path_holder]))]
                self.investment = self.price()
                [self.take_path(connection) for connection in self.path]
                new_log = debug_print_maze(self.maze, self, "Backtrack, fast")
            elif action == "q":
                break
            else:
                print("Invalid input")
            return new_log

    def __init__(self, maze: PointBuilding, bot_name: str = "Fred"):
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

    #     # if self.current_location == self.goal:
    #     #     if not self.path:
    #     #         self.path = self.current_path
    #     #     if self.current_price() < self.price():
    #     #         self.path = self.current_path
    #     # for connection in self.current_location.connections:
    #     #     if connection not in self.current_path:
    #     #         self.take_path(connection)
    #     #         self.find_path1()
    #     #         self.untake_path(connection)
    #     # print(self.path)
    #     # self.investment = self.price()
    #     # self.move_path()
    #
    # def find_path(self):
    #     """Take the fastest path, from current_point to goal by orienting py Points and Connections"""
    #     while not self.current_point == self.goal:
    #         pass
    #
    #     # while not self.current_point == self.goal:
    #     #     if self.current_point.id + 1 < self.goal.id:
    #     #         self.path.append(self.current_point.connections_up[1])
    #     #         self.current_point = self.current_point.connections_up[1].move_from(self, self.current_point)
    #     #     elif self.current_point.id < self.goal.id:
    #     #         self.path.append(self.current_point.connections_up[0])
    #     #         self.current_point = self.current_point.connections_up[0].move_from(self, self.current_point)
    #     #     elif self.current_point.id - 1 > self.goal.id:
    #     #         self.path.append(self.current_point.connections_down[1])
    #     #         self.current_point = self.current_point.connections_down[1].move_from(self, self.current_point)
    #     #     else:
    #     #         self.path.append(self.current_point.connections_down[0])
    #     #         self.current_point = self.current_point.connections_down[0].move_from(self, self.current_point)
    #
    # # Backtracking
