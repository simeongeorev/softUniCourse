from copy import copy

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCT_TYPES = {"Chair": Chair,
                           "HobbyHorse": HobbyHorse}

    VALID_STORE_TYPES = {"ToyStore": ToyStore,
                         "FurnitureStore": FurnitureStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCT_TYPES:
            raise Exception("Invalid product type!")

        product = self.VALID_PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.VALID_STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        products_of_type = [x for x in products if x.sub_type[:3] == store.store_type[:3]]

        if not products_of_type:
            return "Products do not match in type. Nothing sold."

        store.products.extend(products_of_type)

        for p in products_of_type:
            self.products.remove(p)

        store.capacity -= len(products_of_type)

        price_sum = self._get_products_sum_price(products_of_type)
        self.income += price_sum

        return f"Store {store.name} successfully purchased {len(products_of_type)} items."

    def unregister_store(self, store_name: str):
        store = self._get_store_by_name(store_name)
        if store is None:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        n = 0
        for p in self.products:
            if p.model == product_model:
                p.discount()
                n += 1
        return f"Discount applied to {n} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self._get_store_by_name(store_name)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        rows = [f"Factory: {self.name}"]
        rows.append(f"Income: {self.income:.2f}")
        rows.append("***Products Statistics***")
        rows.append(f"Unsold Products: {len(self.products)}. Total net price: {self._get_products_sum_price(self.products):.2f}")

        products_dict = {}
        for p in self.products:
            if p.model not in products_dict:
                products_dict[p.model] = 0
            products_dict[p.model] += 1

        products_dict_info = [f"{k}: {v}" for k, v in sorted(products_dict.items(), key=lambda x: x[0])]
        rows.append("\n".join(products_dict_info))

        rows.append(f"***Partner Stores: {len(self.stores)}***")

        rows.append("\n".join([x.name for x in sorted(self.stores, key=lambda x: x.name)]))

        return "\n".join(rows)


    def _get_store_by_name(self, store_name):
        return next((x for x in self.stores if x.name == store_name), None)

    @staticmethod
    def _get_products_sum_price(collection):
        return sum([x.price for x in collection])




