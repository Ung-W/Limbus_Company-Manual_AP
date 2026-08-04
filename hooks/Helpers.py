from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
    
def single_run_floor(location, locationRemove_list):
    # If the location is a "Boss x - Completion"
    if "Completion" in location and not location.endswith("Boss - Completion"):
        locationRemove_list.append(location)
        return False
    # If the location is a "Reward"
    if location.endswith("Reward"):
        locationRemove_list.append(location)
    
    return True
        
def process_location_removal(location, locationRemove_list, lastFloor_cond, runs_list, run_amount):
    loc_cat = location[1]["category"]
    loc_name = location[1]["name"]
    
    is_single_run = any(run in loc_cat for run in ["Run 0", "Run 1"])
    is_invalidRun = not any(run in loc_cat for run in runs_list[:run_amount])
    
    if not lastFloor_cond:
        if run_amount == 1 and is_single_run:
            single_run_floor(loc_name, locationRemove_list)
        elif is_invalidRun:
            locationRemove_list.append(loc_name)

    elif is_single_run:
        single_run_floor(loc_name, locationRemove_list)

    else:
        locationRemove_list.append(loc_name)
        
def process_reg_loc_removal(multiworld, player, regionRemove_list, locationRemove_list):
    for region in multiworld.regions:
        if region.player == player:
            if region.name in regionRemove_list:
                for location in list(region.locations):
                    region.locations.remove(location)

        for location in list(region.locations):
            if location.name in locationRemove_list:
                region.locations.remove(location)
        
def run_progression_selected(world, floor_list, runs_list, unplayableFloors):
    removed_floors = set(unplayableFloors)                       

    for loc in world.location_name_to_location.items():
        category = loc[1]["category"]
        
        if any(floor in category for floor in removed_floors):
            continue

        floor = next((f for f in floor_list if f in category), None)
        run = next((r for r in runs_list if r in category), None)

        if floor is None or run is None:
            continue
        if floor == "Floor 15":
            continue
        
        if loc[1]["name"].endswith("Reward"):
            loc[1]["requires"] = f"|{floor} Cleared: {runs_list.index(run) + 1}|"
        else:
            loc[1]["requires"] = f"|{floor} Cleared: {runs_list.index(run)}|"
            
def open_progression_selected(world):
    for loc in world.location_name_to_location.items():
        if loc[1]["category"] != "VICTORY":
            loc[1].pop("requires", None)
        
def get_required_sinners(win_cond):
    if win_cond >= 13:
        return 12
    elif win_cond >= 8:
        return 7
    elif win_cond >= 5:
        return 3
    return 0

def add_item_if_missing(item_pool, world, player, item_name):
    if not any(item.player == player and item.name == item_name for item in item_pool):
        item_pool.append(world.create_item(item_name))
        
def add_starting_item(starting_items, items, warning=None, sinner_sel=None, random=1):
    entry = {
        "items": items,
        "random": random
    }

    if sinner_sel is not None:
        entry["sinner_selected"] = sinner_sel

    if warning:
        entry["warning"] = True

    starting_items.append(entry)
        
def get_possible_starting_items(item_pool, starting_data):
    # get all unique item names from the starting_data
    item_names = set(starting_data.get("items", []))
    test = [item for item in item_pool if item.name in item_names]
    return [item for item in item_pool if item.name in item_names]

def build_sin_included(sinners, sins, sin_banned, id_banned):
    sin_included = {}
    
    # Get the Sins excluded by the player for each indicated Sinner
    for excluded in id_banned:
        sinner, sin = (x.strip() for x in excluded.split("/"))
        sin_banned[sinner].append(sin)

    # If Sinner has no excluded combo, add every possibility to starting items
    for sinner in sinners:
        sin_included[sinner] = [
            sin for sin in sins
            if sin not in sin_banned[sinner]
        ]

    return sin_included