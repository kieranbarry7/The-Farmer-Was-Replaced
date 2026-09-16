while True:
    world_size = get_world_size()
    patch_size = world_size // 2
    if world_size >= 8:
        patch_size = 6
    if patch_size > 6:
        patch_size = 6
    if patch_size > world_size:
        patch_size = world_size
    if patch_size < 1:
        patch_size = 1

    ready_count = 0
    dead_count = 0
    col_index = 0
    while col_index < world_size:
        row_index = 0
        while row_index < world_size:
            pos_x = get_pos_x()
            pos_y = get_pos_y()

            if pos_x < patch_size and pos_y < patch_size:
                if get_ground_type() != Grounds.Soil:
                    till()

                current_entity = get_entity_type()

                if current_entity == Entities.Dead_Pumpkin:
                    dead_count = dead_count + 1
                    plant(Entities.Pumpkin)
                elif current_entity == Entities.Pumpkin:
                    if can_harvest():
                        ready_count = ready_count + 1
                else:
                    if can_harvest():
                        harvest()
                    plant(Entities.Pumpkin)
            else:
                if can_harvest():
                    harvest()
                tile_sum = pos_x + pos_y
                if tile_sum % 8 == 0:
                    if get_ground_type() != Grounds.Grassland:
                        till()
                    plant(Entities.Tree)
                elif tile_sum % 8 <= 5:
                    if get_ground_type() != Grounds.Grassland:
                        till()
                else:
                    if get_ground_type() != Grounds.Soil:
                        till()
                    plant(Entities.Carrot)

            if get_water() < 0.5:
                use_item(Items.Water)

            move(North)
            row_index = row_index + 1
        move(East)
        col_index = col_index + 1

    if dead_count == 0:
        if ready_count >= patch_size * patch_size:
            while get_pos_x() != 0:
                move(West)
            while get_pos_y() != 0:
                move(South)
            if can_harvest():
                harvest()