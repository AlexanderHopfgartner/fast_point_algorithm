from map_build import PointBuilding, debug_print_maze, Timer
from map_build_assets.bot import Bot


def main():
    # TODO 1. Build the maze
    timer = Timer()
    maze = PointBuilding(64)
    print(maze.start)
    fred = Bot(maze=maze)
    fred.find_path()
    debug_print_maze(maze, fred)
    timer.end_time()


if __name__ == "__main__":
    main()
