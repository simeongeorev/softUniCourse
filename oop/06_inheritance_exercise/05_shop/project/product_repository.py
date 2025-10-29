from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        current_product = next((p for p in self.products if p.name == product_name), None)
        if current_product:
            return current_product
        return None

    def remove(self, product_name: str) -> None:
        current_product = next((p for p in self.products if p.name == product_name), None)
        self.products.remove(current_product) if current_product else None

    def __repr__(self):
        products_details = "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
        return products_details
