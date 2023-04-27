from map_build import Bot, PointBuilding, debug_print_maze, clear, Timer


def main():

    # TODO 1. Build the maze
    size = int(input("size: "))
    timer = Timer()
    maze = PointBuilding(size)
    debug_print_maze(maze)
    timer.end_time()


    # TODO 1.1. Build the points

    # TODO 1.2. Connect the points


if __name__ == "__main__":
    main()
