from project.animal import Animal
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def __has_animal_capacity(self):
        return True if len(self.animals) < self.__animal_capacity else False

    def __has_worker_capacity(self):
        return True if len(self.workers) < self.__workers_capacity else False

    def add_animal(self, animal: Animal, price):
        if not self.__has_animal_capacity():
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if not self.__has_worker_capacity():
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        cur_worker = next((w for w in self.workers if w.name == worker_name), None)
        if not cur_worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(cur_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        money_needed = sum([w.salary for w in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([a.money_for_care for a in self.animals])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animal_details = f"You have {len(self.animals)} animals\n"

        lions, tigers, cheetahs = [], [], []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            if animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            if animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        animal_details += f"----- {len(lions)} Lions:\n"
        if lions:
            animal_details += "\n".join([a.__repr__() for a in lions]) + "\n"

        animal_details += f"----- {len(tigers)} Tigers:\n"
        if tigers:
            animal_details += "\n".join([a.__repr__() for a in tigers]) + "\n"

        animal_details += f"----- {len(cheetahs)} Cheetahs:\n"
        animal_details += "\n".join([a.__repr__() for a in cheetahs])

        return animal_details

    def workers_status(self):
        workers_details = f"You have {len(self.workers)} workers\n"

        keepers: list[Worker] = []
        caretakers: list[Worker] = []
        vets: list[Worker] = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            if worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            if worker.__class__.__name__ == "Vet":
                vets.append(worker)

        workers_details += f"----- {len(keepers)} Keepers:\n"
        if keepers:
            workers_details += "\n".join([a.__repr__() for a in keepers]) + "\n"

        workers_details += f"----- {len(caretakers)} Caretakers:\n"
        if caretakers:
            workers_details += "\n".join([a.__repr__() for a in caretakers]) + "\n"

        workers_details += f"----- {len(vets)} Vets:\n"
        workers_details += "\n".join([a.__repr__() for a in vets])

        return workers_details

