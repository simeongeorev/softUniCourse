from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    VALID_ASTRONAUT_TYPES = {"EngineerAstronaut": EngineerAstronaut,
                             "ScientistAstronaut": ScientistAstronaut}

    VALID_STATION_TYPES = {"ResearchStation": ResearchStation,
                           "MaintenanceStation": MaintenanceStation}

    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES.keys():
            raise ValueError("Invalid astronaut type!")

        if self._get_astronaut_by_id_in_collection(astronaut_id_number, self.astronauts) is not None:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astro = self.VALID_ASTRONAUT_TYPES[astronaut_type](astronaut_id_number, astronaut_salary)

        self.astronauts.append(astro)

        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.VALID_STATION_TYPES.keys():
            raise ValueError("Invalid station type!")

        if self._get_station_by_name(station_name) is not None:
            raise ValueError(f"{station_name} has been already added!")

        station = self.VALID_STATION_TYPES[station_type](station_name)

        self.stations.append(station)

        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = self._get_station_by_name(station_name)
        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astro = next((a for a in self.astronauts if a.specialization == astronaut_type), None)
        if astro is None:
            raise ValueError("No available astronauts of the type!")

        if station.capacity <= 0:
            return "This station has no available capacity."

        self.astronauts.remove(astro)

        station.astronauts.append(astro)

        station.capacity -= 1

        return f"{astro.id_number} was assigned to {station_name}."

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for a in station.astronauts:
                a.train()

        total_stamina = sum([a.stamina for a in station.astronauts])
        return (f"{station.name} astronauts have {total_stamina} "
                f"total stamina after {sessions_number} training session/s.")

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astro = self._get_astronaut_by_id_in_collection(astronaut_id_number, station.astronauts)
        if astro is None or astro.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astro)
        station.capacity += 1

        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for s in self.stations:
            s.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda x: (-len(x.astronauts), x.name))

        rows = ["*Space Agency Up-to-Date Report*"]
        rows.append(f"Total number of available astronauts: {len(self.astronauts)}")

        total_available_capacity = sum([s.capacity for s in self.stations])
        rows.append(f"**Stations count: {len(self.stations)}; Total available capacity: {total_available_capacity}**")

        stations_info = [s.status() for s in sorted_stations]
        rows.extend(stations_info)

        return "\n".join(rows)

    # HELPERS
    def _get_station_by_name(self, s_name):
        return next((s for s in self.stations if s.name == s_name), None)

    @staticmethod
    def _get_astronaut_by_id_in_collection(a_id, collection) -> BaseAstronaut | None:
        return next((a for a in collection if a.id_number == a_id), None)