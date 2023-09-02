from typing import Optional

from BaseClasses import Item, ItemClassification

from .constants import FE8_NAME, FE8_ID_PREFIX


class FE8Item(Item):
    game = FE8_NAME

    def __init__(
        self,
        name: str,
        cls: ItemClassification,
        code: int,
        player: int,
    ):
        super(FE8Item, self).__init__(name, cls, FE8_ID_PREFIX + code, player)
        self.event = None

    def local_id(self) -> Optional[int]:
        if self.code is not None:
            return self.code - FE8_ID_PREFIX
        else:
            return None
