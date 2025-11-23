from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    DESKTOP_COMP = "Desktop Computer"
    LAPTOP_COMP = "Laptop"

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == self.DESKTOP_COMP:
            comp = DesktopComputer(manufacturer, model)
        elif type_computer == self.LAPTOP_COMP:
            comp = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        conf_result = comp.configure_computer(processor, ram)
        self.warehouse.append(comp)
        return conf_result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        valid_comp = next((c for c in self.warehouse
                           if c.price <= client_budget
                           and c.processor == wanted_processor
                           and c.ram >= wanted_ram), None)

        if not valid_comp:
            raise Exception("Sorry, we don't have a computer for you.")

        price_difference = client_budget - valid_comp.price
        self.profits += price_difference
        return f"{valid_comp.__repr__()} sold for {client_budget}$."
