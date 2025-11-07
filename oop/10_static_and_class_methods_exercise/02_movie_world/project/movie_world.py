from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def get_customer_by_id(self, customer_id):
        return next((c for c in self.customers if c.id == customer_id), None)

    def get_dvd_by_id(self, dvd_id):
        return next((d for d in self.dvds if d.id == dvd_id), None)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        cur_customer = self.get_customer_by_id(customer_id)
        cur_dvd = self.get_dvd_by_id(dvd_id)

        if cur_dvd in cur_customer.rented_dvds:
            return f"{cur_customer.name} has already rented {cur_dvd.name}"

        if cur_dvd.is_rented:
            return "DVD is already rented"

        if cur_customer.age < cur_dvd.age_restriction:
            return f"{cur_customer.name} should be at least {cur_dvd.age_restriction} to rent this movie"

        cur_dvd.is_rented = True
        cur_customer.rented_dvds.append(cur_dvd)
        return f"{cur_customer.name} has successfully rented {cur_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        cur_customer = self.get_customer_by_id(customer_id)
        cur_dvd = self.get_dvd_by_id(dvd_id)

        if cur_dvd in cur_customer.rented_dvds:
            cur_customer.rented_dvds.remove(cur_dvd)
            cur_dvd.is_rented = False
            return f"{cur_customer.name} has successfully returned {cur_dvd.name}"

        return f"{cur_customer.name} does not have that DVD"


    def __repr__(self):
        customers = self.get_details(self.customers)
        result = "\n".join(customers) + "\n"

        dvds = self.get_details(self.dvds)
        result += "\n".join(dvds)

        return result

    @staticmethod
    def get_details(collection):
        return [c.__repr__() for c in collection]

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

