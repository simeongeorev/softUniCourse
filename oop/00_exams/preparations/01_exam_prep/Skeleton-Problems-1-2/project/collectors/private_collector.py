from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):

    def __init__(self, name: str):
        super().__init__(name, available_money=25_000.0, available_space=3_000)

    def increase_money(self):
        self.available_money += 5_000.0