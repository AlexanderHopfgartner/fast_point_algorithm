from map_build import PointBuilding, debug_print_maze, Timer
from map_build_assets.bot import Bot


def main():
    # TODO 1. Build the maze
    timer = Timer()
    maze = PointBuilding(8)
    maze.rebuild_build_points(size=16, distance=(1, 3), price_start=1, price_end=12)
    fred = Bot(maze=maze)
    print()
    debug_print_maze(maze, fred)
    fred.find_path()
    debug_print_maze(maze, fred)
    timer.end_time()


if __name__ == "__main__":
    main()
