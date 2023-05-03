from map_build import PointBuilding, debug_print_maze, Timer
from map_build_assets.bot import Bot


def main():
    # TODO 1. Build the maze
    timer = Timer()
    maze = PointBuilding(8)
    maze.rebuild_build_points(size=14, distance=(1, 3), price_start=1, price_end=10)
    fred = Bot(maze=maze)
    debug_print_maze(maze, fred)
    fred.find_path1()
    debug_print_maze(maze, fred)
    timer.end_time()


if __name__ == "__main__":
    main()
