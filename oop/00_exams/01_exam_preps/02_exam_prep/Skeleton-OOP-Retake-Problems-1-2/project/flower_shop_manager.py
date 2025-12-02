from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS = {"Flower": Flower,
                    "LeafPlant": LeafPlant}
    VALID_CLIENTS = {"RegularClient": RegularClient,
                     "BusinessClient": BusinessClient}

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self,
                  plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        plant = self.VALID_PLANTS[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def get_client_by_number(self, searched_number) -> BaseClient | None:
        return next((c for c in self.clients if c.phone_number == searched_number), None)

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        if self.get_client_by_number(client_phone_number) is not None:
            raise ValueError("This phone number has been used!")

        client = self.VALID_CLIENTS[client_type](client_name, client_phone_number)
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = self.get_client_by_number(client_phone_number)
        if client is None:
            raise ValueError("Client not found!")

        matching_plants = [p for p in self.plants if p.name == plant_name]

        if not matching_plants:
            raise ValueError("Plants not found!")

        if len(matching_plants) < plant_quantity:
            return "Not enough plant quantity."

        matching_plants = matching_plants[:plant_quantity]

        self.plants = [p for p in self.plants if p not in matching_plants]

        plants_price = sum([p.price for p in matching_plants])
        if client.discount != 0:
            plants_price -= (plants_price * (client.discount / 100))

        self.income += plants_price

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {plants_price:.2f}"

    def remove_plant(self, plant_name: str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return "No such plant name."

        self.plants.remove(plant)

        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        empty_clients = [c for c in self.clients if c.total_orders == 0]
        self.clients = [c for c in self.clients if c.total_orders > 0]

        return f"{len(empty_clients)} client/s removed."

    def shop_report(self):
        total_orders = sum(client.total_orders for client in self.clients)
        result = f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {total_orders}\n~~Unsold plants: {len(self.plants)}~~\n"

        plants_dict = {}
        for p in self.plants:
            if p.name not in plants_dict:
                plants_dict[p.name] = 0
            plants_dict[p.name] += 1
        sorted_plants = sorted(plants_dict.items(), key=lambda x: (-x[1], x[0]))
        plant_details = [f"{x[0]}: {x[1]}" for x in sorted_plants]
        result += "\n".join(plant_details) + "\n"

        result += f"~~Clients number: {len(self.clients)}~~\n"
        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))
        client_details_list = [c.client_details() for c in sorted_clients]
        result += "\n".join(client_details_list)

        return result



