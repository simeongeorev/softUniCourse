from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):

    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        rows = ["@Royal Zone Statistics@"]
        rows.append(f"Code: {self.code}; Volume: {self.volume}")
        rows.append(f"Battleships currently in the Royal Zone: {len(self.ships)},"
                    f" {len([x for x in self.ships if type(x) == PirateBattleship])}"
                    f" out of them are Pirate Battleships.")
        if self.ships:
            ships_info = ", ".join([x.name for x in self.get_ships()])
            rows.append(f"#{ships_info}#")
        return "\n".join(rows)

