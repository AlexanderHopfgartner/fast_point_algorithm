from map_build import PointBuilding, debug_print_maze, Timer
from map_build_assets.bot import Bot
from log_save import log_save


def main():
    timer = Timer()
    maze = PointBuilding(size=6, distances=(1, 3), start=2, end=4)
    fred = Bot(maze=maze)
    log = debug_print_maze(maze, fred, "Default")
    fred.find_path(timer)
    new_log = debug_print_maze(maze, fred, "Backtrack, normal")
    for item in new_log:
        log.append(item)
    print(timer.time_passed())
    log_save(log, timer.time_passed())
    print(timer.time_passed())


if __name__ == "__main__":
    main()
