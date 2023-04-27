from map_build import Bot, build, debug_print_maze, clear


def main():

    # TODO 1. Build the maze
    size = 10
    maze = build(size)
    debug_print_maze(maze)
    bot = Bot("Fridolin", maze.start)
    input()
    clear()

    # TODO 1.1. Build the points

    # TODO 1.2. Connect the points


if __name__ == "__main__":
    main()
