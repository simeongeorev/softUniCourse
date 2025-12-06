from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    def store_stats(self):
        rows = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        rows.append(self.get_estimated_profit())
        rows.append(f"**Toys for sale:")
        if self.products:
            sorted_products = sorted(self.products, key=lambda x: x.model)

            products_dict = {}
            for prod in sorted_products:
                if prod.model not in products_dict:
                    products_dict[prod.model] = []
                products_dict[prod.model].append(prod.price)

            dict_details_list = [f"{k}: {len(v)}pcs, average price: {sum(v) / len(v):.2f}" for k, v in
                                 products_dict.items()]

            rows.append("\n".join(dict_details_list))

        return "\n".join(rows)
