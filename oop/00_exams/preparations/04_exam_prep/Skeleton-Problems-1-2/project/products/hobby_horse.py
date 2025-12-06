from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    DISCOUNT_PERCENT = 20

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material="Wood/Plastic", sub_type="Toys")

    def discount(self):
        self.price *= ((100 - self.DISCOUNT_PERCENT) / 100)

