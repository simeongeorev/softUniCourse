from project.computer_types.computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def valid_processors(self) -> dict:
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1050,
                "Apple M1 Pro": 1200}

    @property
    def valid_ram_ceil(self) -> int:
        return 64