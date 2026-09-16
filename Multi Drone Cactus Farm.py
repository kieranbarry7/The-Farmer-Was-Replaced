import UtilsMDCactus as utils
from cactus import plant_column
from CactusCocktailSort import cocktail_sort


# multi-drone task assignment function that dispatches workers to perform a given task in parallel.
def dispatch_workers(task_worker, axis_dir):
    utils.move_to(0, 0)
    workers = []
    total_workers = min(max_drones(), get_world_size())

    for _ in range(total_workers):
        bot = spawn_drone(task_worker)
        if bot:
            workers.append(bot)
        else:
            task_worker()
        move(axis_dir)

    for bot in workers:
        wait_for(bot)

# initial task of all drones planting cacti seeds in a column.
def seed_field():
    def process_column():
        col_idx = get_pos_x()
        grid_dim = get_world_size()
        while col_idx < grid_dim:
            plant_column(col_idx)
            col_idx += max_drones()

    dispatch_workers(process_column, East)

# second task of all drones sorting the cacti in a column using cocktail sort.
def sort_vertical():
    def process_column():
        col_idx = get_pos_x()
        grid_dim = get_world_size()
        while col_idx < grid_dim:
            cocktail_sort(col_idx, True)
            col_idx += max_drones()

    dispatch_workers(process_column, East)

# third task of all drones sorting the cacti in a row using cocktail sort.
def sort_horizontal():
    def process_row():
        row_idx = get_pos_y()
        grid_dim = get_world_size()
        while row_idx < grid_dim:
            cocktail_sort(row_idx, False)
            row_idx += max_drones()

    dispatch_workers(process_row, North)

# the main loop that continuously seeds the field, sorts the cacti vertically and horizontally, and returns to the starting position to repeat the process.
while True:
    seed_field()
    sort_vertical()
    sort_horizontal()
    utils.move_to(0, 0)
    harvest()