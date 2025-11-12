from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans : list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    @staticmethod
    def add_entry(obj, collection: list):
        if obj not in collection:
            collection.append(obj)

    def add_customer(self, customer: Customer):
        self.add_entry(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_entry(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_entry(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_entry(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_entry(subscription, self.subscriptions)

    @staticmethod
    def get_repr_by_id(collection, search_id):
        return next((x.__repr__() for x in collection if x.id == search_id), None)

    def subscription_info(self, subscription_id: int):
        result = self.get_repr_by_id(self.subscriptions, subscription_id) + "\n"
        result += self.get_repr_by_id(self.customers, subscription_id) + "\n"
        result += self.get_repr_by_id(self.trainers, subscription_id) + "\n"
        result += self.get_repr_by_id(self.equipment, subscription_id) + "\n"
        result += self.get_repr_by_id(self.plans, subscription_id)
        return result
