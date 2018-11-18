from game import World, Grid


def main():
    world = World(
        Grid(
            3,
            [
                [False, False, False],
                [True, True, True],
                [False, False, False]
            ]
        )
    )
    for i in range(100):
        world.tick()
    for event in world.history:
        for row in event.display():
            print(" ".join(row))
        print("\n")


if __name__ == '__main__':
    main()
