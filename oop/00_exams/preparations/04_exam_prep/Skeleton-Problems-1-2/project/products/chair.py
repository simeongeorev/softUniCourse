from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    DISCOUNT_PERCENT = 10

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material='Wood', sub_type='Furniture')

    def discount(self):
        self.price *= ((100 - self.DISCOUNT_PERCENT) / 100)
