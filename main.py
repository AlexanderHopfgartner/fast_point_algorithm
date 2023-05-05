from map_build import PointBuilding, debug_print_maze
from map_build_assets.bot import Bot
from log_save import log_save


def distance_div(start, distance):
    print(start + distance)
    return start


def main():
    maze = PointBuilding(size=512, distances=(1, 3, 5, 7, 11), start=3, end=500)
    fred = Bot(maze=maze)
    log = debug_print_maze(maze, fred, "Default")
    new_log = fred.find_path()
    for item in new_log:
        log.append(item)
    log_save(log)


if __name__ == "__main__":
    main()
