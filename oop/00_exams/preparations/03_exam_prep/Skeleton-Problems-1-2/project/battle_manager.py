
from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES = {"RoyalZone": RoyalZone,
                   "PirateZone": PirateZone}

    VALID_BATTLESHIPS = {"RoyalBattleship": RoyalBattleship,
                         "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        # check if zone is of valid type
        if zone_type not in self.VALID_ZONES:
            raise Exception("Invalid zone type!")

        # check if zone already exists
        if any(x.code == zone_code for x in self.zones):
            raise Exception("Zone already exists!")

        # adding the zone to the list
        zone = self.VALID_ZONES[zone_type](zone_code)  # creating new zone
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.VALID_BATTLESHIPS:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = self.VALID_BATTLESHIPS[ship_type](name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        zone_type_str: str = type(zone).__name__[:3]
        ship_type_str: str = type(ship).__name__[:3]
        if zone_type_str != ship_type_str:
            ship.is_attacking = False
        else:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((x for x in self.ships if x.name == ship_name), None)

        if not ship:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        is_attacking_present = any(x.is_attacking == True for x in zone.ships)
        not_attacking_present = any(x.is_attacking == False for x in zone.ships)
        if not is_attacking_present or not not_attacking_present:
            return "Not enough participants. The battle is canceled."

        zone_type_str: str = type(zone).__name__[:3]

        is_attacking_ships_matching_zone = [y for y in zone.ships
                                            if y.is_attacking and type(y).__name__[:3] == zone_type_str]
        attacking_ship = sorted(is_attacking_ships_matching_zone, key = lambda x: -x.hit_strength)[0]

        not_attacking_ships_matching_zone = [y for y in zone.ships
                                            if not y.is_attacking and type(y).__name__[:3] != zone_type_str]
        enemy_ship = sorted(not_attacking_ships_matching_zone, key = lambda x: -x.health)[0]

        # battle begins
        attacking_ship.attack()
        enemy_ship.take_damage(attacking_ship)

        if enemy_ship.health <= 0:
            zone.ships.remove(enemy_ship)
            self.ships.remove(enemy_ship)
            return f"{enemy_ship.name} lost the battle and was sunk."

        if attacking_ship.ammunition <= 0:
            zone.ships.remove(attacking_ship)
            self.ships.remove(attacking_ship)
            return f"{attacking_ship.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [x.name for x in self.ships if x.is_available]
        rows = [f"Available Battleships: {len(available_ships)}"]
        if available_ships:
            available_ships_str = ", ".join(available_ships)
            rows.append(f"#{available_ships_str}#")
        rows.append("***Zones Statistics:***")
        rows.append(f"Total Zones: {len(self.zones)}")
        sorted_zones = sorted(self.zones, key=lambda x: x.code)
        for z in sorted_zones:
            rows.append(z.zone_info())
        return "\n".join(rows)
