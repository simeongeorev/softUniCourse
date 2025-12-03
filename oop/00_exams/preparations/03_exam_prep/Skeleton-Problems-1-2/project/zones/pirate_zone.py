from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):

    def __init__(self, code: str):
        super().__init__(code, volume=8)

    def zone_info(self):
        rows = ["@Pirate Zone Statistics@"]
        rows.append(f"Code: {self.code}; Volume: {self.volume}")
        rows.append(f"Battleships currently in the Pirate Zone: {len(self.ships)},"
                    f" {len([x for x in self.ships if type(x) == RoyalBattleship])}"
                    f" out of them are Royal Battleships.")
        if self.ships:
            ships_info = ", ".join([x.name for x in self.get_ships()])
            rows.append(f"#{ships_info}#")
        return "\n".join(rows)

