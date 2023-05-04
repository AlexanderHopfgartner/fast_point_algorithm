from map_build import PointBuilding, debug_print_maze, Timer
from map_build_assets.bot import Bot
from log_save import log_save


def main():
    # TODO 1. Build the maze
    timer = Timer()
    maze = PointBuilding(8)
    maze.rebuild_build_points(size=8, distance=(1, 3, 5), price_start=1, price_end=10)
    fred = Bot(maze=maze)
    log = debug_print_maze(maze, fred, "Default")
    [print(line) for line in log]
    fred.find_path1()
    new_log = debug_print_maze(maze, fred, "Backtrack, normal")
    for item in new_log:
        log.append(item)
    [print(line) for line in log]
    log_save(log)
    timer.end_time()


if __name__ == "__main__":
    main()
