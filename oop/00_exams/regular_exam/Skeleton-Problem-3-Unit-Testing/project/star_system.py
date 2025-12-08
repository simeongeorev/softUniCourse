from typing import Optional

class StarSystem:
    _STAR_TYPES = {'Red giant', 'Blue giant', 'Yellow dwarf', 'Red dwarf', 'Brown dwarf'}
    _STAR_SYSTEM_TYPES = {'Single', 'Binary', 'Triple', 'Multiple'}

    def __init__(self,
                 name: str,
                 star_type: str,
                 system_type: str,
                 num_planets: int,
                 habitable_zone_range: Optional[tuple] = None):
        self.name = name
        self.num_planets = num_planets
        self.star_type = star_type
        self.system_type = system_type
        self.habitable_zone_range = habitable_zone_range

    @property
    def is_habitable(self) -> bool:
        return self.habitable_zone_range is not None and self.num_planets > 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def star_type(self):
        return self._star_type

    @star_type.setter
    def star_type(self, value):
        if value not in self._STAR_TYPES:
            raise ValueError(f"Star type must be one of {sorted(self._STAR_TYPES)}.")
        self._star_type = value

    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        if value not in self._STAR_SYSTEM_TYPES:
            raise ValueError(f"System type must be one of {sorted(self._STAR_SYSTEM_TYPES)}.")
        self._system_type = value

    @property
    def num_planets(self):
        return self._num_planets

    @num_planets.setter
    def num_planets(self, value):
        if value < 0:
            raise ValueError("Number of planets must be a non-negative integer.")
        self._num_planets = value

    @property
    def habitable_zone_range(self):
        return self._habitable_zone_range

    @habitable_zone_range.setter
    def habitable_zone_range(self, value):
        if value is not None:
            if len(value) != 2 or value[0] >= value[1]:
                raise ValueError("Habitable zone range must be a tuple of two numbers (start, end) where start < end.")
        self._habitable_zone_range = value

    def __gt__(self, other: 'StarSystem') -> bool:
        if not self.is_habitable or not other.is_habitable:
            raise ValueError( "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

        self_range = self.habitable_zone_range[1] - self.habitable_zone_range[0]
        other_range = other.habitable_zone_range[1] - other.habitable_zone_range[0]

        return self_range > other_range

    @staticmethod
    def compare_star_systems(system_one: 'StarSystem', system_two: 'StarSystem') -> str:
        try:
            if system_one > system_two:
                return f"{system_one.name} has a wider habitable zone than {system_two.name}."
            return f"{system_two.name} has a wider or equal habitable zone compared to {system_one.name}."
        except ValueError as error:
            return str(error)