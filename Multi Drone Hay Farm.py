clear()
GRID_SIZE = get_world_size()
change_hat(Hats.Brown_Hat)

# setting the companion crop map dictionaries
companion_crop_map = {}  # Maps (target_x, target_y) -> Entities
companion_source_map = {} # Maps (curr_x, curr_y) -> (target_x, target_y)

# function to register companion crops based on the current position and the target companion entity
def register_companion(curr_x, curr_y):
    companion_data = get_companion()
    if companion_data is None:
        return False
        
    target_entity, target_pos = companion_data

    # check if the target position is already registered in the companion crop map
    if target_pos not in companion_crop_map:
        companion_crop_map[target_pos] = target_entity
        companion_source_map[(curr_x, curr_y)] = target_pos
        return True 
    return False

# function to execute the companion farming logic for each drone
def execute_companion_farming():
    while True:
        for _ in range(GRID_SIZE):
            curr_pos = (get_pos_x(), get_pos_y())
            
            harvest()
            
            if get_ground_type() == Grounds.Soil:
                till()

            # check if the current position has a registered companion crop
            if curr_pos in companion_crop_map:
                required_companion = companion_crop_map[curr_pos]
                
                if required_companion == Entities.Carrot:
                    if get_ground_type() != Grounds.Soil:
                        till()
                    plant(Entities.Carrot)
                elif required_companion != Entities.Grass:
                    plant(required_companion)
            else:
                # if the current position is not registered, attempt to register a new companion crop
                if curr_pos in companion_source_map:
                    target_pos = companion_source_map.pop(curr_pos)
                    companion_crop_map.pop(target_pos, None)
                
                register_companion(curr_pos[0], curr_pos[1])
                
            move(North) 

# deploy drones across the grid to farm the crop
for _ in range(GRID_SIZE - 1):
    while num_drones() >= max_drones():
        pass
    spawn_drone(execute_companion_farming)
    move(East)

# executes the companion farming logic for the initial drone
execute_companion_farming()