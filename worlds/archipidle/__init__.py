from BaseClasses import Region, Location, Item, ItemClassification
from worlds.AutoWorld import World

ARCHIPIDLE_NAME = "ArchipIDLE"
BASE_ID = 9000
NUM_LOCATIONS = 65

ITEM_NAME_TO_ID = {
    "GeoCities Website":  BASE_ID + 0,
    "Dad Joke":           BASE_ID + 1,
    "Motivational Video": BASE_ID + 2,
    "Junk Mail":          BASE_ID + 3,
}

LOCATION_NAME_TO_ID = {
    f"ArchipIDLE - Idle {n}": BASE_ID + (n - 1)
    for n in range(1, NUM_LOCATIONS + 1)
}


class ArchipIDLEItem(Item):
    game = ARCHIPIDLE_NAME


class ArchipIDLELocation(Location):
    game = ARCHIPIDLE_NAME


class ArchipIDLEWorld(World):
    """ArchipIDLE is a browser-based idle game for Archipelago multiworlds."""

    game = ARCHIPIDLE_NAME
    topology_present = False
    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    def create_item(self, name: str) -> ArchipIDLEItem:
        cls = ItemClassification.filler if name == "Junk Mail" else ItemClassification.useful
        return ArchipIDLEItem(name, cls, ITEM_NAME_TO_ID[name], self.player)

    def create_items(self) -> None:
        pool = [
            self.create_item("GeoCities Website"),
            self.create_item("Dad Joke"),
            self.create_item("Motivational Video"),
        ]
        pool += [self.create_item("Junk Mail") for _ in range(NUM_LOCATIONS - 3)]
        self.multiworld.itempool += pool

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        menu.add_locations(LOCATION_NAME_TO_ID, ArchipIDLELocation)
