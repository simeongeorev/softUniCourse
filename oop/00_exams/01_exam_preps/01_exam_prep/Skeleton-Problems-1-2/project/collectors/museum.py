from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):

    def __init__(self, name: str):
        super().__init__(name, available_money=15_000.0, available_space=2_000)

    def increase_money(self):
        self.available_money += 1_000.0