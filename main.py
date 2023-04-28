from map_build import Bot, PointBuilding, debug_print_maze, clear, Timer
from time import time, sleep



def main():
    # TODO 1. Build the maze
    size = int(input("size: "))
    timer = Timer()
    maze = PointBuilding(size)
    debug_print_maze(maze)
    timer.end_time()
    timer1 = Timer()
    fred = Bot(bot_name="Fred", maze=maze)
    fred.find_path()
    print(fred.current_point)
    print(fred.investment)
    timer1.end_time()


    # TODO 1.1. Build the points

    # TODO 1.2. Connect the points


if __name__ == "__main__":
    main()
