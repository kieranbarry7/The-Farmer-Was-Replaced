def navigate_to(target_x, target_y):
    while get_pos_x() < target_x:
        move(East)

    while get_pos_x() > target_x:
        move(West)

    while get_pos_y() < target_y:
        move(North)

    while get_pos_y() > target_y:
        move(South)


def prepare_cactus_field():
    grid_dim = get_world_size()

    navigate_to(0, 0)

    for col in range(grid_dim):
        for row in range(grid_dim):

            if get_ground_type() == Grounds.Grassland:
                till()

            if get_entity_type() != Entities.Cactus:
                plant(Entities.Cactus)

            if row < grid_dim - 1:
                move(North)

        if col < grid_dim - 1:
            navigate_to(col + 1, 0)


def sort_single_column(col_idx):
    grid_dim = get_world_size()

    low_bound = 0
    high_bound = grid_dim - 1

    while low_bound < high_bound:

        did_swap = False

        for row in range(low_bound, high_bound):
            navigate_to(col_idx, row)

            if measure() > measure(North):
                swap(North)
                did_swap = True

        if not did_swap:
            break

        high_bound = high_bound - 1

        did_swap = False

        for row in range(high_bound, low_bound, -1):
            navigate_to(col_idx, row)

            if measure() < measure(South):
                swap(South)
                did_swap = True

        if not did_swap:
            break

        low_bound = low_bound + 1


def sort_single_row(row_idx):
    grid_dim = get_world_size()

    low_bound = 0
    high_bound = grid_dim - 1

    while low_bound < high_bound:

        did_swap = False

        for col in range(low_bound, high_bound):
            navigate_to(col, row_idx)

            if measure() > measure(East):
                swap(East)
                did_swap = True

        if not did_swap:
            break

        high_bound = high_bound - 1

        did_swap = False

        for col in range(high_bound, low_bound, -1):
            navigate_to(col, row_idx)

            if measure() < measure(West):
                swap(West)
                did_swap = True

        if not did_swap:
            break

        low_bound = low_bound + 1


def organize_cacti_grid():
    grid_dim = get_world_size()

    # Sort every row first
    for r_idx in range(grid_dim):
        sort_single_row(r_idx)

    # Then sort every column
    for c_idx in range(grid_dim):
        sort_single_column(c_idx)


while True:

    prepare_cactus_field()

    # Wait until the cactus at 0,0 has grown
    navigate_to(0, 0)

    while not can_harvest():
        pass

    organize_cacti_grid()

    navigate_to(0, 0)

    harvest()