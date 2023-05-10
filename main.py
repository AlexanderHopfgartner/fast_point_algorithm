from map_build import PointBuilding, debug_print_maze, Distances
from map_build_assets.bot import Bot
from log_save import log_save


def distance_div(start, distance):
    print(start + distance)
    return start


def main():
    distance = Distances((1, 3, 5, 7, 11))
    maze = PointBuilding(size=32, distances=distance, start=3, end=30)
    [connection.recalculate_price(start=1, end=10) for connection in maze.connections]
    [connection.recalculate_price(start=200, end=5000) for connection in maze.connections if connection.distance > 5]
    fred = Bot(maze=maze)
    log = debug_print_maze(maze, fred, "Default")
    new_log = fred.find_path()
    for item in new_log:
        log.append(item)
    log_save(log)


if __name__ == "__main__":
    main()
